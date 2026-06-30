import customtkinter as tk
from pathlib import Path


class SubWindow:
    def __init__(self, master):
        self.master = master

        #サブウィンドウを生成
        self.window = tk.CTkToplevel()
        self.window.overrideredirect(True)
        self.window.geometry("300x400+400+300")
        self.window.attributes("-topmost", True)

        #枠線を配置
        self.border = tk.CTkFrame(self.window, corner_radius=10, border_width=2, border_color="gold")
        self.border.pack(fill="both", expand=True, padx=0, pady=0)

        self.bind_id = self.master.bind_all("<Button-1>", self.check_mouse)

    #枠外のクリックで閉じる
    def check_mouse(self, event):
        if not self.exists():
            self.master.unbind("<Button-1>", self.bind_id)
            return

        mx = self.window.winfo_pointerx()
        my = self.window.winfo_pointery()
        
        wx = self.window.winfo_rootx()
        wy = self.window.winfo_rooty()
        ww = self.window.winfo_width()
        wh = self.window.winfo_height()
        
        if not (wx <= mx <= wx + ww and wy <= my <= wy + wh):
            print("destroy")
            self.window.destroy()
            
            self.master.unbind("<Button-1>", self.bind_id)
    
    #存在判定
    def exists(self):
        return self.window.winfo_exists()


class FileScrollFrame:
    def __init__(self, master, path, action):
        self.master = master
        self.folder_path = Path(path)
        
        self.scroll_frame = tk.CTkScrollableFrame(self.master, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for p in self.folder_path.iterdir():
            FileItemButton(master=self.scroll_frame, path=p, action=action)


class FileItemButton:
    def __init__(self, master, path, action):
        self.path = path
        self.action = action

        file_btn = tk.CTkButton(
            master,
            text=self.path.name,
            anchor="w",
            fg_color="transparent",
            hover_color="#3a3a3a",
            command=lambda: self.open_target(self.path)
        )
        file_btn.pack(fill="x", padx=5, pady=2)

    def open_target(self, target_path):
        self.action(target_path)


class Logger:
    def __init__(self, log_widget):
        self.log_widget = log_widget
    
    def log_info(self, message):
        log_text = f"{message}"
        print(log_text)

        self.log_widget.add_log(log_text)