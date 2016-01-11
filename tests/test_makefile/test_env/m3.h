echo - | arm-none-eabi-gcc -mcpu=cortex-m3 -march=armv7-m  -E -dM - | sort -u 
