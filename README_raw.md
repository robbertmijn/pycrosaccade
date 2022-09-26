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