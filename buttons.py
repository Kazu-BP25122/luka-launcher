import os
import customtkinter as tk
from popup import GoldPopup

class Button:
    def __init__(self, root, text, path):
        self.root = root
        self.text = text
        self.path = path
        self.make()
    
    def action(self):
        os.startfile(self.path)
    
    def make(self):
        self.btn = tk.CTkButton(self.root,
                                text = self.text,
                                command = self.action)
        self.btn.pack(pady=10)


class FolderOpenButton(Button):
    def __init__(self, root, text, path):
        super().__init__(root, text, path)
        self.popup = None

    def action(self):
        if self.popup is not None and self.popup.exists():
            print("opening")
            return
        
        self.popup = GoldPopup(self.root, self.path)
        
        print("window")


class DevelopOpenButton(Button):
    def __init__(self, root, text, path):
        super().__init__(root, text, path)
        self.popup = None
    
    def action(self):
        if self.popup is not None and self.popup.exists():
            print("opening")
            return

        self.popup = GoldPopup(self.root, self.path, open_mode="vscode")        
        print("window")