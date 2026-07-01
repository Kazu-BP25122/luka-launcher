import customtkinter as tk
import psutil
from .components.utils import run_bg


class RAMWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.ram_percent_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="white")
        self.ram_percent_label.pack(pady=(5, 0), fill="both", expand=True)

        self.update_ram()

    def update_ram(self):
        def bg_process():
            current_ram_percent = psutil.virtual_memory().percent
            self.ram_percent_label.configure(text=f"RAM:{current_ram_percent}%")
        
        run_bg(bg_process)