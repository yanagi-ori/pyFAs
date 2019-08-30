import copy
import os
import sys

from pynput.keyboard import Key
from pynput.keyboard import Listener

import keyboard
import render

os.system("cls")

print("tech demo")


class MenuKeyboard(keyboard.MenuKeyboard):
    def __init__(self):
        self.s_index = 0
        self.update_screen = render.MainRenderer()

    def on_press(self, key):
        if key == Key.up and self.s_index > 0:
            self.s_index -= 1
            self.update_screen.render(menu_screen, menu_list, self.s_index)
        if key == Key.down and self.s_index < len(menu_list) - 1:
            self.s_index += 1
            self.update_screen.render(menu_screen, menu_list, self.s_index)
        if key == Key.enter:
            if self.s_index == 0: start_game()
            if self.s_index == 1: load_game()
            if self.s_index == 2: settings()
            if self.s_index == 3: main.close_window()


class Menu:
    def __init__(self, menu):
        self.menu_list = menu

    def main_menu(self):
        global menu_screen
        menu_screen = copy.deepcopy(def_screen_construct)
        main_menu_renderer = render.MainRenderer()
        main_menu_renderer.render(menu_screen, self.menu_list)
        this_keyboard = MenuKeyboard()
        this_keyboard.s_index = 0
        with Listener(on_press=this_keyboard.on_press, on_release=this_keyboard.on_release) as listener:
            listener.join()

    def close_window(self):
        sys.exit()


def start_game(): pass


def load_game(): pass


def settings(): pass


def_screen_construct = ["########################################################################",
                        "#                                                                      #"]
menu_screen = []
menu_list = ['New Game', 'Load Game', 'Settings', 'Exit']
if __name__ == '__main__':
    main = Menu(menu_list)
