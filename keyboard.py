from pynput.keyboard import Key


class MenuKeyboard:
    def on_press(self, key):
        if key == Key.up:
            return True
        #print('{0} pressed'.format(key))

    def on_release(self, key):
        #print('{0} release'.format(key))
        if key == Key.esc:
            # Stop listener
            return False
