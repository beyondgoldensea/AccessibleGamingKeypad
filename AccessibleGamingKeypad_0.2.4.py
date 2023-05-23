import json
import time
import tkinter as tk
from pynput.keyboard import Controller, Key
import win32gui, win32con
import sys
import os

# 获取当前执行文件的路径
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

# 使用这个路径构建配置文件的路径
config_path = os.path.join(application_path, 'config.json')

class KeyboardButton(tk.Button):
    def __init__(self, master, key, x, y, script=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.key = key
        self.keyboard = Controller()
        self.script = script
        self.place(x=x, y=y)

    def press_key(self, event):
        if self.script:
            self.script(self.keyboard)
        if isinstance(self.key, tuple):
            for key in self.key:
                self.keyboard.press(key)
        else:
            self.keyboard.press(self.key)

    def release_key(self, event):
        if isinstance(self.key, tuple):
            for key in self.key:
                self.keyboard.release(key)
        else:
            self.keyboard.release(self.key)

def make_script(actions_config):
    def script(keyboard):
        for action_config in actions_config:
            action = action_config["action"]
            keys = action_config["keys"]
            delay = action_config.get("delay", 0) / 1000

            for key in keys:
                if action == "press":
                    keyboard.press(key)
                elif action == "release":
                    keyboard.release(key)

                if delay:
                    time.sleep(delay)

    return script

# Load configuration
with open(config_path) as f:
    config = json.load(f)

window_config = config['window']
height = window_config['window_height']
width = window_config['window_width']
w_x = window_config['window_x']
w_y = window_config['window_y']

def update_geometry():
    geometry_string = f"{width}x{height}+{w_x}+{w_y}"
    root.geometry(geometry_string)

root = tk.Tk()
root.title('My Non-Focusable Keyboard')
update_geometry()
root.overrideredirect(True)

# Prepare the scripts
scripts = {name: make_script(config) for name, config in config["scripts"].items()}

def get_key(key_str):
    if key_str == "up":
        return Key.up
    elif key_str == "down":
        return Key.down
    elif key_str == "left":
        return Key.left
    elif key_str == "right":
        return Key.right
    else:
        return key_str

# Create buttons
for button_config in config['buttons']:
    keys = button_config['keys']
    x, y = button_config['position']
    script_name = button_config['script']
    script = scripts.get(script_name)
    btn_text = keys if isinstance(keys, str) else '+'.join(keys) if isinstance(keys, list) else keys.name
    btn = KeyboardButton(root, get_key(button_config["keys"]), button_config["position"][0], button_config["position"][1], script, text=btn_text, bg='white')
    btn.bind('<Button-1>', btn.press_key)
    btn.bind('<ButtonRelease-1>', btn.release_key)

# 添加一个关闭按钮
close_button = tk.Button(root, text='X', command=root.destroy)
close_button.pack(anchor='ne', padx=10, pady=10)

def set_no_focus():
    hwnd = win32gui.FindWindow(None, 'My Non-Focusable Keyboard')
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_NOACTIVATE)

root.after(1, set_no_focus)

# 使窗口可移动
def start_move(event):
    root.x = event.x_root
    root.y = event.y_root

def stop_move(event):
    root.x = None
    root.y = None

def do_move(event):
    dx = event.x_root - root.x
    dy = event.y_root - root.y
    root.geometry(f"+{root.winfo_x() + dx}+{root.winfo_y() + dy}")

root.bind("<ButtonPress-1>", start_move)
root.bind("<ButtonRelease-1>", stop_move)
root.bind("<B1-Motion>", do_move)

root.mainloop()