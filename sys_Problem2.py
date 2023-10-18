#!/usr/bin/env python3
import sys

#test4 tested first for 50 then for 75 to test divisiblility
count = int(sys.argv[1])
if count > 49:
  message = "True is greater than 49"
  print (count, message)
if count % 2 == 0:
  message = "Number is divisible by 2"
  print (count, message)
if count % 3 == 0:
  message = "Number is divisible by 3"
  print (count, message)
