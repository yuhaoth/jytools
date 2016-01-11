
define __test_vpath
$(warning $1 $2)
vpath $(1) $(2)
endef
__test_vpath =vpath $1 $2
$(foreach i, vpath2 vpath , \
$(eval $(call __test_vpath,%.c,$(i))) \
)
#~ vpath %.c vpath2:vpath
#~ vpath %.c vpath
define test_match
lds=$(1:%.lds=%.lds1) ld=$(1:%.ld=%.ld2)
endef
all: 
	echo $@ $^ $(CC) $(LD)
	echo $(VPATH)
test_match:
	echo 1=$(call test_match,match.lds)
	echo 2=$(call test_match,match.ld)
# Env only affect a53/*
a53/%.o:%.c
	echo $@ $^ $(CC) $(LD)
a53/%.o: CC=test 
a53/%.o: LD=bb
all: a53/vpath.o a53/vpath1.o

%.o:%.c
	echo $@ $^ $(CC) $(LD)
#Test vpath
#a53 only vpath
#~ vpath a53/%.o:%.c vpath
#default vpath
#~ vpath %.c vpath

#detect compiler buildin macros
#TARGET_ARCH=-march=armv8-a -mtune=cortex-a53
TARGET_ARCH=-mcpu=cortex-m3 
%macros:
	echo - | $(@:%macros=%gcc) $(TARGET_ARCH) -E -dM - | sort -u 


#~ vpath %.c 1:2
