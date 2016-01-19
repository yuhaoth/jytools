
.ONESHELL:
all: .obj/a.o .obj/b.o .obj/c.o
	for i in $(^:%.o=%.d)
	do
		echo =============$$i=============
		cat $$i
	done
	
#.obj/c.o

.obj/a.o:md.c
	gcc -Wp,-MD,$(@:%.o=%.d) -c $< -o $@
.obj/b.o:md.c
	gcc -MD -c $< -o $@
.obj/c.o:md.c
	echo $@ $^
	gcc -M -MF$(@:%.o=%.d) -c $< -o $@
