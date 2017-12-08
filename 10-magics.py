#   ~/.ipython/profile_default/startup/10-mystartup.py
# Based on https://goo.gl/RLn7Lq

from IPython.core.magic import register_line_cell_magic
from six import string_types

ip = get_ipython()


def _exec(cmd, line):
    """
    Wrapper to execute IPython command and, if requested, print the command
    """
    if isinstance(cmd, string_types):
        cmd = [cmd]
    for c in cmd:
        _print_cmd(c, line)
        ip.ex(c)


def _display(line):
    cmd = 'from IPython.display import display'
    _exec(cmd, line)


def _future_imports(line):
    cmd = 'from __future__ import (' \
          'absolute_import, division, print_function, unicode_literals)'
    _exec(cmd, line)


def _import_astropy(line):
    cmd = ['import astropy',
           'from astropy import constants, units as u',
           'from astropy.io import ascii, fits',
           'from astropy.table import Column, MaskedColumn, QTable, Table']
    _exec(cmd, line)


def _import_np(line):
    cmd = ['import numpy as np',
           'from numpy import random']
    _exec(cmd, line)


def _import_plt(line):
    cmd = 'from matplotlib import pyplot as plt'
    _exec(cmd, line)


def _update_rcParams(line):
    try:
        cmd = ['from plottools.plotutils import update_rcParams',
               'update_rcParams()']
        _exec(cmd, line)
    except ImportError:
        pass


def _print_cmd(cmd, line):
    if '-v' in line:
        # avoid quotation mark conflicts
        cmd = cmd.replace("'", "\'").replace('"', '\"')
        ip.ex('print("{0}")'.format(cmd))


@register_line_cell_magic
def import_all(line):
    _future_imports(line)
    _display(line)
    _import_astropy(line)
    _import_np(line)
    _import_plt(line)
    _update_rcParams(line)


@register_line_cell_magic
def astropy(line):
    _import_astropy(line)


@register_line_cell_magic
def future(line):
    _future_imports(line)


@register_line_cell_magic
def np(line):
    _import_np(line)


@register_line_cell_magic
def plt(line):
    _import_plt(line)


@register_line_cell_magic
def update_rcParams(line):
    _update_rcParams(line)


del astropy, future, import_all, np, plt, update_rcParams
