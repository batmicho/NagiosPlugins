#!/usr/bin/python

import os, sys, multiprocessing

ncpu=multiprocessing.cpu_count()
avgl=os.getloadavg()
avglall=2.5*ncpu <= avgl[0] or 2*ncpu <= avgl[1] or 1.5*ncpu <= avgl[2]

if  avglall is True:
          print "Critical" , avgl,  "Inspect the CPU Load!"
          sys.exit(2)
else: 
          print "Errting OK", avgl
          sys.exit(0)

