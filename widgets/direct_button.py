import customtkinter as tk
import os


class DirectButton(tk.CTkFrame):
    def __init__(self, master, text, path, logger, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.logger = logger
        self.path = path

        self.button = tk.CTkButton(
            self,
            text=text,
            command=self.launch
        )

        self.button.pack(expand=True, fill="both")
    
    def launch(self):
        if self.path:
            try:
                os.startfile(self.path)
                self.logger.log_info(f"[OPEN] {self.path}\n")
            except Exception as e:
                self.logger.log_info(f"[ERROR] {self.path}\n{e}")