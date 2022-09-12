# micSaccer
Detect microsaccades

# Installation
Clone repo into your preprocessing directory

`> git clone https://github.com/robbertmijn/micSaccer`

# Usage

Use in combination with https://github.com/smathot/python-eyelinkparser/tree/master/eyelinkparser

```
from micSaccer.microsaccades import microsaccades as microsaccades
from eyelinkparser import parse, defaulttraceprocessor

# Parse data as usual
dm = parse(
    maxtracelen = 3000,
    folder=folder,
    traceprocessor=defaulttraceprocessor(
      blinkreconstruct=True, 
      downsample=None, 
      mode = "advanced"
    )
)

# for each phase in the experiment, add 4 columns (saccetlist_phase, saccstlist_phase, saccfistlist_phase, saccfreq_phase)
microsaccades(dm)
```

# Parameters

TODO (but see functions)