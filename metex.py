#!/usr/bin/env python2
import serial, time

# 1200 baud, 7 data bits, 2 stop bits, no parity, no flow control.
ser = serial.Serial("/dev/tty.usbserial-AH070BRN", 1200, 7, "N", 2, timeout=None)
#ser = serial.Serial("/dev/ttyS0", 1200, 7, "N", 2, timeout=None)

# DTR line must be set to high, RTS line must be set to low.
ser.setDTR(1)
ser.setRTS(0)

while True:
	# The instrument sends back currently displayed measurement each time
	# you send 'D' over the line.
	ser.write('D')

	# This returns 14 characters that show type of measurement, value and
	# unit - for example "DC  0.000   V\n".
	print ser.read(14)
	time.sleep(0.1)
