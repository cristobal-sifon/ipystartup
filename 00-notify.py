import jupyternotify

ip = get_ipython()
ip.register_magics(jupyternotify.JupyterNotifyMagics)
