#!/usr/bin/env python
import os,sys

def clean_path(path,sep=os.path.pathsep):
    path=path.split(sep)
    new_path=[]
    for i in path:
        if i not in new_path:
            if os.path.exists(i):
                new_path.append(os.path.abspath(i))
    return new_path,[i for i in path if i not in new_path]

def main(argv):
    # FIXME:Fixed below with optparser later
    if len(argv) > 1 :
        if argv[1] in ('-l',):
            new_path,filter_out=clean_path(os.getenv('PATH'))
        elif argv[1] in ('-s',):
            new_path,filter_out=clean_path(argv[2])
        elif argv[1] in ('-e',):
            new_path,filter_out=clean_path(os.getenv(argv[2]))

        print 'new_path',new_path
        print 'filter_out',filter_out
        return 0
    else:
        s=':'.join(clean_path(os.getenv['PATH'])[0])
        print 'PATH='+s
        return 0
if __name__ == '__main__':
    sys.exit(main(sys.argv))
