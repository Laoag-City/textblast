# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port (win), open phone numbers file or paste to control/widget
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent file (text or csv)
# TODO: multithreaded serial comms
import serial, serial.tools.list_ports, PySimpleGUI
        
comports = serial.tools.list_ports.comports()
portinfo = serial.tools.list_ports
#comport = portinfo.grep()
modem = serial.Serial()
modem.baudrate=115200
modem.port = ''
modem.timeout = 1

print(comports)
print(portinfo)
print(modem)