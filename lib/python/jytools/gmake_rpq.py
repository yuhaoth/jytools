#!/usr/bin/env python
import os,subprocess
def call_command(cmd,ignore_ret=[0]):
    proc=subprocess.Popen(cmd,shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
    while proc.poll() is None:
        line=proc.stdout.readline()
        if line == '':
            break
        yield line.rstrip('\r\n')
    if proc.wait() not in ignore_ret:
        raise Exception("child process return Error " + str(proc.returncode))
    lines=proc.stdout.readlines()
    for line in lines:
        yield line.rstrip('\r\n')
    if proc.returncode not in ignore_ret:
        raise Exception("child process return Error " + str(proc.returncode))
    
def main(argv):
    for i in call_command("make -rspq",ignore_ret=[0,1,2]):
        print i
    return 0
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
