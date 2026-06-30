import customtkinter as tk
import win32gui
import win32con

from widgets.manager import WidgetManager
from shortcuts import ShortcutButtons
from widgets import LogWidget
from widgets.components import Logger

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
log = LogWidget(root)
logger = Logger(log_widget=log)

widgets = WidgetManager(root, logger=logger, log_widget=log)

#==============基本ボタンの配置===================
shortcuts = ShortcutButtons(root, logger)
#=================キルスイッチ====================
exit_btn = tk.CTkButton(root,
                        text = "EXIT",
                        command = root.destroy)
exit_btn.pack(pady=10)
#================================================



root.state('zoomed')
root.mainloop()