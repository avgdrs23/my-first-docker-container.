#!/usr/bin/python3

import time
import sys

i=0
while True:
   print(f"Docker CONTAINER IS WORKING!!! {i}")
   time.sleep(2)
   sys.stdout.flush()
   i=i+1
