##FIND MEDIAN/MODE/MEAN BY COMBINING NEW LIST
import os
import sys
import numpy as np
import csv

def findMedianSortedArrays (nums1,nums2):
        joined_list = nums1 + nums2
        joined_list.sort()
        length = len(joined_list)
        if length % 2 == 0:
                middle = int(length/2)
                sum = joined_list[middle] + joined_list[middle + 1]
                median = float(sum/2)
        else:
                middle = int((length/2) + 1)
                median = float(joined_list[middle])
        return median
 
 def findMeanSortedArrays (nums1,nums2):
        joined_list = nums1 + nums2
        joined_list.sort()
        length = len(joined_list)
        total = 0;
        for i in range(length):
          total = total + joined_list[i]
        mean = total/length
        return mean
        
def findModeSortedArrays (nums1,nums2):
        joined_list = nums1 + nums2
        joined_list.sort()
        mode = {}
        min = 0;
        length = len(joined_list)
        for i in range(length):
           if joined_list[i] not in mode:
              mode[joined_list[i]] = 1
           else:
              mode[joined_list[i]] += 1
        for key,value in mode.items():
          if value > min:
            mode_val = key
            min = value
          else:
            continue
      
        return mode_val


num1 = [1,2,3,4]
num2 = [5,6,7,8]
median = findMedianSortedArrays(num1,num2)
mean = findMeanSortedArrays(num1,num2)
mode = findModeSortedArrays(num1,num2)
print("the median is: " + str(median))
print("the mean is: " + str(mean))
print("the mode is: " + str(mode))
