import customtkinter as tk
import subprocess
from .components import SubWindow
from .components import FileScrollFrame


class DevelopButton(tk.CTkFrame):
    def __init__(self, master, text, path, logger, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.master = master
        self.logger = logger
        self.path = path
        self.logger = logger
        
        self.button = tk.CTkButton(
            self,
            text=text,
            command=self.open_develop_window
        )
    
        self.button.pack(expand=True, fill="both")

    def open_develop_window(self):
        self.sub_win = SubWindow(self.master)
        self.content = FileScrollFrame(
            master=self.sub_win.border,
            path=self.path,
            action=self.vscode_action
        )

    def vscode_action(self, target_path):
        try:
            subprocess.Popen(["code", str(target_path)], shell=True)
            self.logger.log_info(f"[OPEN] {target_path.name}")
        except Exception as e:
            self.logger.log_info(f"[ERROR] {target_path.name}")
            
        self.sub_win.window.destroy()