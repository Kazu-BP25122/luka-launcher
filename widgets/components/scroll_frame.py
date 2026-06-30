import customtkinter as tk
from pathlib import Path
from .item_button import FileItemButton


class FileScrollFrame:
    def __init__(self, master, path, action):
        self.master = master
        self.folder_path = Path(path)
        
        self.scroll_frame = tk.CTkScrollableFrame(self.master, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

        for p in self.folder_path.iterdir():
            FileItemButton(master=self.scroll_frame, path=p, action=action)