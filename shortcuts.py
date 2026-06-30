import os
import customtkinter as tk

from folder import FolderWindow
from develop import DevelopWindow


class ShortcutButtons:
    def __init__(self, master, logger):
        self.master = master
        self.logger = logger

        
        self.chrome_btn = tk.CTkButton(
            self.master, text="CHROME",
            command=lambda: self.launch("C:/Program Files/Google/Chrome/Application/chrome.exe")
        )
        
        self.trash_btn = tk.CTkButton(
            self.master, text="Trash",
            command=lambda: self.launch("shell:RecycleBinFolder")
        )
        
        self.setting_btn = tk.CTkButton(
            self.master, text="Setting",
            command=lambda: self.launch("ms-settings:")
        )

        
        self.assignment_btn = tk.CTkButton(
            self.master, text="Assignment",
            command=lambda: FolderWindow(self.master, "C:/Users/kazuk/Documents/Assignment", self.logger)
        )
        
        self.develop_btn = tk.CTkButton(
            self.master, text="Develop",
            command=lambda: DevelopWindow(self.master, "C:/Users/kazuk/Develop", self.logger)
        )
        
        self.create_btn = tk.CTkButton(
            self.master, text="Create",
            command=lambda: FolderWindow(self.master, "C:/Users/kazuk/Create", self.logger)
        )
        
        self.game_btn = tk.CTkButton(
            self.master, text="Game",
            command=lambda: FolderWindow(self.master, "C:/Users/kazuk/Game", self.logger)
        )

        self.pack_all()

    def launch(self, path):
        self.logger.log_info(f"open : {path}")
        os.startfile(path)

    def pack_all(self):

        buttons = [
            self.chrome_btn,
            self.trash_btn,
            self.setting_btn,
            self.assignment_btn,
            self.develop_btn,
            self.create_btn,
            self.game_btn
        ]

        for btn in buttons:
            btn.pack(
                padx=10,
                pady=6,
                ipadx=10,
                ipady=4
            )