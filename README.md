# ipystartup
Custom IPython startup configuration files

The file `10-magics.py` contains a set of custom magic commands:

```
astropy
display
future
np
plt
update_rcParams
```

in addition to a wrapper that executes all of them, `import_all`. In order to know exactly what each does, call any of them with the `-v` flag, e.g.,

```
In [1]: %np -v
import numpy as np
from numpy import random
```

The magic command `update_rcParams` requires [`plottools`](https://github.com/cristobal-sifon/plottools), and will be ignored if the package is not present.
