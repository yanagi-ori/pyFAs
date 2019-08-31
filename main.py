import os
import sys

from pynput.keyboard import Listener

from keyboard import *
from render import *

os.system("cls")

print("tech demo")


class Menu:
    def __init__(self, x=72):
        self.width = x
        self.menu_renderer = MainRenderer(self.width)
        self.choice = 0

    def main_menu(self, menu):
        os.system("cls")
        self.menu_renderer.render_menu(menu)
        this_keyboard = MenuKeyboard(self.menu_renderer, menu_list)
        with Listener(on_press=this_keyboard.on_press) as self.menu_listener:
            self.menu_listener.join()

        if this_keyboard.s_index == 0:
            self.menu_listener.stop()
            main.start_game()
        if this_keyboard.s_index == 1:
            main.load_game()
        if this_keyboard.s_index == 2:
            main.settings()
        if this_keyboard.s_index == 3:
            self.menu_listener.stop()
            main.close_window()

    def close_window(self):
        msg = "Вы действительно хотите выйти?"
        self.menu_renderer.render_dialog(msg)
        dialog_keyboard = DialogKeyboard(self.menu_renderer, msg)
        with Listener(on_press=dialog_keyboard.on_press) as self.dialog_listener:
            self.dialog_listener.join()
        if dialog_keyboard.s_index == 0:
            sys.exit()
        if dialog_keyboard.s_index == 1:
            self.dialog_listener.stop()
            main.main_menu(menu_list)


def start_game(): pass


def load_game(): pass


def settings(): pass


menu_list = ['New Game', 'Load Game', 'Settings', 'Exit']
if __name__ == '__main__':
    main = Menu(x=72)
    main.main_menu(menu_list)
