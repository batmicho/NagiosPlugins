#!/usr/bin/python

import os, sys

cpu=os.popen("mpstat -P ON|grep all").readline().split()

idel=cpu[-1]

if idel<=20:
        print'Going Critical 80% Cpu power is used! \n',cpu
        sys.exit(2)
elif idel<=50:
        print 'Warning smtg. is using more than 50% Cpu power \n',cpu
        sys.exit(1)
elif idel>=49:
        print 'We all good with the CPU usage \n', cpu

