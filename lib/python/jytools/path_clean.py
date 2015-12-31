#!/usr/bin/env python
import os,sys

def clean_path():
    path=os.getenv("PATH").split(':')
    new_path=[]
    for i in path:
        if i not in new_path:
            if os.path.exists(i):
                new_path.append(i)
    return new_path,[i for i in path if i not in new_path]

def main(argv):
    # FIXME:Fixed below with optparser later
    if len(argv) > 0 and argv[1] in ('-l',):
        new_path,filter_out=clean_path()
        print 'new_path',new_path
        print 'filter_out',filter_out
        return 0
    else:
        s=':'.join(clean_path()[0])
        print 'PATH='+s
        return 0
if __name__ == '__main__':
    sys.exit(main(sys.argv))
