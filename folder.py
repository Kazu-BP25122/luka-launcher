import customtkinter as tk
from widgets.components import SubWindow
from widgets.components import FileScrollFrame


class FolderWindow:
    def __init__(self, master, path, logger):
        self.master = master
        self.logger = logger

        self.sub_win = SubWindow(master)

        self.open_folder(path)
    
    def open_folder(self, current_path):
        if hasattr(self, "content"):
            self.content.scroll_frame.destroy()
    
        def normal_action(target_path):
            if target_path.is_dir():
                self.open_folder(target_path)
            else:
                self.logger.log_info(f"open : {target_path.name}")
                import os
                os.startfile(target_path)
                self.sub_win.window.destroy()

        self.content = FileScrollFrame(
            master=self.sub_win.border,
            path=current_path,
            action=normal_action
        )