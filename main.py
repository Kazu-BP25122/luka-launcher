import customtkinter as tk
import os
import win32gui
import win32con

from buttons import Button, FolderOpenButton, DevelopOpenButton
from widgets import ClockWidget, CPUWidget, RAMWidget, LogWidget, BitrateWidget, BatteryWidget



#===========ランチャーの初期化====================
root = tk.CTk()
root.title("window")
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
#アプリとして認識されないように設定
root.attributes("-toolwindow", True)
root.update()

#前面に出てこないように設定
hwnd = win32gui.GetParent(root.winfo_id())
current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    current_style | win32con.WS_EX_NOACTIVATE
)

#=============ウィジェットの配置==================
clock = ClockWidget(root)
clock.pack(pady=10)

battery = BatteryWidget(root)
battery.pack(pady=10)

cpu = CPUWidget(root)
cpu.pack(pady=10)

ram = RAMWidget(root)
ram.pack(pady=10)

log = LogWidget(root)
log.pack(pady=10)

bitrate = BitrateWidget(root)
bitrate.pack(pady=10)
#==============基本ボタンの配置===================
browser_btn = Button(root,
                     "CHROME",
                     "C:/Program Files/Google/Chrome/Application/chrome.exe",
                     log)
assignment_btn = FolderOpenButton(root,
                                  "Assignment",
                                  "C:/Users/kazuk/Documents/Assignment",
                                  log)
develop_btn = DevelopOpenButton(root,
                                "Develop",
                                "C:/Users/kazuk/Develop",
                                log)
create_btn = FolderOpenButton(root,
                              "Create",
                              "C:/Users/kazuk/Create",
                              log)
game_btn = FolderOpenButton(root,
                            "Game",
                            "C:/Users/kazuk/Game",
                            log)
trash_btn = Button(root,
                   "Trash",
                   "shell:RecycleBinFolder",
                   log)
setting_btn = Button(root,
                     "Setting",
                     "ms-settings:",
                     log)
#=================キルスイッチ====================
exit_btn = tk.CTkButton(root,
                        text = "EXIT",
                        command = root.destroy)
exit_btn.pack(pady=10)
#================================================



root.state('zoomed')
root.mainloop()