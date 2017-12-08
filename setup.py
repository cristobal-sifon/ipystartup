from __future__ import absolute_import, division, print_function

import argparse
from glob import glob
import os
import shutil

"""
Copy files from 
"""

# determine to which IPython profile does this setup correspond
parser = argparse.ArgumentParser()
parser.add_argument(
    'profile', nargs='?', default='default',
    help='IPython profile to which these settings will be applied')
args = parser.parse_args()
dest = os.path.join(
    os.environ['HOME'], '.ipython', 'profile_{0}'.format(args.profile), 'startup')

# copy startup files to the IPython profile directory
pyfiles = glob('*.py')
for f in pyfiles:
    if f == 'setup.py':
        continue
    shutil.copy(f, dest)
