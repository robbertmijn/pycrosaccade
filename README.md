# pycrosaccade
Detect microsaccades

# Installation
Use pip install

`> pip install pycrosaccade`

# Usage

Use in combination with https://github.com/smathot/python-eyelinkparser/tree/master/eyelinkparser

## Preprocessing

``` { .python capture }
from pycrosaccade import microsaccades, ms_diagnostics
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
data/sub_1.asc............................................data/sub_2.asc............................................data/sub_3.asc............................................
```

## Microsaccades

For each phase in the experiment, add 5 columns (`saccetlist_phase`, `saccstlist_phase`, `saccdurlist_phase`, `saccdistlist_phase`, `saccfreq_phase`)

``` { .python capture}
microsaccades(dm)

print(dm.saccstlist_fixation)
```

__Out:__

```
Calculating microsaccades in phase "baseline"
Calculating microsaccades in phase "feedback"
Calculating microsaccades in phase "fixation"
Calculating microsaccades in phase "problem"
Calculating microsaccades in phase "response"
col[[  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [1101.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 487.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 399.  590.   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 613.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [1378.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [1036.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 194.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 785.  898. 1056. 1191. 2360.]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 884. 1068.   nan   nan   nan]
 [ 663.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 209.   nan   nan   nan   nan]
 [1237.   nan   nan   nan   nan]
 [1268.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 275.   nan   nan   nan   nan]
 [1066. 1552.   nan   nan   nan]
 [ 143.  779.   nan   nan   nan]
 [ 705.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 569.  792. 1396.   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  16.   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  91.  609.  738. 1633. 2209.]
 [ 385.   nan   nan   nan   nan]
 [1558.   nan   nan   nan   nan]
 [ 474.  715.   nan   nan   nan]
 [ 354.  926.   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 629. 1065.   nan   nan   nan]
 [1291. 1590.   nan   nan   nan]
 [  55.  608.  862. 1088. 1940.]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [ 478. 1020. 1177. 2420.   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]
 [  nan   nan   nan   nan   nan]]
```

# Visualisation

``` { .python capture }
from matplotlib import pyplot as plt
fig, ax = plt.subplots()
ax.plot(dm.saccfreq_fixation.mean)
fig.savefig('plot.png')
```

__Out:__

```

```

![alt text](https://github.com/robbertmijn/micSaccer/blob/main/plot.png?raw=true)

To compare the results with different parameters, use `ms_diagnostics`

``` { .python capture }
microsaccades(dm, varname='default')
microsaccades(dm, varname='thres3', msVthres=3)
```

__Out:__

```
Calculating microsaccades in phase "baseline"
Calculating microsaccades in phase "feedback"
Calculating microsaccades in phase "fixation"
Calculating microsaccades in phase "problem"
Calculating microsaccades in phase "response"
Calculating microsaccades in phase "baseline"
Calculating microsaccades in phase "feedback"
Calculating microsaccades in phase "fixation"
Calculating microsaccades in phase "problem"
Calculating microsaccades in phase "response"
```

``` { .python capture }
fig, axs = ms_diagnostics(dm, phase='fixation', varname='default')
fig.savefig('defaults.png')
fig, axs = ms_diagnostics(dm, phase='fixation', varname='thres3')
fig.savefig('thres3.png')
```

__Out:__

```

```

![alt text](https://github.com/robbertmijn/micSaccer/blob/main/defaults.png?raw=true)
![alt text](https://github.com/robbertmijn/micSaccer/blob/main/thres3.png?raw=true)

# Parameters

TODO (but see functions)

# References

- Engbert, R., & Kliegl, R. (2003). Microsaccades uncover the orientation of covert attention. Vision Research, 43(9), 1035–1045. https://doi.org/10.1016/S0042-6989(03)00084-1
- Liu, B., Nobre, A. C., & Ede, F. van. (2021). Functional but not obligatory link between microsaccades and neural modulation by covert spatial attention. bioRxiv. https://doi.org/10.1101/2021.11.10.468033
