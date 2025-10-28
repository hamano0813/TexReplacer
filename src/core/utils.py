import os
import sys


def restart():
    exe = sys.executable
    argv = [exe] + sys.argv
    os.execv(exe, argv)
