from os import read
from tkinter.constants import VERTICAL
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Cancel, Input, Multiline, Submit
import time
# from curses import ascii

sg.ChangeLookAndFeel('BlueMono')
phonelist = []
atcmd=''
atsmd=''
smsdelay = 1
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

window = sg.Window('Spam in the place where I work now...', layout, default_element_size=(40, 1), grab_anywhere=False)
atcmd='AT+CMGS=\"GSM\"'
smsmessage='lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet lorem ipsum dolor sit amet'
print(len(smsmessage))
# if len(smsmessage)>160
info = (smsmessage[:160]) if len(smsmessage) > 160 else smsmessage
print(smsmessage)
print(info)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # if user closes window or clicks cancel
      #     print('closed',values[0], values[1])
          break
    if values [0] != '+639123456789' and values[1] != 'message':
          #disable Blast button
      #     print('values changed')
      #     print(repr(values[0]))
# AT
# AT+CMGF=1
            atsmd=str(values[1])+chr(26)
            phonelist = str(values[0]).splitlines()
            for i in phonelist:
                  atcmd='at+cmgs=' + i +'\r\n'
                  print(repr(atcmd))
                  print(repr(atsmd))
                  # print(repr(ascii.ctrl('z')))
                  time.sleep(smsdelay)
#     else:
      #     pass
      #     print('not closed', values[0], values[1])

window.close()

# event, values = window.read()
# window.close()

# sg.Popup('Title',
#          'The results of the window.',
#          'The button clicked was "{}"'.format(event),
#          'The values are', values)