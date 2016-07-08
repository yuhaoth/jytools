Android
=======

Android local envsetup.sh

lib/ must be PUT in $HOME
# USB ROM Protocol

V2.0

2015-03-03











History：

| Version | Author | Modify | Date |
| --- | --- | --- | --- |
| 0.1 | [Victor Wan](mailto:victor.wan@amlogic.com) | Draft release | 2010-05-25 |
| 0.2 | [Victor Wan](mailto:victor.wan@amlogic.com) | Add overview figures, add PC driver section | 2010-07-01 |
| 0.3 | [Victor Wan](mailto:victor.wan@amlogic.com) | Add boot flow chart. Add Bulk transfer protocol. | 2010-08-24 |
| 0.4 | [Victor Wan](mailto:victor.wan@amlogic.com) | Modify Bulk transfer protocol. Add driver description. | 2010-09-01 |
| 0.5 | [Victor Wan](mailto:victor.wan@amlogic.com) [Tianhui Wang](mailto:tianhui.wang) | Add Identify command. Add DLL description. Add application sample code. | 2010-09-06 |
| 0.6 | [Victor Wan](mailto:victor.wan@amlogic.com) | Remove Read/Write memory alignment | 2010-10-08 |
| 0.7 | [Victor Wan](mailto:victor.wan@amlogic.com) | Add ReadAux/Write Aux /Modify memory command | 2011-02-16 |
| 0.8 | [Victor Wan](mailto:victor.wan@amlogic.com) | Add BootRom stage define | 2011-10-31 |
| 0.9 | [Victor Wan](mailto:victor.wan@amlogic.com) | Change to High Speed. Disable ReadAux, WriteAux | 2012-10-19 |
| 1.0 | [Victor Wan](mailto:victor.wan@amlogic.com) | Change RunInMemoryAddr command, add RunningFlags | 2013-04-26 |
| 1.1 | [Victor Wan](mailto:victor.wan@amlogic.com) | Device should not return data over host buffer sizeDon&#39;t power off phy after run command | 2014-07-01 |
| 2.0 | [Victor Wan](mailto:victor.wan@amlogic.com) | Secure changes
- .Add 2.2.11 Password
- .Change 2.2.10 Identify return value defines
 | 2015-03-03 |







































Table of content

## 1 Introduction

### 1.1 Scope

This document covers the protocol of  USB ROM.

### 1.2 Audience

The engineers of USB ROM protocol or PC side driver should refer to this document.

### 1.3 Overview

Figure 1 shows the hardware architecture of the USB ROM boot.

Figure 1 H/W Architecture

USB OTG port works on slave mode in Amlogic chip on the board. PC USB host connects to the board. PC side driver and application send command to the board. The board parses the command packet, and does the corresponding actions.

Figure 2 shows the boot flow of the USB ROM boot.

Figure 2 Boot flow

After system power on, ROM code tries to boot from SPI/NAND/SD Card or other devices that stores the &quot;boot code&quot;. If all these failed, ROM code enters the USB ROM boot stage.

Begin of USB ROM boot stage, USB OTG controller is initialized and forced to work on device mode. VBus detection and command detection is enabled to check connection timeout. If the code does not detect VBus high event or does not get the &quot;identify&quot; command from USB slave port, ROM code jumps to power on first start point. The timeout and &quot;identify&quot; command defined in the document.

If the connection timeout detection is passed, USB ROM boot enters the boot process stage. In this stage, ROM boot code waits commands from PC and does the corresponding actions.

USB ROM boot use vendor class (0xFF) as the transfer protocol. There are 3 packets is defined:

- .Command packet:         Transfer command from PC to board.
- .Data packet:         Transfer data between PC and board.
- .Status packet:        Transfer status between PC and board.

All command packets are transferred through EP0.  Large data packets are transferred through EP1 and EP2. Small data packets are enclosed to command packet and transferred via EP0.

Figure 3,4 shows the small data transfer flow:



Figure 3 Write Memory Command

Figure 4 Read memory command

Figure 5 shows the large data transfer flow:

Figure 5 Write Large Mem command



## 2 Protocol

### 2.1 Overview

Vendor ID: 0x1B8E // Amlogic

ProductID: 0xC003

Config: 1

Interface protocol: 0xff  //USB\_CLASS\_VENDOR\_SPEC

### 2.2 Commands

| Command Name | ID | Descriptor |
| --- | --- | --- |
| WriteMemory | 0x01 | Send single 4bytes or burst 4~64bytes from PC to board |
| ReadMemory | 0x02 | Send single 4bytes or burst 4~64bytes from board to PC |
| FillMemory | 0x03 | PC to board,  Format: Address, value; Address, value |
| ModifyMemory | 0x04 | Modify memory by mask and operation |
| RunInMemoryAddr | 0x05 | Run from memory address |
| WriteAuxReg | 0x06 | Write Aux Register |
| ReadAuxReg | 0x07 | Read Aux Register |
|   |   |   |
| WriteLargeMem | 0x11 | Send 512Bytes ~ 32Mbytes block data from PC to board |
| ReadLargeMem | 0x12 | Send 512Bytes ~ 32Mbytes block data from board to PC |
|   |   |   |
| IdentifyHost | 0x20 | Identify host driver version, get ROM information. |
| Password | 0x30 | Send the password to check |

Table 1 command list

2.2.1 ReadMemory

   Read board memory to host PC. Support single 4bytes read and burst 4~64bytes read.

   Protected by password.

   Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Device-To-Host | 1 | 0x1 | 1 |
| bRequest | 2 |
| wValue | High 16 bit memory start address |
| wIndex | Low 16 bit memory start address |
| wLength | Buffer length (Buffer length  = sizeof memory area) |

Table 2 ReadMemory command

- .Buffer length should equal or smaller than 64, and equal or bigger than 4

   Samples:

-
  - .Read memory 0x82000100, 4bytes: wValue=0x8200,wIndex=0x100,wLength=4
  - .Read memory 0xC1040004, 64bytes: wValue=0xC104,wIndex=0x4,wLength=64



2.2.2 WriteMemory

   Fill board memory from host PC. Support single 4bytes read and burst 4~64bytes write.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 1 |
| wValue | High 16 bit memory start address |
| wIndex | Low 16 bit memory start address |
| wLength | Buffer length (Buffer length  = sizeof memory area) |

Table 3 WriteMemory command

- .Buffer length should equal or smaller than 64, and equal or bigger than 4

Samples:

-
  - .Write memory 0x82000100, 64bytes: wValue=0x8200,wIndex=0x100,wLength=64
  - .Write memory 0xC1040004, 4bytes: wValue=0xC104,wIndex=0x4,wLength=4





**2.2.**** 3 **** FillMemory**

   Fill board memory from host PC. The memory address and value stored in buffer.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 3 |
| wValue | Check sum of buffer |
| wIndex | 0 |
| wLength | Buffer length |

Table 4 FillMemory Command

Buffer:

| Offset(bytes) | Description |
| --- | --- |
| 0 | Memory address bit 0:7 |
| 1 | Memory address bit 8;15 |
| 2 | Memory address bit 16:23 |
| 3 | Memory address bit 24:31 |
| 4 | Data , bit 0:7 |
| 5 | Data , bit 8:15 |
| 6 | Data , bit 16:23 |
| 7 | Data , bit 24:31 |
| 8 | Memory2 address bit 0:7 |
| 9 | Memory2 address bit 8:15 |
| 10 | Memory2 address bit 16:23 |
| 11 | Memory2 address bit 24:31 |
| 12 | Data2 , bit 0:7 |
| 13 | Data2 , bit 8:15 |
| 14 | Data2 , bit 16:23 |
| 15 | Data2 , bit 24:31 |
| … | … |

Table 5 FillMemory Command data



- .wIndex must be set to zero.
- .wValue is the check sum of buffer (sum byte by byte)
- .wLength &lt;= 64
- .Memory address and value stored in buffer by turn.

Samples:

-
  - .Write 0x40100000 to memory 0x82000100 : buffer:0x00 01 00 82 00 00 10 40 , Buffer length=8
  - .Write 0x08 to memory 0xC1040004, 0xC10100408 to 0x30102038, buffer:0x04 00 04 C1 00 08 00 00 08 04 10 C1 38020 10 30 Buffer length = 16



**2.2.**** 4 ****Modify**** Memory**

   Modify memory from host PC. The memory address, mask and value stored in buffer. Operation stored in command.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 4 |
| wValue | Operation (see below table) |
| wIndex | 0 |
| wLength | 16 |

Table 6 ModifyMemory Command

  Operation defines:

| Value | Operation | Description |
| --- | --- | --- |
| 0 | \*mem = data | Set memory |
| 1 | \*mem = (data &amp; mask) | Set memory with mask |
| 2 | \*mem = (\*mem | mask) | Set memory bits |
| 3 | \*mem = (\*mem &amp; (~mask)) | Clear memory bits |
| 4 | \*mem = (data &amp; mask) | (\*mem &amp; (~mask)) | Set memory bits area |
| 5 | \*mem = \*mem2 | Memory copy |
| 6 | \*mem = (\*mem2 &amp; mask) | Memory copy with mask |
| 7 | while(data - -){\*mem++ = \*mem2++}; | Big memory copy |

  **Table 7 ModifyMemory Command operations**

Command data:

| Offset(bytes) | Description |
| --- | --- |
| 0 | Memory address bit 0:7 |
| 1 | Memory address bit 8;15 |
| 2 | Memory address bit 16:23 |
| 3 | Memory address bit 24:31 |
| 4 | Data , bit 0:7 |
| 5 | Data , bit 8:15 |
| 6 | Data , bit 16:23 |
| 7 | Data , bit 24:31 |
| 8 | Mask, bit 0:7 |
| 9 | Mask, bit 8:15 |
| 10 | Mask, bit 16:23 |
| 11 | Mask, bit 24:31 |
| 12 | Memory2 address bit 0:7 |
| 13 | Memory2 address bit 8:15 |
| 14 | Memory2 address bit 16:23 |
| 15 | Memory2 address bit 24:31 |

