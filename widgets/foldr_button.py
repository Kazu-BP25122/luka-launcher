import customtkinter as tk
import os
from .components import SubWindow
from .components import FileScrollFrame


class FolderButton(tk.CTkFrame):
    def __init__(self, master, text, path, logger, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.master = master
        self.logger = logger
        self.path = path
        self.logger = logger
        
        self.button = tk.CTkButton(
            self,
            text=text,
            command=self.open_folder_window
        )
    
        self.button.pack(expand=True, fill="both")

    def open_folder_window(self):
        self.sub_win = SubWindow(self.master)
        self.open_folder(self.path)

    def open_folder(self, current_path):
        if hasattr(self, "content"):
            self.content.scroll_frame.destroy()

        self.content = FileScrollFrame(
            master=self.sub_win.border,
            path=current_path,
            action=self.normal_action
        )

    def normal_action(self, target_path):
        if target_path.is_dir():
            self.open_folder(target_path)
        else:
            try:
                os.startfile(target_path)
                self.logger.log_info(f"[OPEN] {target_path.name}\n")
            except Exception as e:
                self.logger.log_info(f"[ERROR] {target_path.name}\n")
            
            self.sub_win.window.destroy()