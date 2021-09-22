from tkinter.constants import VERTICAL
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Input, Multiline

sg.ChangeLookAndFeel('GreenTan')

# ------ Menu Definition ------
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]
#------- Home Layout ------
layout = [[
    [sg.Menu(menu_def, tearoff=False)],
    sg.Frame('Blast to',[[
          sg.Multiline(default_text='+6391234567890',size=(15,20)),
    ]]),
    sg.Frame('Message',[[
          sg.Multiline(default_text='message',size=(20,5)),
          sg.Submit(button_text='Blast!',disabled=True)
    ]])
]]

window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)
event, values = window.read()
window.close()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)