# emails-extract.py
import argparse

import os
import sys
from tkinter.filedialog import askopenfile

argparser = argparse.ArgumentParser(description='Extract structured data from Mac OS emails (plaintext exports & direct emlx file parsing)')
## tbd
argparser.add_argument('-e',
                       metavar='emlx',
                       type=str,
                       help='run in mode: direct emlx file parsing')
                       


args = argparser.parse_args()


pass