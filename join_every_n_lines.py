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

def join_every_n_lines(infile,outfile,number):
    out = open(outfile,'w')
    i = 1
    str1 = ""
    with open(infile,'r') as f:
        for lines in f:
            lines = lines.replace(';','')
            if i >= number:
                i = 1
                print(str1)
                out.write(str1)
                out.write("\n")
                str1 = " "
                str1 += lines.strip()
                i = i + 1
            else:
                str1 += " " + lines.strip()
                i = i + 1
    f.close()
    out.close()


join_every_n_lines($INPUT-FILE,$OUTPUT-FILE,NUMBER-OF-LINES)
eg. join_every_n_lines("git.txt","git_new.txt",8)
