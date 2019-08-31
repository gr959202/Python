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

def print_bet_lines(infile,pat1,pat2):
    canPrintLines = False
    i = 0
    with open(infile,'r') as f:
        for lines in f:
            if pat1 in lines:
                canPrintLines = True
                i = i + 1
            elif i >= 1 and pat2 in lines:
                canPrintLines = False
                break
            elif i >= 1 and pat2 not in lines:
                canPrintLines = True
            else:
                continue
            if canPrintLines:
                print(lines)
    f.close()

print_bet_lines($FILE-NAME,START-PT,END-PT)
