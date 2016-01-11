#if ONESHELL is not put here . This file will fail
#And make 4.1 support this feature
.ONESHELL:
all:test
	T=
	if [ -z $$T ]	
	then 	
		echo EMPYT $@ T=$$T $$$$ 	
	else 	
		echo $@ T=$$T $$$$
	fi
test:
	T=333
	if [ -z $$T ]	
	then 	
		echo EMPYT $@ T=$$T $$$$ 	
	else 	
		echo $@ T=$$T $$$$
	fi
