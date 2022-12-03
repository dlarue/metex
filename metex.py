#from: https://sourceforge.net/p/pythonformetexme-21/code/ci/master/tree/metex.py
# updated for use with python3 and added unix_timestamp:
#sudo apt install python3-pip
#sudo pip3 install pyserial
#usage: python3 ./metex.py -p /dev/ttyS0 [-i n(1)] [-n n(10)] [-t] [-T]
# port setup for ME-11
#    but ME-3850D works if you change the baud to 1200
#    but ME-21 works if you change the baud to 2400

# This script uses a serial port connection to log data from a Metex ME-21 multimeter.
#
# The protocol is very simple: sending a "D" character causes the meter to report the current 
# reading, always 14 charcters.
#
# The serial port setting are 600 baud, no parity, 7 data bits, 2 stop bits (600N72)
# The serial port setting are 1200 baud, no parity, 7 data bits, 2 stop bits (1200N72)
# The serial port setting are 2400 baud, no parity, 7 data bits, 2 stop bits (2400N72)
#
# Also, the meter apparently uses power from the host system to run the RS-232 interface, so
# DTR must be set high, and RTS must be set low.
#

import argparse
import serial
import time
import datetime
from time import sleep

# Default port settings for Metex ME-11


BAUDRATE = 600 # ME-11
#BAUDRATE = 1200 # ME-3850D
#BAUDRATE = 2400 # ME-21
BYTESIZE = serial.SEVENBITS
PARITY = serial.PARITY_NONE
STOPBITS = serial.STOPBITS_TWO
TIMEOUT = 2

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port_name", required = True, help = "name of serial port (e. g. /dev/ttyUSB0)")
parser.add_argument("-i", "--interval", default = 1, type = int, help = "sampling interval in seconds (default is 1)")
parser.add_argument("-n", "--num_samples", default = 10, type = int, help = "Number of samples to collect (default is 10)")
parser.add_argument("-t", "--display_unix_timestamp", action = "store_true", help = "include a timestamp with each sample")
parser.add_argument("-T", "--display_timestamp", action = "store_true", help = "include a timestamp with each sample")

args = parser.parse_args()

# Open the serial port.
port = serial.Serial(port = args.port_name, baudrate = BAUDRATE, parity = PARITY, stopbits = STOPBITS, bytesize = BYTESIZE, timeout = TIMEOUT)

# Set the control lines to provide power to the meter's RS-232 interface.

port.setDTR(True)
port.setRTS(False)

# Delay to allow the interface to settle.
sleep(1)

# Flush the input buffer.  (Sometimes spurious characters will be sent during initailization).
port.flushInput()

# Loop, reading the value from the meter.
for x in range(args.num_samples):
    #print (str(x) + ':')
    port.write(b'D')
    result = port.read(14).strip().decode("utf-8") 
    if args.display_unix_timestamp:
        ts = time.time()
        print (str(ts).ljust(20), end='')
        #print (datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))
    if args.display_timestamp:
        ts = time.time()
        #print (str(ts).ljust(20), end='')
        print (datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'), end=' ')
    if len(result) == 13:
        print (result)
    else:
        print ("Error")
    if x < (args.num_samples - 1):          # Skip the last interval delay, useful when long intervals are selected.
        sleep(args.interval)

# Close the serial port.
port.close()
