from __future__ import absolute_import, division, print_function

import argparse
from glob import glob
import os
import shutil

"""
Copy files from this repository to the IPython configuration directory
"""

# determine to which IPython profile does this setup correspond
parser = argparse.ArgumentParser()
parser.add_argument(
    'profile', nargs='?', default='default',
    help='IPython profile to which these settings will be applied')
parser.add_argument(
    '-n', dest='notify', action='store_false',
    help='Do not activate jupyter-notify' \
         ' (https://github.com/ShopRunner/jupyter-notify)')
args = parser.parse_args()

path = os.path.join(
    os.environ['HOME'], '.ipython', 'profile_{0}'.format(args.profile))
destination = os.path.join(path, 'startup')
if not os.path.isdir(destination):
    default_path = os.path.join(
        os.path.split(path)[0], 'profile_default')
    shutil.copytree(default_path, path)

# copy startup files to the IPython profile directory
pyfiles = glob('*.py')
for f in pyfiles:
    if f == 'setup.py':
        continue
    shutil.copy(f, destination)

# update IPython startup configuration file
# under construction - doesn't do anything for now
"""
if args.notify:
    head = 'c.InteractiveShellApp.exec_lines = ['
    cmds = ['import jupyternotify',
            'ip = get_ipython()',
            'ip.register_magics(jupyternotify.JupyterNotifyMagics)']
    config_file = os.path.join(path, 'ipython_config.py')
    config = open(config_file).readlines()
    in_exec_lines = False
    for line in config:
        if line.startswith(head):
            in_exec_lines = True
        if in_exec_lines and line.startswith(']'):
            in_exec_lines = False
            break
""" 



