file_list:=$(abspath ../a.c vpath/a.c vpath2/a.c)
#makefile does not include relative path function
all:
	echo file_list=$(file_list)
	echo realpath=$(realpath $(abspath ../a.c))
