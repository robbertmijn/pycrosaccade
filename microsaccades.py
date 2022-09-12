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
def find_microsaccades(xtrace, ytrace, msVthres = 6, mindur = 3, maxdur = 150, 
                  mindist = .1, maxdist = 100, saccISI = 50, 
                  smooth_winlen = 7):

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
        mindist: minimum distance the gaze has to travel (TODO: currently pixels, should transform to degrees visual angle)
        maxdist: maximum distance the gaze has to travel (TODO: currently pixels, should transform to degrees visual angle) 
        saccISI: At least this many samples must pass before a new microsaccade is considered
        smooth_winlen: number of samples taken together to form moving average
        
    """

    # initiate lists for start time, end time, and distance
    saccstlist = []
    saccetlist = []
    saccdistlist = []
    
    # calculate distance from one pair of xy samples to the next pair (i.e., velocity)
    vtrace = np.sqrt(np.square(srs.smooth(np.diff(xtrace), winlen = smooth_winlen)) + 
                     np.square(srs.smooth(np.diff(ytrace), winlen = smooth_winlen)))
    
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
        saccdist = np.sqrt(np.square(xtrace[istart] - xtrace[iend]) + 
                           np.square(ytrace[istart] - ytrace[iend]))
        
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
def microsaccades(dm, msVthres = 6, mindur = 3, maxdur = 150, 
                  mindist = .1, maxdist = 100, saccISI = 50, 
                  smooth_winlen = 7):

    """
    desc:
        find microsaccades for all trials and phases of an experiment and adds them to the dm
        
    arguments:
        dm: DataMatrix containing data from the experiment
        
    """
    
    # extract the phases of the experiment from the dm
    phases = [c.replace("xtrace_", "") for c in dm.column_names if c.startswith("xtrace_")]
    
    for phase in phases:
        
        # create new columns for each phase
        dm["saccstlist_" + phase] = SeriesColumn(0)
        dm["saccetlist_" + phase] = SeriesColumn(0)
        dm["saccdistlist_" + phase] = SeriesColumn(0)
        dm["saccfreq_" + phase] = SeriesColumn(depth = dm["xtrace_" + phase].depth)
        dm["saccfreq_" + phase] = [0] * dm["saccfreq_" + phase].depth
        
        # update max_depth depending on the maximum number of microsaccades we find in phases/trials
        max_depth = 0
        
        for i, row in enumerate(dm):

            # find microsaccades for each trial/phase
            saccstlist, saccetlist, saccdistlist = find_microsaccades(row["xtrace_" + phase], 
                                                                      row["ytrace_" + phase], 
                                                                      msVthres = msVthres, mindur = mindur, maxdur = maxdur, 
                                                                      mindist = mindist, maxdist = maxdist, saccISI = saccISI, 
                                                                      smooth_winlen = smooth_winlen)
            max_depth = max([max_depth, len(saccstlist)])
            if len(saccstlist) > dm["saccstlist_" + phase].depth:
                dm["saccstlist_" + phase].depth = len(saccstlist)
                dm["saccetlist_" + phase].depth = len(saccetlist)
                dm["saccdistlist_" + phase].depth = len(saccdistlist)
 
            row["saccstlist_" + phase][:len(saccstlist)] = saccstlist
            row["saccetlist_" + phase][:len(saccetlist)] = saccetlist
            row["saccdistlist_" + phase][:len(saccdistlist)] = saccdistlist
            
            sacclist = saccstlist + (saccetlist - saccstlist)
            row["saccfreq_" + phase][list(map(int, sacclist))] = 1
            row["saccfreq_" + phase] = srs.smooth(row["saccfreq_" + phase], 99)
            
         