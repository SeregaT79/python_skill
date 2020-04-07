#  -*- coding: utf-8 -*-
import sys
import platform

info = 'OS info - {}\nPython version - {}\n{}'.format(
    platform.uname(), sys.version, platform.architecture())


with open('os_info.txt', 'w') as ff:
    ff.write(info)