Table 8 ModifyMemory Command data

- .wIndex must be set to zero.
- .wValue is
- .wLength
- .Memory address and value stored in buffer by turn.

Samples:

-
  - .Write
  - .Write

**2.2.**** 5 **** RunInMemoryAddr**

  Let target CPU run at specified memory address.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 5 |
| wValue | High 16 bit memory start address |
| wIndex | Low 16 bit memory start address |
| wLength | 4 |

Table 9 RunInMemoryAddr command



- .Memory address should be 32bytes alignment.
- .DATA: Running flags:
  - .Bit 0: Keep power on usb controller (if set this bit, usb controller will keep power on after run command, if not set, usb controller will be powered off after run command )
  - .Bit 1 ~ 15: Reserved

Samples:

-
  - .Run in memory 0x82000000 , then power off usb controller:

        wValue=0x8200,wIndex=0x0,wLength=0,buffer: 0x00 00 00 00

-
  - .Run in memory 0xD9000000, then keep power on usb controller:

        wValue=0x8200,wIndex=0x0,wLength=0,buffer: 0x00 00 00 01









**2.2.**** 6 **** Rea ****dAuxReg**

   Read one CPU AUX register to host PC.

   Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Device-To-Host | 1 | 0x1 | 1 |
| bRequest | 7 |
| wValue | High 16 bit AUX register start address |
| wIndex | Low 16 bit AUX register start address |
| wLength | 4 (Buffer length) |

Table 10 ReadAuxReg command

- .Buffer length should equal 4 (read one AUX register)

   Samples:

-
  - .Read AUX 0x20, 4bytes: wValue=0x0000,wIndex=0x0020,wLength=4



**2.2.**** 7 **** Write ****AuxReg**

   Write one CPU AUX register from host PC.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 6 |
| wValue | High 16 bit AUX register start address |
| wIndex | Low 16 bit AUX register start address |
| wLength | 4 (Buffer length) |

Table 11 WriteAuxReg command

- .Buffer length should equal 4

Samples:

-
  - .Write AUX 0x20, 4bytes: wValue=0x0000,wIndex=0x0020,wLength=4



**2.2.**** 8 WriteLargeMem**

   Fill board memory from host PC. Support single 512 ~ 32M bytes write. The memory data transferred via EP2 (out bulk ep). One packet is 512 bytes.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 0x11 |
| wValue | Data block length (size in byte). (1 ~ 4096) |
| wIndex | Number of blocks (1 ~ 65535) |
| wLength | 16 |

Table 12 WriteLargeMemory Command

  Command data:

| Offset(bytes) | Description |
| --- | --- |
| 0 | Memory start address bit 0:7 (bit 0:1 = 0) |
| 1 | Memory start address bit 8:15 |
| 2 | Memory start address bit 16:23 |
| 3 | Memory start address bit 24:31 |
| 4 | Data length, bit 0:7 |
| 5 | Data length, bit 8:15 |
| 6 | Data length, bit 16:23 |
| 7 | Data length, bit 24:31 |
| 8 | Sequence number, bit 0:7 |
| 9 | Sequence number, bit 8:15 |
| 10 | Sequence number, bit 16:23 |
| 11 | Sequence number, bit 24:31 |
| 12 | Data check sum value, bit 0:7 |
| 13 | Data check sum value, bit 8:15 |
| 14 | Data check sum value, bit 16:23 |
| 15 | Data check sum value, bit 24:31 |

Table 13 WriteLargeMemory Command data



- .Memory address should be 32bytes alignment.
- .Data block length is one bulk urb length, should equal or smaller than 4096, and equal or bigger than 1
- .Number of blocks is number of bulk urbs, should equal or smaller than 65535, and equal or bigger than 1
- .Number of blocks =  （Data length + （Data block length - 1））/ Data block length

Samples:

-
  - .Write memory 0x82000100, 512bytes: wValue=512,wIndex=1,wLength=16
  - .Write memory 0xC1040004, 4096bytes: wValue=4096,wIndex=1,wLength=16
  - .Write memory 0x83000000, 65536bytes: wValue=4096,wIndex=16,wLength=16
  - .Write memory 0x83000000, 1M bytes: wValue=4096, wIndex=256,wLength=16



**2.2.**** 9 ReadLargeMem**

   Read board memory to host PC. Support single 512~32Mbytes read. The memory data transferred via EP1 (in bulk ep). One packet is 512bytes.

Protected by password.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 0x12 |
| wValue | Data block length (size in byte). (1 ~ 4096) |
| wIndex | Number of blocks (1 ~ 65535) |
| wLength | 16 |

Table 14 ReadLargeMemory Command

Command data:

| Offset(bytes) | Description |
| --- | --- |
| 0 | Memory start address bit 0:7 (bit 0:1 = 0) |
| 1 | Memory start address bit 8:15 |
| 2 | Memory start address bit 16:23 |
| 3 | Memory start address bit 24:31 |
| 4 | Data length, bit 0:7 |
| 5 | Data length, bit 8:15 |
| 6 | Data length, bit 16:23 |
| 7 | Data length, bit 24:31 |
| 8 | Sequence number, bit 0:7 |
| 9 | Sequence number, bit 8:15 |
| 10 | Sequence number, bit 16:23 |
| 11 | Sequence number, bit 24:31 |
| 12 | Reserved |
| 13 | Reserved |
| 14 | Reserved |
| 15 | Reserved |

Table 15 ReadLargeMemory Command data



- .Memory address should be 32bytes alignment.
- .Data block length is one bulk urb length, should equal or smaller than 4096, and equal or bigger than 1
- .Number of blocks is number of bulk urbs, should equal or smaller than 65535, and equal or bigger than 1
- .Number of blocks =  （Data length + （Data block length - 1））/ Data block length

Samples:

-
  - .Read memory 0x82000100, 512bytes: wValue=512,wIndex=1,wLength=16
  - .Read memory 0xC1040004, 4096bytes: wValue=4096,wIndex=1,wLength=16
  - .Read memory 0x83000000, 65536bytes: wValue=4096,wIndex=16,wLength=16
  - .Read memory 0x83000000, 1M bytes: wValue=4096, wIndex=256,wLength=16

**2.2.**** 10 IdentifyHost**

   Send Host driver information to device, return ROM information to Host.

   Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Device-To-Host | 1 | 0x1 | 1 |
| bRequest | 0x20 |
| wValue | Host driver version |
| wIndex | Host other information |
| wLength | 4~8 |

Table 16 IdentifyHost command

Return data:

| Offset(bytes) | Name | Description |
| --- | --- | --- |
| 0 | ROM Major | ROM Major Version Number |
| 1 | ROM Minor | ROM Minor Version Number |
| 2 | Stage Major | 0     (Reserved for SPL/TPL&#39;s Stage Major) |
| 3 | Stage Minor | 0     (Reserved for SPL/TPL&#39;s Stage Minor) |
| 4 | Need password |   |
| 5 | Password check OK |   |
| 6 | Reserved | 0 |
| 7 | Reserved | 0 |

Table 17 IdentifyHost command

- .This command will be sent as the first command after USB enumeration stage.
- .Device will reply this command in no data transfer state.
- .Major and Minor version number is same as this specification version number.

SPL/TPL&#39;s stage Major Minor recommend value:

|   | Stage Major | Stage Minor |
| --- | --- | --- |
| IPL(ROM) | 0 | 0 |
| SPL | 0 | 8 |
| TPL | 0 | 16 |

                   Table 18 SPL/TPL stage define

ROM Major Minor version number with chip release:

| Chip | Rom Version | ROM Major | ROM Minor |
| --- | --- | --- | --- |
| A3 | A | 0 | 7 |
| M3 | A | 0 | 7 |
| M6 | A | 0 | 8 |
| M6 | B | 0 | 8 |
| M6 | D | 0 | 9 |
| M6TV | B | 0 | 9 |
| M6TVLite |   |   |   |
| M6TVD | A | 1 | 0 |
| M8 | A/B | 1 | 0 |
| M8baby | A | 1 | 0 |
| G9TV | A | 1 | 1 |
| G9TVbaby | A | 1 | 1 |
| GXBaby | A | 2 | 0 |

                         Table 19 ROM Major Minor define

**2.2.**** 11 ****Password**

   Transfer password from host PC, password data size can be 1 to 64 bytes.

  Command Descriptor:

| Field | Value | Dec | Hex | Bin |
| --- | --- | --- | --- | --- |
| bmRequestType.Recipient | Device | 0 | 0 | 0000 |
| bmRequestType.Type | Vendor | 2 | 0x2 | 10 |
| bmRequestType.Direction | Host-To-Device | 0 | 0x0 | 0 |
| bRequest | 3 |
| wValue | Check sum of buffer |
| wIndex | 0 |
| wLength | Buffer length |

Table 4 FillMemory Command



- .If 3 consecutive failures for password verification, system should reboot.
- .wIndex must be set to zero.
- .wValue is the check sum of buffer (sum byte by byte)
- .wLength &lt;= 64
- .Memory address and value stored in buffer by turn.

2.3 Notes

## 3 PC Driver interface

### 3.1 PC Driver architecture



### 3.2 PC Driver sample code

### 3.3 PC Application Lib (DLL)

UsbRom DLL lib support Write/Read RAM and chip registers.The follow list shows it APIs:

3.3.1 Get the device path and its handle.

1. 1)int **AmlScanUsbRomDevice** (OUT char\*\* DeviceNameArray);

Description:

   Scan all usb rom devices which have connected to PC.

Parameter:

  OUT char\*\* DeviceNameArray: the device array that have found

  Device name :&quot;UsbRom\_n&quot; (0&lt;= n &lt;=7).

Return:

  The number of usb rom device found in pc, if returns 0,there is no device found

  There are at most 8 devices in pc.

2)  HANDLE **AmlGetUsbRomDeviceHandle** (IN char\* DeviceName);

