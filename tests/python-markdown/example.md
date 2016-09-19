## M8

######### Core Pin Mux

Revision: September 7, 2016

|            |               |                                                                 |
|------------|---------------|-----------------------------------------------------------------|
| Date       | Author        | Change                                                          |
| 2013-04-11 | Chris Maslyar | Initial Release                                                 |
| 2013-04-29 | Chris Maslyar | Fixed I2S Out (channels 67)                                     |
| 2013-05-14 | Chris Maslyar | Added VGA outputs and new Audio outputs                         |
| 2013-06-18 | Chris Maslyar | Updated from SVN $top/doc/M8-Signoff-core\_pin\_mux.odt (r9149) |
| 2013-08-12 | Chris Maslyar | Fixed gpioDV GPIO controls                                      |
| 2013-09-09 | Chris Maslyar | Added comments for BSD\_EN as a gpio                            |

This document lists the pin mux registers and the VLSI simulation that
tests the core pin mux condition. The format of each cell is as follows:

|            |                      |                      |                      |                               |                                    |
|------------|----------------------|----------------------|----------------------|-------------------------------|------------------------------------|
| GPIOAO\_10 | 0xc8100024 bit\[10\] | 0xc8100024 bit\[26\] | 0xc8100028 bit\[10\] | JTAG\_Secure register Test536 | I2S\_LR\_CLK\_OUTReg\[28\] Test304 |

BSD\_EN / TEST\_N:

To make the BSD\_EN and TEST\_N pins outputs, you must write the
following registers in the order given below. This will prevent the chip
from entering a production test mode if there is noise near the BSD\_EN
or TEST\_N pin.

1.  Set Bit\[29\]=0 of 0x200d (PREG\_PAD\_GPIO0\_O) to block the BSD\_EN
    signal from entering the TAP controller

2.  Set bit\[0\]=1 of 0xDA004000 (AO\_SECURE\_REG0) to prevent the
    TEST\_N pin from

Once these two steps are complete, you can enable the BSD\_EN pin as an
output by writing bit\[30\]=0 of CBUS 0x200d (PREG\_PAD\_GPIO0\_O)

You can set the level on the BSD\_EN pin using bit\[31\] of CBUS 0x200d
(PREG\_PAD\_GPIO0\_O). 1 =output high. 0 = output low
