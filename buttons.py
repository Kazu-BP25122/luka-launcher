import os
import customtkinter as tk
from popup import GoldPopup

class Button:
    def __init__(self, root, text, path, log_frame):
        self.root = root
        self.text = text
        self.path = path
        self.log_frame = log_frame
        self.make()
    
    def action(self):
        self.log_frame.add_log(f"Open:{self.path}")
        os.startfile(self.path)
    
    def make(self):
        self.btn = tk.CTkButton(self.root,
                                text = self.text,
                                command = self.action)
        self.btn.pack(pady=10)


class FolderOpenButton(Button):
    def __init__(self, root, text, path, log_frame):
        super().__init__(root, text, path, log_frame)
        self.popup = None

    def action(self):
        if self.popup is not None and self.popup.exists():
            print("opening")
            return
        
        self.popup = GoldPopup(self.root, self.path, self.log_frame)
        
        print("window")


class DevelopOpenButton(Button):
    def __init__(self, root, text, path, log_frame):
        super().__init__(root, text, path, log_frame)
        self.popup = None
    
    def action(self):
        if self.popup is not None and self.popup.exists():
            print("opening")
            return

        self.popup = GoldPopup(self.root, self.path, self.log_frame, open_mode="vscode")        
        print("window")