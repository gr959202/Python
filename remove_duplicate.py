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

def remove_duplicate_line(infile,outfile):
    lines_seen = set()
    out = open(outfile,'w')
    with open(infile,'r') as f:
        for lines in f:
            if lines not in lines_seen:
                out.write(lines)
                lines_seen.add(lines)
            else:
                continue
    f.close()
    out.close()

remove_duplicate_line($INPUT-FILE,$OUTPUT-FILE)
