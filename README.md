# Beaglebone-black_I2C-DAC
This repository contains code for DAC adjusting via I2C on BeagleBone Black controller.

## Description
The BeagleBone Black System doesn't include DAC, but it may be needed in some projects. So this repository contains simple code for DAC adjusting. I2C is used for data transmission.

DAC -- MCP4725 (12-bit, High-Speed Mode available). Arduino shield with MCP4725 is used (https://amperka.ru/product/troyka-dac-screw-terminal)

## Find and test your I2C device
You could find your I2C Devices using the console command:

```
i2cdetect
```

Read the man i2cdetect to know about it. If all right, you will see the same:

![i2cdetect](https://github.com/dmt0768/Beaglebone-black_I2C-DAC/blob/editing/images/2020-04-20_11-03-17.png)

My I2C device's number is 63, and on the picture, you can see the device's answer on the i2cdetect command: "63".

To test your I2C device working, you need to send some data. It's important to know the DAC's I2C protocol (see your DAC manual).

Use the next command:

```
i2cset
```

In result you'll see the same:

![i2cset](https://github.com/dmt0768/Beaglebone-black_I2C-DAC/blob/editing/images/2020-04-20_11-52-39.png)

With DAC you could see the result using an oscilloscope, ADC, or just LED.

## Using
The Python file gives a simple example of I2C using and provides fast sending a data. The smbus2 packege is used.

### 1) Preparation

  You should have the recent pip3 version. You could upgrade it by command:

```
  pip3 install --upgrade pip
```

  Then install smbus2 packege:

```
  pip3 install smbus2
```

### 2) Download program from GitHub:

```
  git clone https://github.com/dmt0768/Beaglebone-black_I2C-DAC.git
```

### 3) Open and edit file as you need 
The Python file has plenty of comments so it's not hard to figure out
