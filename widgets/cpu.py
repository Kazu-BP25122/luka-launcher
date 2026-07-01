import customtkinter as tk
import psutil
from .components.utils import run_bg


class CPUWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.cpu_percent_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="white")
        self.cpu_percent_label.pack(pady=(5, 0), fill="both", expand=True)

        self.update_cpu()

    def update_cpu(self):
        def bg_process():
            current_cpu_percent = psutil.cpu_percent(interval=0.1)
            self.cpu_percent_label.configure(text=f"CPU:{current_cpu_percent}%")
        
        run_bg(bg_process)