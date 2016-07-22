
CFLAGS+=-fPIC

all: dymain st_main

dymain:libmean.so $(MAKEFILE_LIST)
	$(CC) -Wl,-rpath=\$$ORIGIN/../lib main.c -o $@ -L. -lmean
st_main:libmean.a  $(MAKEFILE_LIST)
	$(CC) -static main.c -o $@ -L. -lmean
libmean.a: calc_mean.o
	$(AR) rcs $@ $^
libmean.so :calc_mean.o
	$(CC) -shared -o $@ $^
