import time
import PySimpleGUI as sg

        
def step_print():
    sg.theme('LightBlue')   # Add a touch of color

    layout = [  [sg.Text(size=(10,1))],
                [sg.Text('Button menu, select the option: ')],
                [sg.Text('')],
                [sg.Button('Option: 1'), sg.Button('Option: 2'), sg.Button('Option: 3')],
                [sg.Text('')],
                [sg.Button('Cancel')]]

# Create the Window
    window = sg.Window('hi there :)', layout)
    window2_active = False
# Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        # print a text in a new window for every button 
        if event == 'Option: 1':
            window2_active = True
            layout2 = [ [sg.Text('')],
                        [sg.Text('You chose option: 1')],
                        [sg.Text(size=(10,1))],
                        [sg.Button('Exit')]]

            window2 = sg.Window('Thanks', layout2)

            if window2_active:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'Exit':
                    window2.close()
        if event == 'Option: 2':
            window2_active = True
            layout2 = [ [sg.Text('')],
                        [sg.Text('You chose option: 2')],
                        [sg.Text(size=(10,1))],
                        [sg.Button('Exit')]]

            window2 = sg.Window('Thanks', layout2)

            if window2_active:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'Exit':
                    window2.close()
        if event == 'Option: 3':
            window2_active = True
            layout2 = [ [sg.Text('')],
                        [sg.Text('You chose option: 3')],
                        [sg.Text(size=(10,1))],
                        [sg.Button('Exit')]]

            window2 = sg.Window('Thanks', layout2)

            if window2_active:
                event2, values2 = window2.read()
                if event2 == sg.WIN_CLOSED or event2 == 'Exit':
                    window2.close()


        
if __name__ == "__main__":
    step_print()