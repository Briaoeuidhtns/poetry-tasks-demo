__version__ = '0.1.0'
import sys
from subprocess import run

def task():
    _, cmd, *args = sys.argv
    if cmd == 'build':
        run(['echo', 'Building!'])
        run(['touch', 'built1'])
