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

## Microsaccades

``` { .python capture}
# for each phase in the experiment, add 4 columns (saccetlist_phase, saccstlist_phase, saccfistlist_phase, saccfreq_phase)

microsaccades(dm)

print(dm.saccstlist_fixation)
```

# Visualisation

``` { .python capture }
from datamatrix import plot
plot.trace(dm.saccfreq_fixation)
```


# Parameters

TODO (but see functions)

# References

- Engbert, R., & Kliegl, R. (2003). Microsaccades uncover the orientation of covert attention. Vision Research, 43(9), 1035–1045. https://doi.org/10.1016/S0042-6989(03)00084-1
- Liu, B., Nobre, A. C., & Ede, F. van. (2021). Functional but not obligatory link between microsaccades and neural modulation by covert spatial attention. bioRxiv. https://doi.org/10.1101/2021.11.10.468033
