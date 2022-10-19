# Metex Digital Multimeter Software
Scripts and programs that can be used to connect to a Metext M-3850D DMM via RS-232 and periodically read the values of the meter.
It's quite slow, roughly 1 measurement per second ;-).

Note, that a straight cable is required for the serial connection, not a null-modem cable.

## metex.py
Python script that reads the values from the meter.
<img src="https://raw.githubusercontent.com/nerdprojects/metex/main/script.png"/>

## Original Software
The original software is contained in metex-floppy.img. This is a raw copy of the original floppy that came with the multimeter.
It contains two scope programms, one for DOS and one for Windows.

I got them both running under macOS with DOSBox with a Windows 3.1 installation.
You can configure your USB serial device in the DOSBox settings like this:

    serial1=directserial realport:tty.usbserial-AH070BRN

### Digital Multimeter Scope
This is the METEX.EXE DOS program in the folder GRAPHIC.

<img src="https://raw.githubusercontent.com/nerdprojects/metex/main/graphic.png"/>

### ScopeView
This is the METEX.EXE Windows program in the folder SCOPE.

<img src="https://raw.githubusercontent.com/nerdprojects/metex/main/scopeview.png"/>


## Manual
I also have a manual lying around, I can scan it if someones interested.
