"""
GPIO definitions for Amlogic Meson GXL SoCs
Ref:
Linux kernel 4.19.y (hardkernel)
    linux/include/dt-bindings/gpio/meson-gxl-gpio.h

"""

import re
import gpiod
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

chip0 = gpiod.Chip("0")
chip1 = gpiod.Chip("1")

if chip0.num_lines() < 20:
    aobus = 0
    periphs = 1
    periphs_offset = chip1.num_lines() - 11
else:
    aobus = 1
    periphs = 0
    periphs_offset = chip0.num_lines() - 11

chip0.close()
chip1.close()

GPIOAO_0 = Pin((aobus, 0))
GPIOAO_1 = Pin((aobus, 1))
GPIOAO_2 = Pin((aobus, 2))
GPIOAO_3 = Pin((aobus, 3))
GPIOAO_4 = Pin5 = Pin((aobus, 4))
GPIOAO_5 = Pin3 = Pin((aobus, 5))
GPIOAO_6 = Pin12 = Pin((aobus, 6))
GPIOAO_7 = Pin((aobus, 7))
GPIOAO_8 = Pin((aobus, 8))
GPIOAO_9 = Pin13 = Pin((aobus, 9))
GPIO_TEST_N = Pin15 = Pin((aobus, 10))


#define GPIOZ_0         0
#define GPIOZ_1         1
#define GPIOZ_2         2
#define GPIOZ_3         3
#define GPIOZ_4         4
#define GPIOZ_5         5
#define GPIOZ_6         6
#define GPIOZ_7         7
#define GPIOZ_8         8
#define GPIOZ_9         9
#define GPIOZ_10        10
#define GPIOZ_11        11
#define GPIOZ_12        12
#define GPIOZ_13        13
#define GPIOZ_14        14
#define GPIOZ_15        15


GPIOH_0 = Pin((periphs, 16 + periphs_offset))
GPIOH_1 = Pin((periphs, 17 + periphs_offset))
GPIOH_2 = Pin((periphs, 18 + periphs_offset))
GPIOH_3 = Pin((periphs, 19 + periphs_offset))
GPIOH_4 = Pin((periphs, 20 + periphs_offset))
GPIOH_5 = Pin((periphs, 21 + periphs_offset))
GPIOH_6 = Pin((periphs, 22 + periphs_offset))
GPIOH_7 = Pin((periphs, 23 + periphs_offset))
GPIOH_8 = Pin((periphs, 24 + periphs_offset))
GPIOH_9 = Pin((periphs, 25 + periphs_offset))

#define BOOT_0          26
#define BOOT_1          27
#define BOOT_2          28
#define BOOT_3          29
#define BOOT_4          30
#define BOOT_5          31
#define BOOT_6          32
#define BOOT_7          33
#define BOOT_8          34
#define BOOT_9          35
#define BOOT_10         36
#define BOOT_11         37
#define BOOT_12         38
#define BOOT_13         39
#define BOOT_14         40
#define BOOT_15         41
#define CARD_0          42
#define CARD_1          43
#define CARD_2          44
#define CARD_3          45
#define CARD_4          46
#define CARD_5          47
#define CARD_6          48
#define GPIODV_0        49
#define GPIODV_1        50
#define GPIODV_2        51
#define GPIODV_3        52
#define GPIODV_4        53
#define GPIODV_5        54
#define GPIODV_6        55
#define GPIODV_7        56
#define GPIODV_8        57
#define GPIODV_9        58
#define GPIODV_10       59
#define GPIODV_11       60
#define GPIODV_12       61
#define GPIODV_13       62
#define GPIODV_14       63
#define GPIODV_15       64
#define GPIODV_16       65
#define GPIODV_17       66
#define GPIODV_18       67
#define GPIODV_19       68
#define GPIODV_20       69
#define GPIODV_21       70
#define GPIODV_22       71
#define GPIODV_23       72
#define GPIODV_24       73
#define GPIODV_25       74
#define GPIODV_26       75
#define GPIODV_27       76
#define GPIODV_28       77
#define GPIODV_29       78

GPIOX_0 = Pin22 = Pin((periphs, 79 + periphs_offset))
GPIOX_1 = Pin26 = Pin((periphs, 80 + periphs_offset))
GPIOX_2 = Pin36 = Pin((periphs, 81 + periphs_offset))
GPIOX_3 = Pin38 = Pin((periphs, 82 + periphs_offset))
GPIOX_4 = Pin40 = Pin((periphs, 83 + periphs_offset))
GPIOX_5 = Pin37 = Pin((periphs, 84 + periphs_offset))
GPIOX_6 = Pin33 = Pin((periphs, 85 + periphs_offset))
GPIOX_7 = Pin35 = Pin((periphs, 86 + periphs_offset))
GPIOX_8 = Pin19 = Pin((periphs, 87 + periphs_offset))
GPIOX_9 = Pin21 = Pin((periphs, 88 + periphs_offset))
GPIOX_10 = Pin24 = Pin((periphs, 89 + periphs_offset))
GPIOX_11 = Pin23 = Pin((periphs, 90 + periphs_offset))
GPIOX_12 = Pin8 = Pin((periphs, 91 + periphs_offset))
GPIOX_13 = Pin10 = Pin((periphs, 92 + periphs_offset))
GPIOX_14 = Pin16 = Pin((periphs, 93 + periphs_offset))
GPIOX_15 = Pin18 = Pin((periphs, 94 + periphs_offset))
GPIOX_16 = Pin32 = Pin((periphs, 95 + periphs_offset))
GPIOX_17 = Pin29 = Pin((periphs, 96 + periphs_offset))
GPIOX_18 = Pin31 = Pin((periphs, 97 + periphs_offset))
GPIOCLK_0 = Pin7 = Pin((periphs, 98 + periphs_offset))
GPIOCLK_1 = Pin((periphs, 99 + periphs_offset))

# UART 0
UART1_TX = GPIOAO_0
UART1_RX = GPIOAO_1

# UART 1
UART2_TX = GPIOX_12
UART2_RX = GPIOX_13

# ordered as uartId, txId, rxId
uartPorts = ((1, UART1_TX, UART1_RX),
             (2, UART2_TX, UART2_RX),)


I2C0_SDA = GPIOAO_5
I2C0_SCL = GPIOAO_4

i2cPorts = (
    (0, I2C0_SCL, I2C0_SDA),
)


SPI0_SCLK = GPIOX_11
SPI0_MISO = GPIOX_9
SPI0_MOSI = GPIOX_8
SPI0_CS0 = GPIOX_10

# ordered as spiId, sckId, mosiId, misoId
spiPorts = ((0, SPI0_SCLK, SPI0_MOSI, SPI0_MISO),)

