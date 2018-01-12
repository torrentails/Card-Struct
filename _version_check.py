#!/usr/bin/python3

from sys import exit
from sys import version_info as vi

from .config import BASIC

if vi[0] < BASIC.min_major_version or vi[1] < BASIC.min_minor_version:
    print("%s only supports python language version %d.%d or higher." \
        " Please download the latest version of python." \
        % (BASIC.name, BASIC.min_major_version, BASIC.min_minor_version))
    exit(1)
