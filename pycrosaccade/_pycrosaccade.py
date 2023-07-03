#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extract microsaccades

@author: robbertmijn
"""
#%%
from datamatrix import (
    series as srs,
    SeriesColumn,
    plot
    )
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('default')

#%%
def _round_to_odd(k):
    return 2 * int(k/2) + 1

#%%
def _find_microsaccades(xtrace, ytrace, msVthres=6, mindur=9, maxdur=50,
                  mindist=.08, maxdist=2, saccISI=50, 
                  vel_smooth=7, pix2degree=1/34.6, sampfreq=1000):
    
    """
    desc:
        Get microsaccades for a trace of x and y coordinates for a single trial
        Returns three lists with respectively first sample, last sample and the distance travelled during the microsaccade.

    NOTE: default settings need updating!
        
    arguments:
        xtrace: SeriesColumn with x coordinates
        ytrace: SeriesColumn with y coordinates
        msVthres: Velocity threshold of eye movement to mark a microsaccade. Its unit is the number of median absoute deviations the velocity must deviate from the median velocity for each trial.
        mindur: minumum duration for the velocity to be above threshold for it to be considered a saccade
        maxdur: saccades longer than maxdur are not considered
        mindist: minimum distance the gaze has to travel
        maxdist: maximum distance the gaze has to travel
        saccISI: At least this many samples must pass before a new microsaccade is considered
        vel_smooth: How many ms to smooth over gaze velocity
        pix2degree: depending on distance to screen and resolution, how many pixels make up one degree visual angle
        sampfreq: sampling frequency
        
    """

    # initiate lists for start time, end time, and distance
    saccstlist = []
    saccetlist = []
    saccdistlist = []
    saccpvlist = []
    
    # get number of samples for mindur and maxdur (depending on sampfreq)
    mindur = max(1, int(mindur * sampfreq/1000))
    maxdur = max(1, int(maxdur * sampfreq/1000))
    vel_smooth = max(1, _round_to_odd(vel_smooth * sampfreq/1000))
    dist_margin = max(1, int(5 * sampfreq/1000))
    
    # calculate distance from one pair of xy samples to the next pair. Smooth it over 7 samples (default).
    vtrace = srs.smooth(np.sqrt(np.square(np.diff(xtrace)) + np.square(np.diff(ytrace))), winlen = vel_smooth)
    
    # calculate threshold for current trial
    vt = np.nanmedian(vtrace) * msVthres
    
    # find microsaccades in the velocity trace
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
        
        # determine distance travelled between start and end of saccade
        saccdist = pix2degree * vtrace[istart:iend].sum()
        
        # determine peak velocity between start and end of saccade
        saccpv = pix2degree * np.nanmax(vtrace[istart:iend])
        
        # append this saccade if duration and distance is within margins
        if l[0] > mindur and l[0] < maxdur and saccdist < maxdist and saccdist > mindist:
            saccstlist.append(istart)
            saccetlist.append(iend)
            saccdistlist.append(saccdist)
            saccpvlist.append(saccpv)
            ifrom = iend + saccISI
        else:
            ifrom = iend
    
    return np.array(saccstlist, dtype = float), np.array(saccetlist, dtype = float), np.array(saccdistlist, dtype = float), np.array(saccpvlist, dtype=float)

#%%
def microsaccades(dm, msVthres=6, mindur=9, maxdur=50, 
                  mindist=.08, maxdist=2, saccISI=50, 
                  vel_smooth=7, freq_smooth=100, varname="",
                  pix2degree=1/34.6, sampfreq=None):

    """
    desc:
        find microsaccades for all trials and phases of an experiment and adds them to the dm
        
    arguments:
        dm: DataMatrix containing data from the experiment
        
    """
        
    # extract the phases of the experiment from the dm
    phases = [c.replace("xtrace_", "") for c in dm.column_names if c.startswith("xtrace_")]
    
    for phase in phases:
        
        if sampfreq is None:
            # extract sampling frequency from time
            sampfreq = int(1000/(dm["ttrace_" + phase][0,1] - dm["ttrace_" + phase][0,0]))
        else:
            pass
        
        freq_smooth_samps = max(1, _round_to_odd(freq_smooth * sampfreq/1000))

        # create new columns start times, end times and distance
        dm[varname + "saccstlist_" + phase] = SeriesColumn(0)
        dm[varname + "saccetlist_" + phase] = SeriesColumn(0)
        dm[varname + "saccdistlist_" + phase] = SeriesColumn(0)
        dm[varname + "saccpvlist_" + phase] = SeriesColumn(0)
        
        # create new column for saccade frequency over time (list of zeros to start with)
        dm[varname + "saccfreq_" + phase] = SeriesColumn(depth = dm["xtrace_" + phase].depth)
        dm[varname + "saccfreq_" + phase] = [0] * dm[varname + "saccfreq_" + phase].depth
        
        # update max_depth depending on the maximum number of microsaccades we find in phases/trials
        max_depth = 0
        
        for i, row in enumerate(dm):

            # find microsaccades for each trial/phase, store start times, end times and distances
            saccstlist, saccetlist, saccdistlist, saccpvlist = _find_microsaccades(row["xtrace_" + phase], 
                                                                      row["ytrace_" + phase], 
                                                                      msVthres=msVthres, mindur=mindur, maxdur=maxdur, 
                                                                      mindist=mindist, maxdist=maxdist, saccISI=saccISI, 
                                                                      vel_smooth=vel_smooth, pix2degree=pix2degree, sampfreq=sampfreq)
            
            # update max depth if more saccades are found than previously in this trial
            max_depth = max([max_depth, len(saccstlist)])
            
            if len(saccstlist) > dm[varname + "saccstlist_" + phase].depth:
                dm[varname + "saccstlist_" + phase].depth = len(saccstlist)
                dm[varname + "saccetlist_" + phase].depth = len(saccetlist)
                dm[varname + "saccdistlist_" + phase].depth = len(saccdistlist)
                dm[varname + "saccpvlist_" + phase].depth = len(saccpvlist)
                
            # store lists in dm
            row[varname + "saccstlist_" + phase][:len(saccstlist)] = saccstlist
            row[varname + "saccetlist_" + phase][:len(saccetlist)] = saccetlist
            row[varname + "saccdistlist_" + phase][:len(saccdistlist)] = saccdistlist
            row[varname + "saccpvlist_" + phase][:len(saccpvlist)] = saccpvlist            
            
            # create a trace with saccade frequency over time
            # set frequency to 1 at the onsets of saccades
            row[varname + "saccfreq_" + phase][list(map(int, saccstlist))] = 1
            
            # smooth signal
            row[varname + "saccfreq_" + phase] = srs.smooth(row[varname + "saccfreq_" + phase], freq_smooth_samps) * sampfreq
        
def plot_dist_dur(dm, phase, varname=""):
    
    sampfreq = int(1000/(dm["ttrace_" + phase][0,1] - dm["ttrace_" + phase][0,0]))

    dm[varname + "saccdurlist_" + phase] = dm[varname + "saccetlist_" + phase] - dm[varname + "saccstlist_" + phase]
    dm_distdur = dm[varname + "saccdistlist_" + phase, varname + "saccdurlist_" + phase]
    dm_distdur = srs.flatten(dm_distdur)
    dm_distdur = dm_distdur["saccdistlist_" + phase] != np.nan
    
    dm_pvdist = dm[varname + "saccpvlist_" + phase, varname + "saccdistlist_" + phase]
    dm_pvdist = srs.flatten(dm_pvdist)
    dm_pvdist = dm_pvdist[varname + "saccdistlist_" + phase] != np.nan
    
    fig, axs = plt.subplots(2, 2, constrained_layout=True)
    fig.suptitle(f"{len(dm_distdur)/len(dm)} saccades per phase")

    axs[0,0].scatter(dm_distdur[varname + "saccdurlist_" + phase], dm_distdur[varname + "saccdistlist_" + phase])
    axs[0,0].set_xlabel("Duration (ms)")
    axs[0,0].set_ylabel("Distance (px)")
    
    axs[0,1].scatter(dm_pvdist[varname + "saccdistlist_" + phase], dm_pvdist[varname + "saccpvlist_" + phase])
    axs[0,1].title("{} times threshold, {} saccades".format(varname, len(dm_pvdist)))
    axs[0,1].set_xlabel("Distance (degree)")
    axs[0,1].set_xlabel("Peak velocity (degree/s)")
    
    saccfreq = dm[varname + "saccfreq_" + phase].mean()
    axs[1,0].plot(saccfreq)
    axs[1,0].set_xlabel("Time (ms)")
    axs[1,0].set_ylabel("Microsaccades (Hz)")
