CROSS_COMPILE ?= aarch64-elf-

CC=$(CROSS_COMPILE)gcc
ASM=$(CROSS_COMPILE)as
LD=$(CROSS_COMPILE)ld
OBJCOPY=$(CROSS_COMPILE)objcopy
DUMPELF=$(CROSS_COMPILE)objdump
CPP=$(CROSS_COMPILE)cpp
AR=$(CROSS_COMPILE)ar
CFLAGS += -march=armv8-a -mtune=cortex-a53  -mabi=ilp32 --sysroot=$(CURDIR)/sysroot -I $(CURDIR)/sysroot/include
ASFLAGS += -march=armv8-a -mtune=cortex-a53  -mabi=ilp32 --sysroot=$(CURDIR)/sysroot -I $(CURDIR)/sysroot/include
all:main.elf

clean:
	rm -rf *.elf *.o
main.elf:  main.o start.o
	$(CC) $(CFLAGS) -nostartfiles -T main.lds -Wl,-b=aarch64elf32,-Map=main.map,--build-id=none  -o $@ $^
	$(LD) -EL -X -maarch64elf32 --fix-cortex-a53-835769 --fix-cortex-a53-843419  -T main.lds -o main.ld.elf $^
