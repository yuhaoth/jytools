#!/usr/bin/env python
import subprocess,sys

def call(args):
    p = subprocess.Popen(
        args,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        shell=False)
    while p.poll() is None:
        yield p.stderr.readline()
    l=None
    while l != b'':
        l=p.stderr.readline()
        yield l

for i in call(['./child.py']):
    print >>sys.stderr,repr(i)
