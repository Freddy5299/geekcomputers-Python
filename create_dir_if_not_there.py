# Script Name   : create_dir_if_not_there.py
# Author        : Craig Richards
# Created       : 09th January 2012
# Last Modified : 22nd October 2015
# Version       : 1.0.1
# Modifications : Added exceptions
#               : 1.0.1 Tidy up comments and syntax
#
# Description   : Checks to see if a directory exists in the users home directory, if not then create it

import os  # Import the OS module
import argparse

MESSAGE = 'The directory already exists.'
TESTDIR = '20200429'
def creat(dir_name):
    try:
        home = os.path.expanduser("~")  # Set the variable home by expanding the user's set home directory
        print(home)  # Print the location

        if not os.path.exists(os.path.join(home, dir_name)):  # os.path.join() for making a full path safely
            os.makedirs(os.path.join(home, dir_name))  # If not create the directory, inside their home directory
        else:
            print(MESSAGE)
    except Exception as e:
        print(e)

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1,
                        help='the directory where to change extension')
    return parser


if __name__ == '__main__':
    parser = get_parser()
    dict = vars(parser.parse_args())
    dir = dict['work_dir'][0]
    creat(_)