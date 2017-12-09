# ipystartup
Custom IPython startup configuration files

Running
```
python setup.py [profile]
```
will copy the files below to `~/.ipython/profile_<profile>/startup/`, which means all the definitions in them will be available when starting an `IPython` session, be it in the terminal or a `Jupyter` notebook. If `profile` is not specified, the default profile will be updated.

### Notifications

`00-notify.py` enables notifications per https://github.com/ShopRunner/jupyter-notify

### `magic` commands

`10-magics.py` is based on [this repo](https://github.com/saimn/dotfiles/blob/master/ipython/profile_default/startup/10-mystartup.py) and contains a set of custom magic commands:

```
astropy
display
future
np
plotting
```

in addition to a wrapper that executes all of them, `import_all`. In order to know exactly what each does, call any of them with the `-v` flag, e.g.,

```
In [1]: %np -v
import numpy as np
from numpy import random
```

