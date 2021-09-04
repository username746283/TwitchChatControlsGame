from pynput import keyboard
import sys
import time

goon = True

exitKey = None

def on_press(key):
    global exitKey
    if exitKey is None:
        print('Exit-Key bound to {0}'.format(key))
        exitKey = key
    else:
        print('key {0} exitKey {1}'.format(key, exitKey))
        if key == exitKey:
            print('end')
            global goon
            goon = False
            quit()
#    try:
#        print('Keypress: {0}   {1}'.format(key.char, key))
#        if key.char == 'p':
#            global goon
#            goon = False
#            quit()
#            #sys.exit(0)
#    except AttributeError:
#        print('Keypress: {0}'.format(key))

listener = keyboard.Listener(on_press=on_press)
listener.start()

while goon:
    print('a')
    time.sleep(1)
