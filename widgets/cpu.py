import customtkinter as tk
import psutil


class CPUWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.cpu_percent_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="white")
        self.cpu_percent_label.pack(pady=(5, 0))

        self.update_cpu()

    def update_cpu(self):
        current_cpu_percent = psutil.cpu_percent(interval=None)
        self.cpu_percent_label.configure(text=f"CPU:{current_cpu_percent}%")

        self.after(1000, self.update_cpu)