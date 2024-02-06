# texteffect.py (1/23/2024)
# Added -option setting on 2/2/2024

import sys
import time

typing_delay = None

# type_text() is supposed to be like a cooler print() function
def type_text(text, end='\n', delay=0.03):

    if typing_delay != None:
        delay = typing_delay
        
    for char in text:
        print(char, end='', flush=True)
        time.sleep(float(delay)) # Note: This is the first time I have ever casted something into a float in Python
        
    print(end, end='')


while True:

    type_text('Give text a typing effect')
    type_text('Type -options for settings')
    type_text('Type -exit to quit', end='\n\n')
    type_text('Enter some text: ', end='')
    text = input()
    text = text.strip()
    print() # Just an empty line

    if text == '-options' or text == '-o':
        print    ('===================================== \n')
        type_text('Welcome to Options', end='\n\n')
        type_text('1. Change typing speed', end='\n\n')
        
        type_text('Type -home to return to the main menu')
        type_text('Type -exit to quit', end='\n\n')
        
        while True:
            option = input('You: ')
            option = option.replace(' ', '')
            
            if option == '1':
            
                type_text(f'Change typing speed (currently {str(typing_delay)}): ', end='')
                new_delay = input()
                
                try:
                    new_delay = float(new_delay)
                    typing_delay = new_delay
                    print('Typing speed changed successfully.')
                except:
                    pass
                    
            elif option == '-home' or option == '-h':
                break
            elif option == '-exit' or option == '-e':
                exit()
            
    elif text == '-exit' or text == '-e':
        type_text('Exiting now...')
        time.sleep(0.5)
        break
    else:
        type_text(text, end='\n\n')

