import copy
from ctypes import *

STD_OUTPUT_HANDLE = -11


class MainRenderer:
    def __init__(self, width):
        self.width = width
        self.screen_forms = ["#" * width, "#" + " " * (width - 2) + "#"]
        self.win_height = 0

    def render_menu(self, menu, s_index=0):
        height = len(menu)
        this_screen = copy.deepcopy(self.screen_forms)
        for i in range(7):
            this_screen.append(this_screen[1])
        for i in range(height):
            if i == s_index:
                this_screen.append(
                    this_screen[1][:len(this_screen[1]) // 2 - len(menu[i]) // 2 - 2] + "> " + menu[i] + " <"
                    + this_screen[1][len(this_screen[1]) // 2 - len(menu[i]) // 2 + len(menu[i]) + 2:])
            else:
                this_screen.append(this_screen[1][:len(this_screen[1]) // 2 - len(menu[i]) // 2] + menu[i]
                                   + this_screen[1][len(this_screen[1]) // 2 - len(menu[i]) // 2 + len(menu[i]):])
            this_screen.append(this_screen[1])
        for _ in range(7):
            this_screen.append(this_screen[1])
        this_screen.append(this_screen[0])
        self.win_height = len(this_screen)
        render(this_screen)

    def render_dialog(self, msg, s_index=0):
        this_screen = copy.deepcopy(self.screen_forms)
        for i in range((self.win_height - 5) // 2 - 1):
            this_screen.append(this_screen[1])
        this_screen.append('#' + msg.center(self.width - 2) + '#')
        this_screen.append(this_screen[1])
        if s_index == 0:
            line = '> Yes <       No  '
        else:
            line = '  Yes       > No <'
        this_screen.append('#' + line.center(self.width - 2) + '#')
        for i in range((self.win_height - 5) // 2):
            this_screen.append(this_screen[1])
        this_screen.append(this_screen[0])
        render(this_screen)

    def render_loading_screen(self, percentage, current_task):
        this_screen = copy.deepcopy(self.screen_forms)
        for i in range((self.win_height - 5) // 2 - 1):
            this_screen.append(this_screen[1])
        this_screen.append('#' + current_task.center(self.width - 2) + '#')
        this_screen.append(this_screen[1])
        this_screen.append('#' + (str(percentage) + '%').center(self.width - 2) + '#')
        for i in range((self.win_height - 5) // 2):
            this_screen.append(this_screen[1])
        this_screen.append(this_screen[0])
        render(this_screen)

    def render_sim_screen(self, match_day):
        this_screen = copy.deepcopy(self.screen_forms)
        for _ in range((self.win_height - 5) // 2 - 1):
            this_screen.append(this_screen[1])
        pass

    def render_game_screen(self, menu, s_index):
        this_screen = copy.deepcopy(self.screen_forms)
        for _ in range(8):
            this_screen.append(this_screen[1])
        for i in range(len(menu)):
            if i == s_index:
                this_screen.append('#' + ("> " + menu[i] + " <").center(self.width - 2) + '#')
            else:
                this_screen.append('#' + (menu[i]).center(self.width - 2) + '#')
            this_screen.append(this_screen[1])
        for _ in range(8):
            this_screen.append(this_screen[1])
        this_screen.append(this_screen[0])
        self.win_height = len(this_screen)
        render(this_screen)


class COORD(Structure):
    pass


COORD._fields_ = [("X", c_short), ("Y", c_short)]


def render(this_screen):
    for i, line in enumerate(this_screen):
        print_at(1 + i, 0, this_screen[i])
    print_at(0, 0, '')


def print_at(y, x, s):
    h = windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    windll.kernel32.SetConsoleCursorPosition(h, COORD(x, y))
    c = s.encode("cp866")
    windll.kernel32.WriteConsoleA(h, c_char_p(c), len(c), None, None)
