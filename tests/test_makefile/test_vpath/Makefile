
all:
	echo $^
vpath t1/%.o:%.c vpath1:vpath2
vpath t2/%.o:%.c vpath2:vpath1
all:t1/test.o

all:t2/test1.o
vpath %.c
t1/%.o:%.c
	echo $@ $^
t2/%.o:%.c
	echo $@ $^
