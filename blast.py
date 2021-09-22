# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port,
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent logfile (text or csv)
# TODO: multithreaded serial comms
import time, serial, serial.tools.list_ports, PySimpleGUI

theports = serial.tools.list_ports.comports()
modem = serial.Serial()
modem.baudrate=115200
modem.timeout = 1
modem.port = ''
atcmd = 'AT\r\n'
atresp = ''
portdesc = ''

# Test presence of serial GSM modem
# Note: AT commands is terminated with \r\n
# SMS message ends with EOF (^Z) to instruct send
for i in range(len(theports)):
    portdesc=theports[i].description[0:10].lower()
    if portdesc == 'usb-serial':
        modem.port = theports[i].device
        break
modem.open()
modem.write(atcmd.encode())
modem.readline()
time.sleep(5)
atresp = modem.readline().decode()
# print(atresp)
modem.close()
if atresp == 'OK\r\n':
    print('GSM modem is OK')