Description:

   Get the handle of  usb rom devices corresponding to the DeviceName.

Parameter:

  IN char\* DeviceName: the device name

Return:

  The handle of  usb rom devices. If the operation fails, it returns NULL

3.3.2 Read/write memory.

BOOL **AmlUsbWriteData** (AmlUsbRomRW \_t \* pUsbRomRW );

BOOL **AmlUsbReadData** (AmlUsbRomRW \_t \* pUsbRomRW );

Parameter:

  AmlUsbRomRW \_t \* pUsbRomRW: the parameter descript in 3.3.5 sector.

Return:

  If the operation success, it returns TRUE, otherwise FALSE

3.3.3 Read/write the register.

       BOOL **AmlUsbReadRegister** (AmlUsbRomRWRg \_t \* pUsbRomRWRg);

BOOL **AmlUsbWriteRegister** (AmlUsbRomRWRg \_t \* pUsbRomRWRg);

Parameter:

  AmlUsbRomRWRg \_t \* pUsbRomRWRg: the parameter descript in 3.3.6 sector.

Return:

  If the operation success, it returns TRUE, otherwise FALSE

3.3.4   Run the code in target device

      BOOL **AmlUsbRunBinCode** (AmlUsbRomRW \_t \* pUsbRomRW );

Parameter:

  AmlUsbRomRWRg \_t \* pUsbRomRWRg: the parameter descript in 3.3.5 sector.

Return:

  If the operation success, it returns TRUE, otherwise FALSE





3.3.5 Read/write memory struct

typedef struct **AmlUsbRom**

{

  HANDLE hDevice;

  DWORD DataLength;

  LPVOID buffer;

  DWORD \*ActualLength;

  DWORD RamAddr;

} AmlUsbRom\_t;

Description:

1. 1)hDevice: device handle
2. 2)DataLength: length of data you will send to or receive from the target device
3. 3)buffer : data buffer for upload or download
4. 4)ActualLength: Reports bytes transferred to/from the communication
5. 5)RamAddr: write/read ram mode: it means the data store address in ram.

run mode: it means the code address in ram

3.3.6 Read/write register struct

typedef struct **AmlUsbRomRg**

{

  HANDLE hDevice;

  DWORD DataLength;

  LPVOID buffer;

  DWORD \*ActualLength;

  DWORD RamAddr;

} AmlUsbRomRg\_t;

Description:

1. 1)hDevice: device handle
2. 2)DataLength: length of data you will receive from the target device.
3. 3)buffer : data buffer for upload or download.
4. 4)ActualLength: Reports bytes transferred to/from the communication. Only used by reading register. Pls set 0 in write register mode
5. 5)RamAddr:register address in ram. Only used by reading register. Pls set 0 in write register mode

###  3.4 Lib sample code

BOOL \_stdcall AmlUsbWriteData(AmlUsbRom\_t\* pUsbRom)

{

        if((pUsbRom-&gt;DataLength &lt; 0) &amp;&amp;

(pUsbRom-&gt;DataLength &gt; 65536))//check parameter

                return FALSE;

        if(ValidParamHANDLE(&amp;(pUsbRom-&gt;hDevice)) != TRUE)

                return FALSE;

        if(ValidParamVOID(pUsbRom-&gt;buffer) != TRUE)

                return FALSE;

        static int WriteSeqNum;

        int TryCnt = 0;

        DWORD actual\_len = 0;

        int SendSizeOld = -1;

        USHORT CheckSumValue = 0;

        int RemLen, SendSize, SizeOffset = 0;

        CheckSumValue = checksum((USHORT\*)pUsbRom-&gt;buffer,pUsbRom-&gt;DataLength);

        do{

                actual\_len = 0;

                RemLen = pUsbRom-&gt;DataLength;

                TryCnt++;

                if(TryCnt == TRYCNT)

                        break;

                while(RemLen &gt; 0)

                {

                        SendSize = RemLen&gt;MAXSIZE ? MAXSIZE:RemLen;

                        if(SendSize != SendSizeOld)

                        {

                                if(WriteLargeMemCMD(pUsbRom-&gt;hDevice,pUsbRom-&gt;RamAddr,

                                        pUsbRom-&gt;DataLength,SendSize,CheckSumValue,WriteSeqNum))

                                        break;

                                SendSizeOld = SendSize;

                        }

                        WriteSeqNum++;

                        actual\_len += write\_bulk\_usb(pUsbRom-&gt;hDevice,(char\*)pUsbRom-&gt;buffer+SizeOffset, SendSize);

                        SizeOffset += SendSize;

                        RemLen -= SendSize;

                }

        }while(actual\_len != pUsbRom-&gt;DataLength);//status[0]);

        \*(pUsbRom-&gt;ActualLength) = actual\_len;

        if(actual\_len == pUsbRom-&gt;DataLength)

        {

                return TRUE;

        }

        return FALSE;

}

