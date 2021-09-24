# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port,
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent logfile (text or csv)
# TODO: multithreaded serial comms, progressbar, check if sim is inserted
import re
import sys, time, serial, serial.tools.list_ports, PySimpleGUI as sg

theports = serial.tools.list_ports.comports()
modem = serial.Serial()
modem.baudrate=115200
modem.timeout = 1
modem.port = ''
atcmd = 'AT\r\n'
atresp = ''
portdesc = ''
phonelist = []
smsinput = ''
senddelay = 10
defaultnum='+639123456789'
defaultsms='message'

# ------ Menu Definition ------
menu_def = [['&File', ['&Open', '&Save', 'E&xit']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
#------- Home Layout ------
layout = [[
#     [sg.Menu(menu_def, tearoff=False)],
    sg.Frame('Blast to',[[
          sg.Multiline(default_text=defaultnum,size=(15,20)),
    ]]),
    sg.Frame('Message',[
          [sg.Multiline(default_text=defaultsms,size=(20,5))],
          [sg.Button(button_text='Blast!'),sg.Button('Exit')]
    ])
]]

window = sg.Window('Spam in the place where I work now...', layout, default_element_size=(40, 1), grab_anywhere=False)

# Test presence of serial GSM modem
# TODO: us pyserial in_waiting() method
# check for the serial port that accepts AT commands
for i in range(len(theports)):
    portdesc=theports[i].description[0:10].lower()
    print(portdesc)
    if portdesc != 'usb-serial':
        continue
    if portdesc == 'usb-serial':
        modem.port=theports[i].device
        print(modem.port)
        break

if modem.port == '':
    print('No GSM Modem')
    sg.Popup('Error', 'No GSM modem')
    modem.close()
    window.close()
    sys.exit()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        print('clicked x',values[0], values[1])
        modem.close()
        break
    if values [0] != '+639123456789' and values[1] != 'message':
        # TODO: Throw an exception if port error
        print('values changed')
        smsinput=str(values[1]) + chr(26) + '\r\n'
        smsinput=smsinput.encode()
        # print(smsinput)
        phonelist = str(values[0]).splitlines()
        modem.open()
        modem.write(atcmd.encode())
        time.sleep(1)
        print(repr(modem.readline()))
        # init modem to full functionality
        atcmd='AT+CFUN=1\r\n'
        modem.write(atcmd.encode())
        time.sleep(0.1)
        print(repr(modem.readline()))
        atcmd='AT+CMGF=1\r\n'
        modem.write(atcmd.encode())
        print(repr(modem.readline()))
        time.sleep(0.1)
        atcmd='AT+CSCS=\"GSM\"\r\n'
        modem.write(atcmd.encode())
        print(repr(modem.readline()))
        time.sleep(0.1)
        # print(repr(modem.readline()))
        # time.sleep(1)
        # atresp = modem.readline().decode()
        # print(repr(atresp))
        for i in phonelist:
            # Note: AT commands and replies is terminated with \r\n
            # SMS message ends with (^Z) to instruct send
            atcmd='AT+CMGS=\"' + str(i) +'"\r\n'
            print(repr(atcmd))
            modem.write(atcmd.encode())
            print(repr(modem.readline()))
            time.sleep(1)
            modem.write(smsinput)
            print(repr(smsinput))
            print(repr(modem.readline()))
            time.sleep(senddelay-1)
            #TODO: randomize senddelay
    else:
        print('values not changed', values[0], values[1])