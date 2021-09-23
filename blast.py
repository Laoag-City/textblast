# Text blast app by eihcek https://kechie.github.io
# Enumerate and open serial port,
# input sms message and generate random delay ranging from 5 to 60 seconds between sends
# open a sent logfile (text or csv)
# TODO: multithreaded serial comms
import time, serial, serial.tools.list_ports, PySimpleGUI as sg

# ------ Menu Definition ------
menu_def = [['&File', ['&Open', '&Save', 'E&xit']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
#------- Home Layout ------
layout = [[
#     [sg.Menu(menu_def, tearoff=False)],
    sg.Frame('Blast to',[[
          sg.Multiline(default_text='+639123456789',size=(15,20)),
    ]]),
    sg.Frame('Message',[
          [sg.Multiline(default_text='message',size=(20,5))],
          [sg.Button(button_text='Blast!'),sg.Button('Exit')]
    ])
]]

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


# print(theports)
# Test presence of serial GSM modem
# Note: AT commands and replies is terminated with \r\n
# SMS message ends with EOF (^Z) to instruct send
# TODO: us pyserial in_waiting() method
for i in range(len(theports)):
    portdesc=theports[i].description[0:10].lower()
    # print(portdesc)
    if portdesc != 'usb-serial':
        continue
    if portdesc == 'usb-serial':
        modem.port = theports[i].device
        modem.open()
        modem.write(atcmd.encode())
        modem.readline()
        time.sleep(5)
        atresp = modem.readline().decode()
        modem.close()
    if atresp == 'OK\r\n':
        print('GSM modem is OK')
        window = sg.Window('Spam in the place where I work now...', layout, default_element_size=(40, 1), grab_anywhere=False)
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
                # print('closed',values[0], values[1])
                break
            if values [0] != '+639123456789' and values[1] != 'message':
                print('values changed')
                print(repr(values[0]))
                phonelist = str(values[0]).splitlines()
                for i in phonelist:
                    print(i)
            else:
                print('not closed', values[0], values[1])
                window.close()
    else:
        # window = sg.Window('Spam in the place where I work now...', layout, default_element_size=(40, 1), grab_anywhere=False)
        sg.Popup('Error', 'No GSM modem')
        window.close()
        break