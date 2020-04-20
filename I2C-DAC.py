#!/usr/bin/python3
# This is your python3 interpreter path (console command: which python3)

import smbus2  # The lib for adjusting I2C
from datetime import datetime  # The lib for time checking

max_out = 2700  # The absolute maximum is (2^n - 1), n is DAC's discharge
chip_adr = 0x63  # DAC's I2C address
i2c_folder = '/dev/i2c-2'  # Folder to the 2nd I2C bus file (Debian 9)

port = smbus2.SMBus(bus=i2c_folder)  # I2C port initialization
port.open(i2c_folder)  # Open I2C port

input('\n\n\nEnter any key to start')

print('\nProgram is started. Press Ctrl + C to stop and close the program\n')

try:  # Handling KeyboardInterrupt error

    while True:
        n = int(input('Enter integer number from 0 to ' + str(max_out) + ':   '))
        if n <= max_out:
            first_b = n >> 8  # prepearing for the DAC's I2C protocol
            second_b = n & 0x0ff
            time_0 = datetime.now()
            port.write_byte_data(chip_adr, first_b, second_b)  # Send data via I2C
            time_1 = datetime.now()
            print('Time for sending:', str(time_1 - time_0), '\n')
        else:
            print('You have entered so great number!\n')

except KeyboardInterrupt:  # Handling KeyboardInterrupt error
    port.close()  # Closing port and all files
    print('\n\nProgram is closed\n')
