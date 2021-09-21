# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port (win), open phone numbers file or paste to control/widget
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent file (text or csv)
# TODO: multithreaded serial comms
import PySimpleGUI
import serial

simcom = serial.Serial()
simcom.baudrate=115200
simcom.port = ''
simcom.timeout = 1
winports = simcom.tools.list_ports()
print (winports)