import copy
import os
import sys

from pynput.keyboard import Key
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


menu_list = ['New Game', 'Load Game', 'Settings', 'Exit']
if __name__ == '__main__':
    main = Menu(x=72)
    main.main_menu(menu_list)
