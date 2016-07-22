OUTPUT_FORMAT("elf32-littleaarch64", "elf32-littleaarch64", "elf32-littleaarch64")
OUTPUT_ARCH(aarch64:ilp32)
ENTRY(_start)
SECTIONS
{
        . = 0xD9040000;
        . = ALIGN(4);
        .text :
        {
                *start.o (.text)
                *(.text .text* )
                 *(.ARM.extab* .gnu.linkonce.armextab.*)
        }
        . = ALIGN(4);
        .rodata : { *(.rodata* .rodata)}
                .ARM.exidx : {*(.ARM.exidx* .gnu.linkonce.armexidx.*)}
                .vectors : {*(.vectors* .vectors)}
                _end = . ;
                __bin_end = .;
        . = ALIGN(4);
        . = ((0xD9000000 + 0xC000) + (2 * 1024));
        __data_start = .;
        .data : { *(.data*)}
        __data_end = .;
         . = ALIGN(4);
        __bss_start = .;
        .bss : { *(.bss) }
        . = ALIGN(32);
        _bss_end = .;
}
ASSERT(__bin_end <= (0xD9040000 +(64*1024)) , "ROM BOOT bootstrap: too big __bin_end > ROMBOOT_END");
ASSERT(__data_start == __data_end, "ROM BOOT bootstrap: Found RW data");
