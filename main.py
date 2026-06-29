import customtkinter as tk
import os
import win32gui
import win32con

from buttons import Button


root = tk.CTk()

root.title("window")
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")
#アプリとして認識されない設定
root.attributes("-toolwindow", True)

#基本ボタンの配置
browser_btn = Button(root,
                     "CHROME",
                     "C:/Program Files/Google/Chrome/Application/chrome.exe")

assignment_btn = Button(root,
                        "Assignment",
                        "C:/Users/kazuk/Documents/Assignment")

develop_btn = Button(root,
                     "Develop",
                     "C:/Users/kazuk/Develop")

create_btn = Button(root,
                    "Create",
                    "C:/Users/kazuk/Create")

game_btn = Button(root,
                  "Game",
                  "C:/Users/kazuk/Game")

trash_btn = Button(root,
                   "Trash",
                   "shell:RecycleBinFolder")

setting_btn = Button(root,
                     "Setting",
                     "ms-settings:")


#============キルスイッチ====================
exit_btn = tk.CTkButton(root,
                        text = "EXIT",
                        command = root.destroy)
exit_btn.pack(pady=10)
#===========================================


root.update()
#前面に出てこないように設定
hwnd = win32gui.GetParent(root.winfo_id())
current_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
win32gui.SetWindowLong(
    hwnd,
    win32con.GWL_EXSTYLE,
    current_style | win32con.WS_EX_NOACTIVATE
)


root.mainloop()