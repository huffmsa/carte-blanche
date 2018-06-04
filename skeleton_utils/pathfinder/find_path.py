'''
=================================================================
Utility for generating root path from any module
-----------------------------------------------------------------
'''
import os
import sys
from os import path

KEYFILE = 'README.md'


def find_path(keyfile=KEYFILE):
    hot_path = ''
    start_location = path.dirname(__file__)
    current_location = start_location

    root_toggle = False

    while root_toggle == False:
        files = os.listdir(current_location)

        if keyfile not in files:
            current_location = path.join(current_location, '..')

        else:
            hot_path = path.abspath(current_location)
            root_toggle = True

    return hot_path




if __name__ == '__main__':
    find_path()