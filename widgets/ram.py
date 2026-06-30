import customtkinter as tk
import psutil


class RAMWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.ram_percent_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="white")
        self.ram_percent_label.pack(pady=(5, 0))

        self.update_ram()

    def update_ram(self):
        current_ram_percent = psutil.virtual_memory().percent
        self.ram_percent_label.configure(text=f"RAM:{current_ram_percent}%")

        self.after(1000, self.update_ram)