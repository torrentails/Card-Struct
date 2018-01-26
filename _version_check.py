#!/usr/bin/python3

from sys import exit
from sys import version_info as vi

from .Config import BASIC

min_major = BASIC.min_python_major
min_minor = BASIC.min_python_minor

if vi[0] < min_major or vi[1] < min_minor:
    print("%s only supports python language version %d.%d or higher." \
        " Please download the latest version of python." \
        % (BASIC.name, min_major, min_minor))
    exit(1)
