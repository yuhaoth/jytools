
STDERR_CODE=$(abspath ../../3rd-party/stderred)
LD_PRELOAD_32=$(STDERR_CODE)/lib/libstderred.so
LD_PRELOAD_64=$(STDERR_CODE)/lib64/libstderred.so
#LD_PRELOAD=$(LD_PRELOAD_32) $(LD_PRELOAD_64)
LD_PRELOAD=libstderred.so
LD_LIBRARY_PATH=$(STDERR_CODE)/lib/:$(STDERR_CODE)/lib64/
$(warning $(LD_PRELOAD))
all:test_32 test_64

test_32: $(LD_PRELOAD_32) $(LD_PRELOAD_64)
	gcc -m32 -DBUILD_TARGET="\"x86\"" test.c -o prog_32.out
	LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) LD_PRELOAD="$(LD_PRELOAD)" ./prog_32.out
test_64:$(LD_PRELOAD_64) $(LD_PRELOAD_32)
	gcc -m64 -DBUILD_TARGET="\"x86_64\"" test.c -o prog_64.out
	LD_LIBRARY_PATH=$(LD_LIBRARY_PATH) LD_PRELOAD="$(LD_PRELOAD)" ./prog_64.out
$(LD_PRELOAD_32):
	make -C $(STDERR_CODE) 32
$(LD_PRELOAD_64):
	make -C $(STDERR_CODE) 64
install: install-i386-linux-gnu install-x86_64-linux-gnu

install-i386-linux-gnu : test_32
	@mkdir -p $(HOME)/lib/$(@:install-%=%)
	@cp $(LD_PRELOAD_32) $(HOME)/lib/$(@:install-%=%)
install-x86_64-linux-gnu : test_64
	@mkdir -p $(HOME)/lib/$(@:install-%=%)
	@cp $(LD_PRELOAD_64) $(HOME)/lib/$(@:install-%=%)

