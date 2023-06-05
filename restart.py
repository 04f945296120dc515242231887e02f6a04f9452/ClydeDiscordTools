import os
import sys


def restart_bot():
    """
    Restart the Discord bot by calling the Python interpreter with the current command line arguments.
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)
