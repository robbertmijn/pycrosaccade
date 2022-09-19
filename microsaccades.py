#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 16:30:18 2022

@author: robbertmijn
"""
#%%
from datamatrix import (
    series as srs,
    SeriesColumn
    )
import numpy as np

#%%
def find_microsaccades(xtrace, ytrace, msVthres = 6, mindur = 9, maxdur = 50, 
                  mindist = .08, maxdist = 2, saccISI = 50, 
                  vel_smooth = 7, pix2degree = 1/34.6, sampfreq = 1000):
    
    """
    desc:
        Get microsaccades for a trace of x and y coordinates for a single trial
        Returns three lists with respectively first sample, last sample and the distance travelled during the microsaccade.
        
    arguments:
        xtrace: SeriesColumn with x coordinates
        ytrace: SeriesColumn with y coordinates
        msVthres: Velocity threshold of eye movement to mark a microsaccade. Its unit is the number of median absoute deviations the velocity must deviate from the median velocity for each trial.
        mindur: minumum duration for the velocity to be above threshold for it to be considered a saccade
        maxdur: saccades longer than maxdur are not considered
        mindist: minimum distance the gaze has to travel
        maxdist: maximum distance the gaze has to travel
        saccISI: At least this many samples must pass before a new microsaccade is considered
        smooth_winlen: number of samples taken together to form moving average
        vel_smooth: How many samples to smooth over gaze velocity
        pix2degree: depending on distance to screen and resolution, how many pixels make up one degree visual angle
        sampfreq: sampling frequency
        
    """

    # initiate lists for start time, end time, and distance
    saccstlist = []
    saccetlist = []
    saccdistlist = []
    
    # get number of samples for mindur and maxdur (depending on sampfreq)
    mindur = int(mindur * 1000/sampfreq)
    maxdur = int(maxdur * 1000/sampfreq)
    
    # calculate distance from one pair of xy samples to the next pair (i.e., velocity)
    vtrace = np.sqrt(np.square(srs.smooth(np.diff(xtrace), winlen = vel_smooth)) + 
                     np.square(srs.smooth(np.diff(ytrace), winlen = vel_smooth)))
    
    # calculate raw threshold for current trial
    vt = np.nanmedian(np.absolute(vtrace - np.nanmedian(vtrace))) * msVthres
    
    ifrom = 0
    
    while ifrom < len(vtrace):
        
        # find first index where velocity exceeds threshold
        l = np.where(vtrace[ifrom:] > vt)[0]
        if len(l) == 0:
            break
        istart = l[0] + ifrom

        if ifrom == istart:
            break
        
        # find how many samples passed until velocity drops beneath threshold
        l = np.where(vtrace[istart:] < vt)[0]
        
        if len(l) == 0:
            # iend = len(vtrace)
            break
        else:
            iend = l[0] + istart
        
        # determine distance between start and end of saccade
        # use the median location 5 samples before and 5 samples after the saccade to calculate distance
        saccdist = pix2degree * (np.sqrt(np.square(np.nanmedian(xtrace[istart - 5:istart]) - np.nanmedian(xtrace[iend:iend + 5])) + 
                           np.square(np.nanmedian(ytrace[istart - 5:istart]) - np.nanmedian(ytrace[iend:iend + 5]))))
                
        # append this saccade if duration and distance is within margins
        if l[0] > mindur and l[0] < maxdur and saccdist < maxdist and saccdist > mindist:
            saccstlist.append(istart)
            saccetlist.append(iend)
            saccdistlist.append(saccdist)
            ifrom = iend + saccISI
        else:
            ifrom = iend
    
    return np.array(saccstlist, dtype = float), np.array(saccetlist, dtype = float), np.array(saccdistlist, dtype = float)

#%%
def microsaccades(dm, msVthres = 6, mindur = 9, maxdur = 50, 
                  mindist = .08, maxdist = 2, saccISI = 50, 
                  vel_smooth = 7, freq_smooth = 99, varname = "",
                  pix2degree = 1/34.6):

    """
    desc:
        find microsaccades for all trials and phases of an experiment and adds them to the dm
        
    arguments:
        dm: DataMatrix containing data from the experiment
        
    """
    
    # extract the phases of the experiment from the dm
    phases = [c.replace("xtrace_", "") for c in dm.column_names if c.startswith("xtrace_")]
    
    for phase in phases:
        
        # extract sampling frequency from time
        sampfreq = int(1000/(dm["ttrace_" + phase][0,1] - dm["ttrace_" + phase][0,0]))
        
        # create new columns start times, end times and distance
        dm[varname + "saccstlist_" + phase] = SeriesColumn(0)
        dm[varname + "saccetlist_" + phase] = SeriesColumn(0)
        dm[varname + "saccdistlist_" + phase] = SeriesColumn(0)
        
        # create new column for saccade frequency over time (list of zeros to start with)
        dm[varname + "saccfreq_" + phase] = SeriesColumn(depth = dm["xtrace_" + phase].depth)
        dm[varname + "saccfreq_" + phase] = [0] * dm[varname + "saccfreq_" + phase].depth
        
        # update max_depth depending on the maximum number of microsaccades we find in phases/trials
        max_depth = 0
        
        for i, row in enumerate(dm):

            # find microsaccades for each trial/phase, store start times, end times and distances
            saccstlist, saccetlist, saccdistlist = find_microsaccades(row["xtrace_" + phase], 
                                                                      row["ytrace_" + phase], 
                                                                      msVthres = msVthres, mindur = mindur, maxdur = maxdur, 
                                                                      mindist = mindist, maxdist = maxdist, saccISI = saccISI, 
                                                                      vel_smooth = vel_smooth, pix2degree = pix2degree, sampfreq = sampfreq)
            
            # update max depth if more saccades are sound than previously in this trial
            max_depth = max([max_depth, len(saccstlist)])
            
            if len(saccstlist) > dm[varname + "saccstlist_" + phase].depth:
                dm[varname + "saccstlist_" + phase].depth = len(saccstlist)
                dm[varname + "saccetlist_" + phase].depth = len(saccetlist)
                dm[varname + "saccdistlist_" + phase].depth = len(saccdistlist)
 
            # store lists in dm
            row[varname + "saccstlist_" + phase][:len(saccstlist)] = saccstlist
            row[varname + "saccetlist_" + phase][:len(saccetlist)] = saccetlist
            row[varname + "saccdistlist_" + phase][:len(saccdistlist)] = saccdistlist
            
            # create a trace with saccade frequency over time
            # set frequency to 1 at the onsets of saccades
            row[varname + "saccfreq_" + phase][list(map(int, saccstlist))] = 1
            # smooth signal
            row[varname + "saccfreq_" + phase] = srs.smooth(row[varname + "saccfreq_" + phase], freq_smooth) * sampfreq
            
         