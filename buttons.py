import os
import customtkinter as tk

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