### 3.5 PC Application

 ![](data:image/*;base64,iVBORw0KGgoAAAANSUhEUgAAAeUAAAGHCAIAAAABbt1kAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOxAAADsQBlSsOGwAAQT9JREFUeF7tnQ+sJVd932fev12v/4LXGDtxEG1RkKq2ShVCIwS2mxIgbQnFNg5NmihtcEJRAyWoaTCCtVSTqqWEqKAQJwLaJhATbdpGUajlSiSyXTexK9qkUnBCsR2D/7DeeHe97+3b9969t7+5v/d++9vfOXPmzNwz987M/V7dfTt37vnzO59z7nd+85tzZvJHn/3Ka34iz19y3dqRS/fWR+uHL79sI8+y7NBh+pMdOlT83VjL1laLDX7RR37t7F3YiS0QAAEQWE4Ce6P9drNO8se97YOdh61Uruxl4wMVpUTnz1+E7fxBxrOb4+Lb57aypx5/9HhRaJ7d/IfZlS/PVrfzl76EPk9WVjjryvpavrKW5etr62vnJ5PVSbF/bWVC24fyQtB5J++hj7RzMsroz162X8Jy9hxaDQIJCYx3ih8XXh0nsLKRU09NDhWSOMoLkeVXfm6U707y1d1sNBrvrk1IIndXs/VRtkfKWkh7sSc/cHv3xqSw2WQt29rOVguNzdamf7fPZS+cynYuefQ3X5zq9ZHV7MqXXiCydpiy5asrpN2k2vsVk3aXvCbjvXxPud+jg2NNxxnDPBAAARBoicB4tyh4PBlnk3yvOOiOR2P6WOwcHRyD6Ut+8cZ0fz7aIw0n73w/GQn3+d3s7Hb25BOP/u+/kmc/8LUsP50dvnw/56H1qa4Xkl1knqr2/lcr06/4xdZMX/l4PKGDBr/oEIFXPwjgsNqPfoKV/SAwdqSP1Hk0Wc/HP/76jY+886XXX13q8nob+JP/9snP/u7JXRJxOsfa3SrSPPV4nv3N38+uvCS/dGNy6Eixy9FrKeuCcE81mvZPRuN8QmGQ6eGCdrDFfAzBCwRAAASWhIAEsPOpd8v+cuFWj++4+dAn37Z5+ou/ND51cry1OTm/PdnbnezuZOQH7+1MVbTwnCY706A1hU12tve2z5294ppX3P2Zn/3Pl9/zxWeyfDfb3sr2NrMXzl6s18c/b/BOJh/hPXl+l4f8j/7k1KyDb4y3vyRd1dNmyrlYT+1fErPRTf3qaNHrEYWexxTcGP/2Xz758Z9dfdn1+era+Ozp0YunJjvns52dCXm3ReiDxHqSkYKPRpO9Hfpqsr21t/niqdOnn16//G989g++7U3/q9DrU9vZysnsW38yPRrsreQXX6As9H7yERFr9+M+Q1JqFmtSahZrOs4UERu8O0+gXz8DWAsCHSdAYQbSaJI+cqunYi32js68kG8cyjc2stW1fG09X6P5duvkX09WVvPV1XxlNVuhyR2rGWk9/Z2mWVlbP/vsN6+/ZqMoZGc6S2/62o9Nj1dk14FDXfjU06uT0xdt648HuZ2pIFQl3r0g0PHRD/NAoEcECoGeimGxcfDaJfUuYtaTzRfHZ8+MN18k33ly/txke3uyfW5ybmuyeXb84pnRmVOj038xOnua0ky2XiwSkNNNcz1WpxcFN6ZXDcdXHuj1hJSehD/PRlMtzzjuIWGQQrMvVmr6av/b/YC12CfXPXsEemlN7cVBBUbSvCy8u08gVxPkWLVHF/ZQtHp89hR52ePNM5f97X9wzYc+Nd7cnGxujjfPjjbPjM+cGr/4wvj0X3zbr95/5Q//9FSv9/KVFfKyC3GaHHjSpNLF/OvXPpKtHcquPJJdsp4d/46pXpMc35UdRK7Zuz6QtWP737Jk/8Nn9/ePJ5MvXOeVvvwdT9eVxMkXr5cs3uySoEHhdY1BehBYJAEsSVsk/fp16wly4+mFxN95xTPveev6Da/MaK7d+R0Say706Xe/lQLW2e75Imy9u3PDvY/w/qdu+es0Jfvs7vhPT55++0N/nr/2j7Otrewszdn7+jR+Tfq9Pp0ZwpHyfd/5wINWIRHX9pVVyk4hm5zy5u98xk1w6XX/6sgDn6nbaFJhysi5vNlFphsUXtcYpAeBRRKg82m8u08gOEQmu+fHdIHxPOny7nP/8sc47fW/9Nt0vZFmZdPfC2L9g6+mPXlxkZkugB1MtBtN15pP/WsVgB5d2N5P6Yj1sWPZsWPsgE8VPltdpdg5L8XZl3tr+Nbr/3GD4d4sV4OKkAUEQAAEZiXARxT9ung2Nk3jG09n8tGMvWffexsn/LbP/Hda3/jtX/gD/vjUW1+VjSgBhb1JsgtHuNg74TD1/ivPvuePsiNHsqs2ssNr2W9cJ5rO3xeRa9qV58eOHfvIRw6cbgqX3HUX7Vj9RycpTRG1pkui+Wjy+WtNs8lN3np9Medv8sVrLlT5jhO8rXfuV3fwlXwrJXizeMsvzH7HCSm8bNu1xxiPjyAAAiBQgwDJMb92aKbHNJJFXvLvfPs3fvT169feQBM/SIEnezSHb4eE+/pP/ldd8jffTp71dHpfvjJeWT27m/3pybNv+59P59/zWJbvZC+Os/yZ7Bv/g8rdyDYO00LGbFQU53mVhkT2g9qFe03r3CcXR9yloNWcpZO0laMcxUfKs5rn73xeUvG3Rx74Zf5q32fnrw/2mHL28zrl034qRwov23btuVC12DDgjRrDEElBAARiCJAvPH0Xd8ibLhHnmAVNr6Z7ONEaGQqAFHOdaZHh5OmferOU+PQP/bV8ZUI3X1rJxyt0sXKyV9yHaRr+ztZJWqcuNq2XWb9CxUOmYY1iNsi0mIsm8E0m5F3TfnKr6UVfkbs9VdJ1eo/GG9MSS/Ra7d+66T1s4pHf+/Q0/X4W1nH6dpqA9+vS7B4ph+Vcmk3783e+cBD7NiVIqovSO/ZIXUPfoKM93iAAAqkIZIeytY39977Y0Mci9Exh6zFdVByP6E2x6cIBXsmu//R/E0m6/jf+mFY70oTsPB/TzJKc7vYx2s3HUw89n84P2aGiLqX/VzK+o5MEX6gwz0TrQr+P3VVM9dtXaq4qX6d3caMpcq5XDuU/8qJYQBv7ukk4Lkjlxdvqq63ve6+VD52LmZaVc3FKKmq/tJj0bi2p+g/lgMDsBDKa1IV3HwjQ5At+F3I6Fe79jiO9Pl8sXCT/miIeE5pLN7nu3/82C8+zd7yBN6793CPFchmS7GyPlDrf21kR/5riH5dOXeyVQysH92Fd3793H0WrpwFrrby8TUp9kVjTcWN6t9eVPF+lu6lu7N8hUGc89+b3820D+WW23Y+0R946F+8sK0fvn/za5fSOT+/Wom0Y8HZxiMW7+wSmfhfefSJwQbVzFtXpjL3pvD1agD4eXfeLv7Uv1u/+PvryuX/y2kIbj1xx7W9+Pacl7BQwIed6GuOeiib51xeiIHn2uieyS49kl+bZFYeyz13uVWpScHKuC7G+WMpXf4osKGLefJWSQi6Tz164mllcDHzzv2DLzH7aQ1/pnYVhP17c/cQk3hf6qq+85ZcVZerdj8YcmKqPN9gGARAAgWoCepo8xzGK24NMxfqLlz7x/a9YvfrlK0cuy9cPXf/p3+XSnnn39xdB6tEO3Tl7ZW/7mv/wR7z/W3/3paOdvdPnxn96avet//d8/qYT2e6Y7jeSnXs8e+r/TPX6qkPZ5Wv0LJljr/y48aBlWkgxIYTmhyi/m7z61fdMxXp6DxG+pSpZcMnv/Btp3rm/t6/XtMe7X++kNJLe7I/5KqZeNmzzmQ/RX5nirQuv7hikAIE5EpjoO8vPsV5UVZMA352YNJAfLTP9RL4sqeQXDj9+83WrL3nZyqWX5RuHX/JjP3PkDT/wzB1/Zzp3hEIfFKfeyfe2yaG+5vN/tn3ffzzziX+2t717ZmvvsdOjH/zqKH8zPangfHZuJTv79ey5PyS9/vPsqkuyy1ezQ2sT8q/35+oVoQ89gY+t58g22cAf195b/KXbXxdf9eTG16NPXQj18PEGLxDoLIHxLoZoZzunxDDpsulNVif/aePrr79m9cqX5JdctnLoMN2lr5jRQVcdp3egzies1+dJr4vbq+5sT3Z29s7vnNkaPfbi5G2PjQu9nuxmZ+iBXl/LvvHoBb3ODx8af3a60DH6tfYzB0nV6cBk+jCFLr8O/9bdYt722+/ssqmwDQRAoC8ELjq4Hqj25LOrj/2tK1cvu2LlEvKvD5Fe02LwYq4eTeyYTt1bKWaDkGRP9Xq3WJu+t7NL8ZDHzma3fW2S//2z2e5edno32/kTjofs+9ek18SFLh6So00bq8UjwaauKF/nozoufk0fWkMVHuzHjQ76Mqymdnb/sNornDAWBAoCrmR/89/lz/7IX528cIKWuaxOb6laTJkuZvXRLGzyr+m+ULQknbzs0YT+0kztvd293dHpnclzL33FrQ88cZFeP6njIST866uk1zzrg8Sa7k9C92O9SLWLYMgF4XbFGiqAYQsCILCcBGzwaupi3/Hac//6xv/38E//0OlnvrmxvjadYk2z8saF1BYX/EartPp8PFqhiSPFAx7p43iHJmq//BVv+PR/+dCX/9I9961c8K+nek3XGy8t4tck/LT8ZnVtdX0a0KC51YcowrJRqDa/6F7a09fILFpnf226vnF/jvdydlevWj1S93vsleEwFgS6SmA/BnLwZNRpyGF9Mvrx1+398rsPHpAbZ/vTJ0d3/drmZ7+c727TE2Cm8WuKh1zQ65VtWp6TTT3rYpo3TRucPll9deNArPnm2fuvDVo1aV40P6SYnjKd1YdXHwiUrUftg+1LZCMei9yHzibRI/GkC4w0JyQfFZP5yH/lWDF5t/SxSHAwb0TfGWpvLyOVp0XndOM8SsOKTwFr8+L49b5e03dXZdmZ58mZlsfIjNenN/ErAiP7xU8KB5zccFFwfuyNepmPfeAMG0Gg0wTOQ6873T/7xhWPFljNdn2dRUEL3i1f0lw6WgNFH8VlIkGnPYWsT9WVZtzR9ULSbp4fSOsbR0ccvd5+oVDn4p/88ZO6EA7hLb6H30HGPtCFjRcmZYJFlwl41hl32dwltq3FWXHbL8le3MvWvlnMD3nZP/2LMyde+MYnD+4EuMTE0XQQAAEQ6CCBo29fyZ7+SnbmKScO3UFjYRIIgAAIgMBFz5cBDhAAARAAgQ4TgH/d4c6BaSAAAiCgCECvMRxAAARAoB8EoNf96CdYCQIgAALQa4wBEAABEOgHAeh1P/oJVoIACIAA9BpjAARAAAT6QQB63Y9+gpUgAAIgAL3GGAABEACBfhBIoNdHr321aau7hxPwfvpr3i6qshJ0OZIrnLgf/QArQQAEQKCKQAK9fv65r4pixkgnpSer6C+/vRbqMkXoI48KVU3G9yAAAiDQKwJ09769c2RxAr32yqh40OIRa+da5Jh2imS7TrcupPJIUJmgV/0DY0EABEDAEkh5fz4RX63CukKjzuxle4MhWsRNGl2Lm7fMYUfPgwAIgEBPCRy9dS174sFs6/kE/jV7wV4/Wn8lpHgnB0OMG15JU1ekIyrh6EplsUgAAiAAAt0nkECvxaWVeHQgQi1KTWhkO94p1nV1Hy4sBAEQAIGEBGLjIb/35d93a73p5hvFrTYRDBMSEb/YXEjk7K5ec3ZvXEW+8lKQorwGJwSHokAABEAgCYFbbr/j5LceCxQl8ZAaek2FmhKlDhOY1lLrfqUDI2WedaVea0u8sn71y74zCUoUAgIgAALtETh+7z1t6XXZQcC90qhna7iut9v4MhfbTemqc9nlzfYQo2QQAAEQSEKAIgHxep0gfi2+sNZNuQDoCnHldUK5IOm9XJmEEQoBARAAgd4RSKDX3GbWZZnvoTdkf5iOZNHXLRvMIeldH8BgEAABEIghUC9+HQ6Kx9SHNCAAAiAAAkJg3vEQoAcBEAABEJgDgWTxkDnYiipAAARAYJkJQK+XuffRdhAAgT4RgF73qbdgKwiAwDITgF4vc++j7SAAAn0iAL3uU2/BVhAAgWUmgPl8y9z7aDsILJ7AsG8d8f73vevOD34gQLnWfD7o9eLHKywAgWUmQHp95tRTgyRw/31feujhRxLqNeIhgxwnaBQI9IzA7s7W8N7J+wB6nRwpCgQBEACBVggsbzwEN8huZUChUBA4IFB52zlOyPEQcq6HR45EJm08ZKn1mlAOb4igRSDQBQLHjn34iqtuiLnjEPS68sDW8HkFMfS7MFZibIg59MWUgzQgAAIugfWNI9DrGJGJnR/y5IPZZorn7ZYNVv3IgloD2psxXJr5tnHVtexEYhAAARCYJ4F5XG90b4rNLfTeLJul1hVc8+DHBpo+I1YcA2YEiOwgAAIzEmhFr+W5MPKkGPMIAjba7HSfqm4EXUu8V9MNi0iFdWuZkWmD7K6peo9+zk7ZM3cC+xvYgywgAAIdJNCKXnvVuUHjy54cpvezcOtHRGoPPUay9XGigZFtZDFmm2eqeR9SXPbk4rL9bZiNMkEABFol0Ipet2pxmRPNqu312SPt0brv+u8mIBNZZnwyrdEQ2XhuSAkCy0OgXb0OPDBXohBulCOQy+0YkbYZNc4bMa8cB26kIrzHW6A5TpRVGoPFpPF+jCmnsuFIAAIgMH8Crei1KIJ4u16drYxfSy7xbQPSpsPQ5hgQgzVG7t1rntwE1nodVynbE2NJWZoATA1KG+kNpGibZ7EHeUGgywTC14TY8ph4aafa2IpexyhLcgoSDHGvW0bWFSPZuihWxiRdrmPukdYiGQiAQICA+3OO2dNxpK3odRttZnGsK6l1LaklvhIxr1tL2dnG7OWgBBAAgQETWLBeR0owu7EJ/Vndo+LbGrH2areJNoh/LYnFVKnC3ePWrhPLaZou02uwOy5NXcZt934c8OBG00BgYARa0Ws3SlC2J+wvS0jaRLplf5LO0IEUbU+ZbSaNZGdj3FhQODqkv/UG9E2ZOo1pvrFEMorBOsFCYlZJ+guFgMDSEmhFryuFw6trvFP3hFuO1kQtQ65yzb9H3Ri0d4++Llor/DL/FqFGEACBThFY9vvzhR/90KmugjEg0CMCte73dPzee3rUtFqmJruf6vR+T9Dr0KPVanUMEoMACAiBeL2++6MfGza3NM8Dg15XHvqGPYzQOhBoj0C8XrdnQy9K7sr9VHsBC0aCAAiAQF8ILHU85I1vektf+gl2gkDvCEQ+r6B37UprcC3/enn1mp5ClJY7SgMBEDAEhvREqpY6F3rdElgUCwIgAAKJCdTS61bmXyduEIoDARAAARDIMug1RgEIgAAI9IMA9Lof/QQrQQAEQAB6jTEAAiAAAt0mkGfZhP4hHtLtboJ1IAACICAE4F9jMIAACIBAPwhAr/vRT7ASBEAABGqslwEsEAABEACB5ARuuf2O8MKio7etZY8/lG2diNVrrAZM3kkoEARAAASYQGK9BlYQAAEQAIGFEBD/GvHrhfBHpSAAAiBQm0AavdbPtdLPu3LNCTwBy81Yllg/ITdcXW0eyAACIAACXSWQRq/1U8OppeFnuQYeYOhmDDxaVz8nlyvtKmTYBQIgAAIJCKTR60i5JPFlVQ085FvaxIm9Cm6kWYpNwANFgAAIgEBXCSTTa28D2Tvmr7RY837XI5b0/K3EPSSl5DLF4kHjXR1gsAsEQGBmArQYvViOnmI9ug5ZaBU23rHRXBNC4Qa53reRdU6gVVuyQLJnHhQoAARAoNMEEvjXErIQp7jsGqBxq92ot0GlvWwdJzEOu2g9JLvTYw3GgQAIzEYgdr0MPQTBreimm2/UMmqcX+MIh+1k7RYFL/O+JY3UpYvVARavwbOxQm4QAAEQSE+gen3jrevZkw9mm9HrG/mhNcZSvSZHBy6MqgY0vSyXq8tai02QxBsKx4LM9MMKJYIACKQmcPzee9rS68CiSY5FuBcGdeu88QqTxVVw7ad7IyFevU5NFeWBAAiAQHoCcc9v3PevE8SvpQWu8rqN0zP5vPNDWJ0RiU4/LlAiCIBAzwkk02uOOOsrirLHuNgyS88VZbMEJqDd5pKmnqPS8x6B+SAAAiDgJ1DjemNlkAWMQQAEQAAEahGoFQ+BXtdii8QgAAJtERj2HIH3v+9dd37wAy476HVb4wnlggAItEeA9PrMqafaK3+BJd9/35ceeviR2fU6Wfx6gSxQNQiAwGAI7O5sDe+dqneg16lIohwQAAEQaInAJJtMqGjodUt8USwIgEBbBPT0MLNtqnQnoZVNFw7MIdZfyfS2ttoWLBd6vRDsqBQEQKA5ATPxt2wesJk6LLON5W4WZdOCK5eAeG+Y0bw90Tmh19GokBAEQKADBFyH2t3j3umTDddr9FyV17m0plNGV8Hd5X5zYAO9ngNkVAECIJCMgNZZo7CyfJqlOXKZtL6hhXvTUF2FdtgrffBkDVYFQa/boIoyQQAE2iWglzS7y5tFTE242ZuS3WftRJcJvXt4aLeRTukp18vgFqZz7jxUBwI9IlC5QJrnX9NkvphGiVPsbujs2nfmbZ3eDZKwautkoubis0uoJD4kQto42/zrteyJB7Ot5xPrNdkUwxppQAAElorAsWMfvuKqGwI3+CQadfXaBahvOWe+FQnWCq61WKd3ywncRjSmH7ur1941PDFNQhoQAIGhEljfOJJcr42f6wqxBKN1Sm+yMpec91dmqey1VHqN+HUlaiQAARDoFgHvRL2Asxy+8OhOLwm0VhcVeT0zITvodUKYKAoEQGAeBGLmX5upe8ZHFivNbBM9w8RtCRcSP/MkOYtW9FrPdCmb9eLu10e5GdvpXgWesUBkBwEQ6AgB1x1290gAxBvQkJ0mY1nJbiGLkuxW9NpcNvVeRXV3uvMcm40POQYuimkzs5ELBEAghoDXIzYeN5cjzrLxtfW3gdKkBJEmbV7YE49pSL00eZG8Fb2uZwdSgwAIgAAIRBCYn157wx1lURF9PHSjK2Uxloj2IgkIgAAI9JXA/PTanFzoUxJ9mdXESdwAv5ybzP/ibF87GXaDAAgMgkD69TI8/1ovIjKTz83Mc29iN7tedOQuQNJ9oS8El10UHkTfoREg0BsCkfOvj997T2+aVNPQWdc3PvlgttnC+saAXnMDy7Q45itXtV1o0OuaAwnJQaB1AjF6ffdHP9a6HQutYIbnga1lreo1iy/HQESmhZWZbeN+1HnNNs/6kL9e/hIq8U5NWWiXoXIQWEYCMXq9jFyyLO55u/t63WL82sx3cSfcyB7uJ/1R5zXbcgwIaLEpeTnHAVoNAiAwMAIt6vV8SLkz3udTL2oBARAAgTkT6L1eu9Pd50wQ1YEACIDAfAgknh/yxje9ZT52oxYQAIF+Eai8P1+/mpPK2lrx65R6TbevTdUGlAMCIDA8AuH7Xw+vvTEtitPr9ezJBxLP54sxDmlAAARAAASEQC297n38Gh0PAiAAAktCAHq9JB2NZoIACPSeAPS6912IBoAACCwJAej1knQ0mgkCINB7AtDr3nchGgACILAkBGrM51sSImgmCIAACMyTwC233xGe6Xj01prz+TC3ep79h7pAAASWikBivV4qdmgsCIAACHSHgPjXiePXciNT8/AX/bFymxPovwacfOU+z7g7iGEJCIAACKQlkEav3UdzmWeT64+ybR7+otNEPhfG+1DktIBQGgiAAAh0hEAavfY2puz+1MZ9Ni6566GLE81Ot5tddnaEKcwAARAAgaQEJlxa7PyQQN2uc20Se4W7zIN2nybDMm2emK6fLxPpjCfFh8JAAARAYE4Ejt6a7vky7nNhzD2ptV8cbp9+tGNlyjmhQjUgAAIg0A0CieMhZRcA9VMcdUzDxDokmX5IowFlHHBz7bEbVGEFCIAACKQnEBsPoZv+uZXfdPONeqd5DK43iCHptey6hehkbugjXBHn9Rqcnh9KBAEQAIHZCESsl2n0fHRjlZ7jrUMZ3oeXa/k2iblY7yQT3m8i4KLXxh6dDAt8ZhtCyA0CIDAPAsfvvactvQ4swvHKsddxDvjdZToe0GsdaQk8MX0e4FEHCIAACNQkEPe8gnTXG7ULzPFo9q+1v6x3GlXVHwMZDQTMCak5KpAcBECg9wQSXG80Wsz6y1NEjGrrne6VSdF6nUxK09cVuXyJophaet8naAAIgAAI+AjUuN5YGWQBYRAAARAAgVoEFhAPqWUfEoMACIAACDQgkCAe0qBWZAEBEAABEKhLAHpdlxjSgwAIgMBiCECvF8MdtYIACIBAXQLQ67rEkH5QBOhqj7wrGyZTVN0NyWsmPpVNXjKzXU3V7toxd0+ltUgwPALQ6+H1KVoURYBl+qGHH5E374nKHEzk3u9sxjLLFvTOWCyy944A9Lp3XQaDExAQpf7hn3uPvFm4vXcyEDc5xs911xa47rOsTtALC2Sb0usazSqEBO1HEf0kAL3uZ7/B6hQESKl1MfTx2LEPewtml5m+KruZu84V6V/rMs1NibkifZdKvXI4RdNRRi8JYL1ML7sNRs9CgJ1rEevvfvl3UWmPPvsVLvNVh66+4qobvLfK0fe3YUllj5hFvNL11skC972R6Mfy3A+nEt0s3d2FvIGuxHqZLnQQbOgHARZreslG2G5RFvkF6g19MwbxkfWGVnwd8ZAQCtdugiQmTtIPsjWtnAz09c/f+xM1SYSSw79OCBNF9YOA9q+1TLOL7fWvjUxr2TWuk9dVdNOIr13meWkv293uB+hoK6mBJNdnTj0VnaMfCe+/70t0JvcLv/ir8K/70WGwsuMEJAwiG16DJdYc0xwTmK502I1zLem1Wx1T7wDS7O5sDemdvEcSX28U58J4GWWzTcPzTCujWpUJkvNCgQMgQM9Fet33vubXf/5T3BZS6pjgtdtwd7TrOAaHNcKa615m1LkCVzgH0AuBJrjxn2Z7uAp9OIwRomZ1zSdmlUavXd2USzGMTH+UbTmprHRAYkYntDuGEtIIAZoKQqEPDcR8rByW7kmunhnCw14rslfxWU10UcaXN6GYwfeg0NCHq1rbOlolvSBCJCJuLvkazrVq5Fr038RylFPZxb80eu0dQ4HAHB/0tCshe9yitNbLoVJ7LpVezOCHOBpYlwC52DQJhN6k0fLmPWUzQ8wvUP/aRQL0+NSenQxRY6eoeVkCkQCpom5Le5e+pVkxdeVoRm4ttSLB9cbKI4nXdK9zzUUZ31zAeS/aRDrpM9LvdXYXURk03u89WzIEtAuj+0WXXLZdVlQYstiW9pegV8cEHnfX6wHQfeOpc/l6IwWvZ/xFJ5SjWbhxK/jKdoLrjbetZU88lG2eSOBfmxicPgeUM7uA+6ChyE9RMpadUeqTpsoemoX7APKaE5TKFsmZnTkx954DGX3XH2U7/AusZV7ZsbyyUWUJSKPl3bgQZExIYMbjcUI5mqVRM7airOoEeq2LduMV/K0+eXRDGXUFV1ytsD8+C+4B52Vo0lPcUtMpkVJrOtd1nEXi9QHbDBJtj0mvUxojB9xBS960umoQwDUfOfIakLAVuvwE8RApzpyxGq/K/ah1XFTDiLtJIwJtKpXfeUuHtWH8hMqCGC5ML8/KIRgf+PLWGIY842nyMHpwqK3Q8ZBUbZxdjma3pIvxEJHasjim22xGac5tw/ourhzXIv6afHRP3mfHPYwSXN9WAHrjVLxTOkij9sap9Bmot8BKITbO/jCwoxXNCFS6BTHFxoiJcRrShtqStMJtaeJ4CLvDYVdIf2vCna59LkQB4Q2VxvTlsqXxXhXgnvJGqGWnqLbrOCc80ywzo6yKZeu+ZWtv2lPkxnI0I/a0rRBj0ui1PtGW0xB9hNE7TUsqT6IDxz0dFk97eJyxt3qXXTvR2tst85eZfOCcxqiwV5QDlHT6Vs+caj2vwNwdu+xm2d79gbxu+pg9vRtjkQbP7pkml6NIy3Wy2VvhrTSBXhst1r9k82s3p9jagTJNdTWd2699czd7S8e0Br3VoywMVmtiWCsTnmmGz8MMw+TH42bPK6D5f/p5NObZNKKznMw0wdxZW390b7qt91BRNGE8ybMUuj8yZ/wVJ5ejZsRmbEVZpSmvNzZrGHLNgYD2OHgk6eN/zGmKScM2ewXXrasscYz0myO0GD/j74EvBJFhd37wA8L/7o9+jLY//olfcSdiG6285fY7dK8dv/ce2kO5XEllneW/nIYyBvTX6LJkJ/nm8mnPHAbMnKugXk41/3rOlpdVx+O2u9cbO4IJZrgEvMEocaJd4XP9a1es+eSGfd5mga9459rEahJ2sRZr1u6y5xWQSrJG01/eII0mAeW/rKEspjoZbbOb7HWf3cScnkvjikTZqaIl8bLlREpOqcW96NGeGf0J+NcJf+Y9K0o7vF7TdahBjzOv/yvxE12U7DTusFud1KWPAZzMVO3uFD/dJK7bH+z1GLGWQtY3jpStSmf3uczn9cYrxLM2Prj2tWWbbRBdZuFmz1oUn7cHthRT+9d1e7PL6ZP714iHdLm7YVsrBJrpNcsxaSspLympFk0JU7CqsjSL6fxR/oYj0WXf6rjK8EIirNeEqJX+XmihadejQ68X2pmofBEEGui1iUEbV1rkuyx+LXrN3rEIulF2hqHTGK3X5SyCXFt1kl6nfQ5LW4Y2Kjfh/UOg1416AJn6TKCBXnNcQmIa+qOILIcyRFLF0daaK9cbvdcntePsXuF0y+lzJ1xku74EMphG6YYEwtn6QnRZ248mvN/TIPmiUQMmwM8r4Nkg5hUIXpuQsXzk20W5RcnOQPiCLznKJUoOp/AcQdqQ/QPuC26avvo9yO1UPZhg/nUqU1AOCMyTAE0FIXXWNZqPMxqjHeSyy4OUhrxmDohTdZxM5o2wARLVHV7YekbCS5gder2EnY4mF5rITycgjZZ34HkF4vOK/8tyzNPsRJq1pIrs6gQGvfjXLNzyrdZ3c+kSnbfMBIYQv45ZoOFdduF2fOSkYJl63NIsy2UekXNue/zzCsyMOtdOLbJmyp3OyxndOXmcxi1E5vPxV26yORNDdWkJ1Ipf91ivvTIdWDLnFdnKCx1eRS47QqTtSJQGAiAweAK19Hpo8ZAyh9esjNIyHbi+IWOFl9jJm/bLojuzum/wwwsNBAEQWBSBvvrXM/rFBre3tMqVfo3DKYvqbNQLAiDQNQJL4V9773Fh7okhLnBlD3ld7Mpc7GXHJEMaEAABEJidwBDiIW6wgrnoO1To8IUOa8QTbJYrvnykBAEQAIEwgSHoNesy+8je1mpnXFLKnTmN3AfU35QfOZkEQxAEQAAEkhDot14HZoO4dDixvhed0W5RfBNXcYviQjCZL8kQRCEgAAKRBPqt19LISgHV8mokO0AqZu6HmWoSyR3JQAAEQKAugR7rtZ4ELXOrjcKyNLu+cIPIhj4kSHUGNy4/1h1/SA8CIBBPoK96rQXaxDHMtBCJgbhxasLkVXNzaVHkXkLeEjE3Ao0ISfzIQ0oQAIG6BPo6/7puO5EeBEAABDpIYCnmX3eQO0wCARAAgVYJ9DUe0ioUFA4CIAACHSQAve5gp8AkEAABEPAQgF5jWIAACIBAPwhAr/vRT7ASBEAABKDXGAMgAAIg0A8C0Ot+9BOsBAEQAAHoNcYACIAACPSDAPS6H/0EK0EABEAAeo0xAAIgAAL9IAC97kc/wUoQAAEQgF5jDIAACIBAPwgkuN8T3a+kH22FlSAAAiCwIAK33H7HyW895lZe635PafT6pptvXBAEVAsCIAACPSBw9cu+s0N6/ca7ToaZ3f+RqykBkgklADEDBkAAZJAawgM7iV4jft2DIzNMBAEQAAEiAL3GMAABEACBfhCAXvejn2AlCIAACECvMQZAAARAoB8EoNf96CdYCQIgAALQa4wBEAABEOgHAeh1P/oJVoIACIAA9BpjAARAAAT6QQB63Y9+gpUgAAIgAL3GGAABEACBfhCAXvejn2AlCIAACECvMQZAAARAoB8EoNf96CdYCQIgAALQa4wBEAABEOgHAeh1P/oJVoIACIAA9BpjAARAAAT6QQDPl+lHP8FKEACBXhNI8ryCBHpNdvSaI4wHARAAgTkQ6MTzwObQTlQBAiAAAoMkUOt5u4hfD3IMoFEgAAIDJAC9HmCnokkgAAKDJAC9HmS3olEgAAIDJAC9HmCnokkgAAKDJAC9HmS3olEgAAJDIpBnk6I50OshdSraAgIgMGQCNeZfDxkD2gYCIAACCyJwy+13eKdmizlHb1vPHn8w2zoRq9dYFLOgrkS1IAACwyeQWK+HDwwtBAEQAIFOEqjtX4dbcfTaVz//3FcpDW2YlLyfX5wskMb9SpcmRUl1uthOcoZR8yNgRoWMN2NB5BgzgzbQDLdenVe2zcjXv4v5MUJN/SSQWK/LfhvuTyU8TPXQD4iy6L4cJDD6+zkOE1sd4zeUyasZewHLvD6H103R9nAujNjEXb4cxYleJ5sfUqmYATckCfOw35SkChTScQIyCGmDt3nDPTOrPMnTGWXblO/WYqrrOC6Y1zsCsdcbYxpWppjGs/AWVRZO4cRe38RbXeVhI6YhSNNrAoFx6I1U6JBFfAJOGR6E+lvEQ3o9qBZrfMp4CA9KN07ttrAywlgZD5G6AikXSxa1L4qAGYfhoFnM2V7lGKsczxoFgiGLGhgDqDdlPCTSpY2PV1BKTiwbrgcUWekAugpNiCQQvrId40+Iy2xGoB6NgWFs5JsLkbcez+7Ajmwjki05gdh4CN2k1SV10803yhD3hgjNzkp/xPhEPMTNJRpJ4+05qdFr8JJ39pybX7kKoIE9dceh14+OCZhUnh3qUz03ceDw4JqEsdpgJAwpS+UvpXY8hG+qbRjJHG+tqiZN2K9xXRIdqg7otfdMU+/EAp/FDujj995TOQobWBgzDhPKMVvoTupwHQs9VsWJ0Q008WspljYwVhuMhMFkifmlHL11LXvyoWwzen1j+CEIZbE5rxwHpNbrO3v960q9Hkx39rQhMU/NaNC0yHEoJbsjsOy0rGysBuLO8cPb6LvX629AA1kGQCDmlyJ6nWA+nxZZE1ZuFmXW06ealTCAXkQTmhHQzrV7+DdDKzz9DlHmZl2AXO0RSKDXcs5oLrDoKy2mATFfuZdr2qOAkgdDQM7GxId1AxHm5IxHmutqiJpXCncggfmqsqjBdAQa0gaBGtcb2whHttEklNkFAjFneQ3sbKnYBpYgCwgkIRAzpFPGQ5IYjUJAAARAAATCBJLFQwAaBEAABECgVQKIh7SKd3kLjznLa0CnpWKNJZhg16Br+p7l/e97150f/MD8WxEzpFPO58Pgnn8fL7zGysEdMwobtKKlYl29PnPqqQbmIUtPCdx/35ceeviRZdFrDO6eDtNmZscM7paEtaVivXq9u7PVjA9y9Y4Ajate6HWy+DUNbryXhEDvfo0wGASGQSCZXg8DB1oBAr0g4K65967CL1sSUTYNvGwpvzAJJNB1UXrzsRdUu28k9DrURzI63XGvs3GycJruDwVY2CMCehGQiK93GZp3SSe1VN+LTWd016kFhNjoPtclGM3HHuHtrKnQ61DXyK/CHfRutpg0nR0HMKx3BEQZRRbN8npZtOk6xVqsWbvdQkz53gRQ5DkPG+h1BfDKG5i4S5nn3IWobpkJlLnG2oMOnPyx4HoLMSVwIW5R5kRTHxuw+D75yIReVyMtCwLy2NU3rEBIpJomUqQgIFKo3V7xlOue/PEYNl62KYSHun4bQddfSWJX9FO0fnnLgF6X9r35SZgxLR9Ftd2hXOmbL++4Q8tnI6CHFoujdmzdb8tqK/OsvaFw40qbWrxhbvHHZ2sucu8TgF6XDoVItXWDgxhcIDBPAizWgeHqPUFkC92LLiZOzclkkAciJ2URcMS4Ew4G6HUsTO/VGwSvY/EhXTsE5CzQBJelNq8iG1uMa+x+61571FovTrTYoN1qRLET9jz0Ogqm/jFodyPSB4+qA4lAoD4BbxSuwTWVgBccM8h1tNAcKljZ67cMOTwEoNexw8L8MGKzIR0ItEbATMZwo9gxzrVEPBDZa62jkhUMvS5FqS/jGAcB/kKyAYiCZiCg/WjxcAOyK3EPdzyLsleGLwIJzFeVRc3Q9CXNCr2u6Hj2WQJXbHT+yqvqSzrK0OwWCJiYso5ClNUmohwwpyyNN4StyymLzMC5Sdj50OtSmO4ANWeX7i8EMZOEQxNFgQAIHBDIs8mEtqHXGBIgAAIg0A8C0Ot+9BOsBAEQAIEEzwOj58vQ8wpwc/flGUwxN3dv6cECLRVr+o6G9PF771meDkVLiUC3n1ewnj3xQLb1fBq9xuBethFfObhbEtaWijXdd/dHP7ZsHYr2EoEOPw8snV5jcC/nWA8P7paEtaVil7MH0eouEIgZ0kdvTafXXWgzbOgagZhR2MDmloptYAmygEASAjFDWvQa1xuTMEchIAACINA6Aeh164hRAQiAAAgkIQC9ToIRhYAACIBA6wRqzA9p3RZUMCwCt9x+x8lvPZa2TTHBvrQ1ojQQaJVAzJCufb2RZqS2ajQKHyQB6PUguxWNSkigFb1OaB+KAoHGBGhwN86LjCDQTQKVZ6KFf/3kA9lm9HqZbrYTVi0bAZznLVuPL0l7w2ei0OslGQZoJgiAQO8JiF5jfkjv+xINAAEQWBIC0Osl6Wg0EwRAoPcEEui19+HK5qFE4WcUMUVJY56y7DI2j4LGU116PwzRABAAgQgCCfQ68iFDAZHlr/TTQvnZiZX243kulYiQAARAYDAEEui1do3FUzaPahZeZQ95k0KMl8375cGdekN/hUc7D2ZEoiEgAAJlBNLotS5dXGMj2ZX+Mks5F8XbXJQ8+Fn284b5WFk+BgEIgAAI9JpAYr1mhRWPWCRbP9k+HMtm2a30lysT9LpXYDwIgAAIuAQS6LW+PKjdXuMXe+mbWIf2r0X6TUYJdks8xMRM0M0gAAIgMEgCM93v6aabb3QjIaKzEtDgNBIncTfcQmSPLk0K8e403YOFy4Mcr2gUCAyPQPV69NvWsicerLEenW9KYkjpNZR6jocotZ7mUanXbohDYiMmNl3meutkWLg8vGGNFoHA8AjQw2/b0mvvIveAUtfSa68Prne6TjftEY2OnAI4vP5Gi0AABPpLIOr+fAf+dYL4tZ7XIQJqgiESEgljlWuVXmkOhE3621uwHARAAAQiCSTQa3aBzcwQuQipoxzudBFzvVEm8Ilwy0VLU6B2q/Xkk8hmIxkIgAAI9I5AjeuNlUGW3jUeBoMACIDAYgnMOx6y2NaidhAAARBYEgJp4iFLAgvNBAEQAIEFEoBeLxA+qgYBEACBGgSg1zVgISkIgAAILJAA9HqB8LteNV0JkXfAVnehU/zdXcpSyn6TQH8s2xZTAwlM+TL7yG2mnpgk05niG9j1PoZ9vSIAve5Vd83LWJbphx5+RN68x1u/vhGjzK3UMzU5lxY7M4/Tq7C8073Lo2ilnh7q3p0xvH7K2Bxzc0deZ2BWG8yrQ1APCBQEMJ8P48ASYKWmvT/8c++R73795z9F2x//xK+EH+Qs0hyjgCziOqV8DKitTmNM997c0Si+ewyoPDCUHaUwdEBgdgJx8/nWp/cPOQH/enbgwyxBizVr97FjHw431V39pJcyVcYQzJIo1x8XYZUN936Q+it9JDCusXaTeVvWarGg81/ZMB8jj0bDHBlo1eIIQK8Xx76TNbNzLWL93S//LnqzpX92/uSZU0+5N9ISUS4TOGlomQS7IquDD1pqG6xlLXPVA3666ZnKI00nexJGDZDAcsVDhn2T1SQLULVei1LTwH/02a/Q31cduvqKq25wQyImjsECZ5zQcEBZ/7ZcfXRjJmUaKp4yF8iV6qrNHv3Rm5gb4q0OXnYqRRz23TTf/7533fnBD5SxqhUPWTq95sjs8F4UrPAqad2WzqjXXonU0hljj1dStZNu5NscG4y2SlDbbIippmT32KMVP/6oE9NSpGECpNd06jZIGvff9yXSHOh1k85lMQqwa1JoN/KsbxxJrtfUMnax2bmmV9i/Dvi8rjhqbK7/G6n73uuTgdJ0sabfXDXXh5mwy9+NIdBjK1ivd3e2etyGEtMrNaeWf50sfq0HtDu4deBSuzNuG01erwS4YdAGYc3hjYwkLaJnBr3ue1/Ds0FYqSvFWuo1M95mnP1m4hjeoSKOdlnIQtumS/BeUawEOGOLKstHAhAIE0im1+bH4J6T6ivys/eKvrSVtuTZbRtACRRdIVdaN8R8DB9oJaBRF4X2l6UQ4wqwNLtxCRMkqTyESznagfDqfqoYiF5/VLZdFsllCK6nUunx6NYFsnt9rED3xfhVdXs/SfrIhpT5fJXDJomRjQtJEL/WgLzDXZ9peoOD5gfD49Jtkvwgw+fdARaV5yaNOS48Y6p4CDeEVUOHFCnYQnvKJl/rbqVkuqcqe41rFG+aO9e9VqnTcJayQaLl1RgmJZta3I96JMsA1r3c4GKjTGwvGy2BixBy9DKHJa9tgd8Oc3ONr9xpEhh7ZjykpY2HuJ0uQLwj0+CasS2mtErNqRUPSaDX8uMxLAIdXPaLqrwiZOrylgO9TnXw0L5ezDKZVPUOtRwzV9JtZuT0G8lYKbJuFWU6K/vD8Mt+497DSXw/ptXrGP0NiHKX9TplPISdFGltWUhRupZPPXQy2VPZ05ySq5PtylxIUIsAabS8a2VE4vYIyIDn8e9qk/5RmJ9G5W9TB+jLto2Hrn+J/FV7ba9VslaGMmh6f3csDzQzjV5zU+WUVnvBoqrSl/pSj2xzdn30DiiydyQ1OD+t1f1IDAILIWB0RH4mZTEN+XXoH5f8+oyKNWiR2MPqr+3RP+EGJSfJIrphQJXZppuQxIBWC0mg1/r0wfWpXXXWQ8cckPVZlR52wto9HvbuCNlqd6Lw4RHQumw0Ouyj6B+m+EPe32MtaFJpNz0kbZU5fWcItRrbocSTCRmTQK/dMVR2ZhE+4xBPnAv0CrHxHZimd2eHQMMUEEhBwJzUm0igdnsD56aRhojjZURfZw/bE1lRq8m4FZVHNcHVqjFJCk+g164dLiYmEgbnnpgETlWkNNejT8IFhYBA1wiYn4P+aM5xvTEKEwmZPVxr/KSuBRb0QUv7f6Zbu2Z2eNS1otfe0xD3tM579Is51rknerMPvq79OGEPCHgJyODXYz7mNF8Lkwh6AHKMc9rlPoo5nLii1OUWpYmHSAvlAC4xMi2+4mJ7T6PkAKhHkjnj02ncg2SM0He8M7pmXuTzZdy7aJXdV0v2x9x4K0maQCGmdZGNXWwfGT+6sZtifqpuo8yvdbGtblC7JuO6j1ygFiIjSg1qnE+WZPOv52PujLVUzl2fsfwFZk+7XoZlTt8bixap0x5are5tI6Xnr1x91FlkaYDe0MWGNbqsCm0SpakUeimH7mhIeY/few9t8F/52MZ88xnnX2ux1l62OImu620uvjEo44yLtOnQYiANK52bIMbHL/uBpJ1/bTi4fLxNENsqI7e1fuaVmhO7XubxB7Kt56HXteB3N3FCvZZlePrGWHd/9GPU+MDzZegnxxpHG6J9zIv2aw3VkkrbnF52smi6L1FV+krSmIr4I1UnK31MAimWTeLEvCF5Y34/zcYBlfzGN70lnDfJTbuambfAXGn1eoENcauGXjfvjkp2zYtedM7keu3exbCyijLHlv1ZreNaRrV0ss6W+bZ8SOByXN5Si2T32iP+vv6W9VrKTHIncdfCyLs8t+HaL3p4VtQPvQ53+tHb1jP41x0fxLXMqxTTyNLChzRvLSx8RpS94QUTBtEmiatbZqcJxXBRnFjq0oOeQzRaIt1k2g0XT5+LXULRjBwhbSSDXkOvPeMK/nXlj62BXlOZWoh1ZEMiJLxhlN0YI4mNCksyE1fxtkW7z9pNFvnWlgRolEXqKwEiQQMC0GvotV+vKwOIDUZbR7IkCX3OqNcsyizZRi6ZklzT09DMNUl9PdAdx96oghtg4brCkRPtm7sHCbjYcxvYZTGuuRnQakVpni+zhPGQyABiq53XauGzS8wseu0VR2qvCZVIwFpLpA46e2MjRtMFoyvu5oDBne5emTQHDBPshn/d6kA1hfPV7AG/Zn0e2K1r2ZMPZZsnlmt+yIAHRMKmlUl2IEQu3nTZxAyJQni12PXExUPX7TKaLiqsr1hyerm26R4GpECJgHvn81Gy2Q9+CTsFRQ2VQMx8pKMHet3K+sahkl2edtGN80mddXvNRxcFO9d8/1Wen0d/+aNX+Eij+a2LYteYdoq3KyWYQqjwMne+ltSaYuUjxHp5RnuPWgq97lFnzclUUkwKhdObNFrevCegYiSy5NWSzsqVPT3PmvfrBrDgas3VlwRZtelbzmiy87f85jQBNG7VktjkrSxqTh2AakCghADiIRgapQRqPV9Gr5fRHq7ZL1+ZawlmJonY5E1mLJY05nBSVrW3cMpbq70YNyCQhECteAj0OglzFAICIAACTQjU0mvEQ5ogRh4QAAEQmD8B6PX8maNGEAABEGhCAHrdhBrygAAIgMD8CUCv588cNYIACIBAEwLQ6ybUkAcEQAAE5k8Aej1/5qgRBEAABJoQgF43oYY8IAACIDBfAhOqDno9X+aoDQRAAASaEoBeNyWHfCAAAiAwXwLQ6/nyRm0gAAIg0JQA9LopOeQDARAAgfkSqHH/kPkahtpAAARAYCkIVD7feXr/6wezzedj9XrwT2ZZinGBRoIACHSSQMXzG+vqdSfbCKNAAARAYPgExL9G/Hr4nY0WggAIDIMA9HoY/YhWgAAIDJ8A9Hr4fYwWggAIDIMA9HoY/YhWgAAIDJdAnmUT+of16MPtYrQMBEBgYATgXw+sQ9EcEACBwRKInX89WABoGAiAQOcJDHv9x/vf9647P/iBQCccvW0te/yhbOsE9LrzQxUGgsDSEyC9PnPqqUFiuP++Lz308CORel07HnL02lcLNb3NOyv3VCbwdomba5A9h0aBAAgECOzubA3vXavHa+t1rdJJZ59/7qtabeUj7eQ3q7z+aPaUpallyfAS4xg2vD5Fi0AgTKBePMTVXyndq8u0U/xu7zZLs3ylPXfeqb/1pozpYCNtUjLn1YaZPTGFp0ojRhqSXpMao0hlLcoBgXkS4HgIOdezV2okxRToalGZRs1uCZfwe1/+/RbjISxw3Cre0B9lpyg7O85ag7Q+Gt9ZI3C9bwbXzK80RrJJ/BYbJE2qnqhVjiAVgdaQm7W6lgFIDALLQMD1LLWICYGyX9xif4k14iGVhmpdNoIubqwRXJ3MPdB5C/EeAMPjrFaWWonbGN/wndugijJBwEvADcZ2GVSsXouI6ECzN+4sXrB2kHmnqLY5iIW9Zl3jLCi1DpYFahr777MYZs4qzAFDTlA0NJ2mXwMuFSiUAwKNCeifjwkSNC5zPhlj9Vpa6A2GGDfZnNqXtUTHH8piEZpmcs/XeLImQjKfDnDPKsx5jA7ahEkm57MQAqgUBFolYHyygLvj9U1bta2y8Fi9dgsKt1Mc6rAF4nR7gy26iuSeb0/DDq7ZHI+rjFZVDgUkAIFlIGDcmjKP0PjdC3bDJ1mW07+m9w/REXodW9BBj7C7Z07zzUUAHjfal+ePqcZTl8XaiyLc8BgfPBU6lAMCAyNgIrfcujIHaLGOUUP/WjxfNxIkfSkNM8FW1iM3AKJ130hzG4zM+YF4qYuScm6jtFSPobBJ+qxtYD8kNAcE5kBA3J2EHmFLZjfUax3qLRNTI9O6AVocWaRc0dGHBAE6y4m/e2jRZwnizi+qz8wpi/c0zSvcCz5Ta2lgolgQmAsBkZQG57VzMfCiSuqtl5m/fagRBEAABJKvl9GRWy9e7RuVbSfpl6j1MgfP223oXycxFIWAAAiAwEIImFP28Cm+jgEsxFqpFHq9WP6oHQRAYK4EAnFRfVHNBCQ7EnWEXs91rKAyEAABEGhMAHrdGB0yggAIgMBcCUCv54oblYEACIBAYwKYH9IYHTKCAAjMiQDNDzl+7z1zqmzu1VTfT/Vgfgj0eu6dgwpBAARqErj7ox+rmaNnySueB0Z6/cSD2dbz0Oue9SvMBQEQWDYCRw/0GvHrZet6tBcEQKCvBKDXfe052A0CILBsBKDXy9bjaC8IgEBfCUCv+9pzsBsEQGDZCECvl63H0V4QAIG+EoBe97XnYDcIgMCyEYBeL1uPo70gAAJ9JQC97mvPwW4QAIFlIwC9XrYeR3tBAAT6SgB63deeg90gAALLRiA//F2PHXnlZWsvv+TMiRcmO5dXtv/8+UOVaZAABEAABEAgDYHNE9mpPy/edP+Q7Ds+Ny00z7JJmtL3S4spLFGNiYopGMS8YqrLI8qaRBQUU05kx00iTMojTIrFVIUypqqqMva/jzE7qvmR9cUkS9W8iF6LHAAxVkd1bqqmRRkUlSiqc2PMjqEdZVG6RGT2apaNs9FOtn06z64e+I2v0oFDSSAAAiCwSAL5o89+ZZH1o24QAAEQAIE4ArjeGMcJqUAABEBg0QT+Pz3NiYewg2bmAAAAAElFTkSuQmCC)

The figure shows a writing device ram process

### 3.6 PC Application sample code

The following code shows how to use dll API write register of target chip

void CDATA::OnWriterg()

{

        int RemLen;

        int send\_rg = 0;

        int send\_off = 0;

        int status;

        char valueByte;

        int TotalBytes = RemLen = GetDlgItem(IDC\_WRITEB)-&gt;GetWindowTextLength()/2;

        char\* TextWrg = (char\*)malloc(TotalBytes\*2+1);

        GetDlgItem(IDC\_WRITEB)-&gt;GetWindowText(TextWrg,TotalBytes\*2+1);

        for(int i=0;i&lt;TotalBytes\*2;i++)

        {

                if((TextWrg[i]&gt;=&#39;0&#39;) &amp;&amp; (TextWrg[i]&lt;=&#39;9&#39;))

                        TextWrg[i] = TextWrg[i] - &#39;0&#39;;

                else if((TextWrg[i]&gt;=&#39;a&#39;) &amp;&amp; (TextWrg[i]&lt;=&#39;f&#39;))

                        TextWrg[i] = TextWrg[i] - &#39;a&#39;+ 0xa;

                else if((TextWrg[i]&gt;=&#39;A&#39;) &amp;&amp; (TextWrg[i]&lt;=&#39;F&#39;))

                        TextWrg[i] = TextWrg[i] - &#39;A&#39;+ 0xa;

                else

                {

                        ::MessageBox(NULL,&quot;输入数字有其他字符!&quot;,&quot;写寄存器&quot;,MB\_ICONEXCLAMATION);

                        return;

                }

        }

        i = 0;

        for(int j=0;j&lt;TotalBytes;j++)

        {

                valueByte = TextWrg[i]&lt;&lt;4 | TextWrg[i+1];

                TextWrg[j] = valueByte;

                i += 2;

        }

        while(RemLen &gt; 0)

        {

                if(RemLen &gt; MAX\_PER\_CTRL\_SEND)

                        send\_rg = MAX\_PER\_CTRL\_SEND;

                else

                        send\_rg = RemLen;

                UsbRom.DataLength = send\_rg;

                UsbRom.buffer = TextWrg;

                UsbRom.ActualLength = 0;

                UsbRom.RamAddr = 0;

                status = AmlUsbWriteRegister(&amp;UsbRom);

                send\_off += send\_rg;

                RemLen -= send\_rg;

        }

        if((status==TRUE) &amp;&amp; !RemLen)

        {

                UpdateData(TRUE);

                GetDlgItem(IDC\_STATUS)-&gt;SetWindowText(&quot;发送成功&quot;);

        }

        else

        {

                UpdateData(TRUE);

                GetDlgItem(IDC\_STATUS)-&gt;SetWindowText(&quot;发送失败&quot;);

        }



}
