import os
def clear():
    if os.name == 'nt':
        os.system('CLS')
    else: 
        os.system('clear')