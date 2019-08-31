from pynput.keyboard import Key


class MenuKeyboard:
    def __init__(self, renderer, menu_list):
        self.s_index = 0
        self.update_screen = renderer
        self.menu_list = menu_list

    def on_press(self, key):
        if key == Key.up and self.s_index > 0:
            self.s_index -= 1
            self.update_screen.render_menu(self.menu_list, self.s_index)
        if key == Key.down and self.s_index < len(self.menu_list) - 1:
            self.s_index += 1
            self.update_screen.render_menu(self.menu_list, self.s_index)
        if key == Key.enter:
            return False


class DialogKeyboard():
    def __init__(self, renderer, msg):
        self.s_index = 0
        self.msg = msg
        self.update_screen = renderer

    def on_press(self, key):
        if key == Key.left and self.s_index > 0:
            self.s_index -= 1
            self.update_screen.render_dialog(self.msg, self.s_index)
        if key == Key.right and self.s_index == 0:
            self.s_index += 1
            self.update_screen.render_dialog(self.msg, self.s_index)
        if key == Key.enter:
            return False
