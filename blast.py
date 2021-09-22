# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port (win), open phone numbers file or paste to element/widget
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent logfile (text or csv)
# TODO: multithreaded serial comms
import time, serial, serial.tools.list_ports, PySimpleGUI

theports = serial.tools.list_ports.comports()
modem = serial.Serial()
modem.baudrate=115200
modem.timeout = 1
modem.port = ''
atcmd = 'AT\r'
atresp = ''
portdesc = ''

# Test presence of serial GSM modem
for i in range(len(theports)):
    portdesc=theports[i].description[0:10].lower()
    if portdesc == 'usb-serial':
        modem.port = theports[i].device
        break
# 2 send at command
# 3 check response
modem.open()
print('open')
cmd="AT\n"
modem.write(cmd.encode())
modem.readline()
time.sleep(5)
atresp = modem.readline().decode()
print(atresp)
modem.close()