#!/usr/bin/env python
import os,subprocess,sys,json
from jytools import path_clean 
run_exe=lambda exe,arg: subprocess.check_output(exe + ' ' + arg + ' 2>&1 ',shell=True)
def get_gcc_params(gcc_exe):
    full_version=[]
    for i in run_exe(gcc_exe,'-v').splitlines():
        if i.startswith("COLLECT_GCC=") or i.startswith("COLLECT_LTO_WRAPPER="):
            continue
        full_version.append(i)
    ret={
                'exe_file': [gcc_exe],
                'machine':run_exe(gcc_exe,'-dumpmachine').rstrip('\r\n'),
                'version':run_exe(gcc_exe,'-dumpversion').rstrip('\r\n'),
                'full_version': full_version
                
        }
    return hash('\n'.join(ret['full_version'])),ret 
def find_files(path,recursive=False,is_match=None):
    if is_match is None:
        is_match=lambda a: True
    elif callable(is_match) is False:
        raise Exception("Wrong is_match parameter")
    if recursive is True:
        for dirname,dirlist,filelist in os.walk(os.path.abspath(path)):
            for i in filelist:
                filename=os.path.join(dirname,i)
                if is_match(filename):
                    yield filename
    else:
        for i in os.listdir(path):
            filename= os.path.join(path,i)
            if is_match(filename):
                    yield filename
def find_all_gcc(env_path=True,path=['~/local']):
    if env_path is True:
        for i in path_clean.clean_path()[0]:
            for j in find_files(i,
                is_match=lambda a:a.endswith('gcc') and a.endswith('winegcc') is False):
                yield j
    for p in path:
        for i in find_files(os.path.expanduser(p),
            recursive=True,is_match=lambda a:a.endswith('gcc')):
            yield i
import json
def build_gcc_config(env_path=True,path=['~/local']):
    ret={}
    for i in find_all_gcc(env_path=env_path,path=path):
        hash_v,data=get_gcc_params(i)
        if hash_v not in ret:
            ret[hash_v]=data
        else:
            ret[hash_v]['exe_file'].extend(data['exe_file'])
    return ret


import json
config_dir=os.path.expanduser("~/.config/jytools/")  \
    if os.getenv("JY_CONFIG",None) is None else os.getenv("JY_CONFIG")
config_file=os.path.join(config_dir,'gcc.conf')
def makedirs(path):
    if os.path.exists(path) is False:
        os.makedirs(path)

def check_config(dis_rebuild=False):
    if os.path.exists(config_file) is False :
        if  dis_rebuild == True:
            return None
        makedirs(config_dir)
        return None
    return json.load(file(config_file))
        
gcc_config=check_config(dis_rebuild=True)
gcc_config=gcc_config if gcc_config is not None \
                else {"env_path":True,
                    "path":['~/local'],
                    "compilers": None}

cmd_table={}
get_cmd_function=lambda a : cmd_table[a]
def decorator_cmd(fn):
    def rebuild(argv):
        if gcc_config['compilers'] is None:
            gcc_config['compilers']=    \
                build_gcc_config(env_path=gcc_config['env_path'],
                    path=gcc_config['path'])
        return fn(argv)
    cmd_table[fn.__name__]=rebuild
    return rebuild
@decorator_cmd
def version(argv):
    compilers=gcc_config['compilers']
    out={}
    for i in compilers:
        compiler=compilers[i]
        gen_name=compiler['machine'] + '-gcc-' + compiler['version']
        value={'hash':[i],'exe_file':compiler['exe_file']}
        if gen_name not in out:
            out[gen_name]=value
        else:
            out[gen_name]['hash'].extend(value['hash'])
            out[gen_name]['exe_file'].extend(value['exe_file'])
    print json.dumps(out,indent=4)
    return 0
@decorator_cmd
def machine(argv):
    compilers=gcc_config['compilers']
    out={}
    for i in compilers:
        compiler=compilers[i]
        gen_name=compiler['machine'] 
        value={'hash':[i],'exe_file':[]}
        for j in compiler['exe_file']:
            value['exe_file'].append((compiler['version'],j,i))
        if gen_name not in out:
            out[gen_name]=value
        else:
            out[gen_name]['hash'].extend(value['hash'])
            out[gen_name]['exe_file'].extend(value['exe_file'])
    print json.dumps(out,indent=4)
    return 0
@decorator_cmd
def config(argv):
    gcc_config['compilers']=    \
                build_gcc_config(env_path=gcc_config['env_path'],
                    path=gcc_config['path'])
    json.dump(gcc_config,file(config_file,"w"),indent=2)
    return 0
@decorator_cmd
def get_cross_compiler(argv):
    machine=None
    version=None
    machine=argv[0]
    version=argv[1]
    for i in gcc_config['compilers']:
        compiler=gcc_config['compilers'][i]
        if compiler['machine'] == machine and compiler['version']==version:
            print compiler['exe_file'][0][:-3]
            return 0
    print "ERROR NO COMPILER Found for ", machine,version
    return 0

    
# Basic frame work 
def main(argv):
    if len(argv) == 1 or argv[1]=='list' or argv[1] not in cmd_table:
        print "Support commands:",'list',' '.join(cmd_table.keys())
        return 0
    func=get_cmd_function(argv[1])
    return func(argv[2:])
if __name__ == '__main__':
    
    import sys
    sys.exit(main(sys.argv))
    
    
    
