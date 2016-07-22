#!/usr/bin/env python
import sys
for i in range(0,1000):
    if (i%2) == 0:
        print >>sys.stdout,"This is stdout " + str(i)
    else:
        print >>sys.stderr,"This is stderr " + str(i)
