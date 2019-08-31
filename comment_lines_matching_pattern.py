##Comment lines matching a pattern

import codecs
import csv
import re
import sys
import os
import glob
import gzip
import json
import string
import numpy as np
from sqlalchemy import Table, Column, Float, Integer, String, MetaData, ForeignKey
import optparse

def comment_lines_matching_pattern(infile,pattern):
    with open(infile,'r+') as f:
        get_all = f.readlines()
    f.close()

    with open(infile,'w') as f:
        for lines in get_all:
            if pattern in lines:
                lines = "##" + lines
                f.write(lines)
            else:
                f.write(lines)

    f.close()


comment_lines_matching_pattern($FILE-NAME,PATTERN)
