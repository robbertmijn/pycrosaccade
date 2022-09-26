# pycrosaccade
Detect microsaccades

# Installation
Use pip install

`> pip install pycrosaccade`

# Usage

Use in combination with https://github.com/smathot/python-eyelinkparser/tree/master/eyelinkparser

## Preprocessing

``` { .python capture }
from pycrosaccade import microsaccades
from eyelinkparser import parse, defaulttraceprocessor

# Parse data as usual
dm = parse(
    traceprocessor=defaulttraceprocessor(
      blinkreconstruct=True, 
      downsample=None, 
      mode = "advanced"
    )
)
```

__Out:__

```
....................................................................................................................................
```

## Microsaccades

``` { .python capture}
# for each phase in the experiment, add 4 columns (saccetlist_phase, saccstlist_phase, saccfistlist_phase, saccfreq_phase)

microsaccades(dm)

print(dm.saccstlist_fixation)
```

__Out:__

```
col[[  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [2198.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 434.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [1280.   nan   nan   nan   nan   nan]
 [ 363.  618.  843.   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [1004.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  88.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 263.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 678. 1382.   nan   nan   nan   nan]
 [  87.   nan   nan   nan   nan   nan]
 [ 667.   nan   nan   nan   nan   nan]
 [1024.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 608.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [1228. 1995.   nan   nan   nan   nan]
 [ 301.   nan   nan   nan   nan   nan]
 [1030. 1193.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 728.   nan   nan   nan   nan   nan]
 [  93.  256.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  37.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [2132.   nan   nan   nan   nan   nan]
 [1719.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 190.  813. 2124.   nan   nan   nan]
 [  33.   nan   nan   nan   nan   nan]
 [ 415.  780.  898. 1933. 2357.   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 252.  434.  875. 1052.   nan   nan]
 [ 660. 1207. 2476.   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  21. 1487.   nan   nan   nan   nan]
 [ 207.  394.  625.   nan   nan   nan]
 [ 116.  549. 1231. 1378.   nan   nan]
 [1265. 1443.   nan   nan   nan   nan]
 [1395.   nan   nan   nan   nan   nan]
 [  97.  270.  686. 1182.   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 138.  337.  775. 2131.   nan   nan]
 [ 299.  722.  914. 2216.   nan   nan]
 [ 486. 1366.   nan   nan   nan   nan]
 [ 404.  549.   nan   nan   nan   nan]
 [ 615.   nan   nan   nan   nan   nan]
 [ 312.  617. 1387. 1861.   nan   nan]
 [ 163.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 863. 1019.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [ 104.   nan   nan   nan   nan   nan]
 [ 459.   nan   nan   nan   nan   nan]
 [ 268.  957. 1114.   nan   nan   nan]
 [ 348.  472.   nan   nan   nan   nan]
 [ 201.  351. 1048. 1842. 2485.   nan]
 [1038. 1907. 2132.   nan   nan   nan]
 [ 157.   nan   nan   nan   nan   nan]
 [ 625.  915. 1050.   nan   nan   nan]
 [ 262.  722. 1285. 1585.   nan   nan]
 [  50.  603. 1515. 1936. 2113.   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]
 [  68.  263. 1016. 1171. 1685. 2413.]
 [  nan   nan   nan   nan   nan   nan]
 [ 619.   nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan   nan]]
```

# Visualisation

``` { .python capture }
from datamatrix import plot
plot.trace(dm.saccfreq_fixation)
```


__Out:__

![alt text](https://github.com/robbertmijn/micSaccer/blob/main/plot.png?raw=true)

# Parameters

TODO (but see functions)