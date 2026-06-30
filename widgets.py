import customtkinter as tk
import time
import psutil

class ClockWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.date_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="gray")
        self.date_label.pack(pady=(5, 0))

        self.clock_label = tk.CTkLabel(self, text="", font=("Helvetica", 40, "bold"), text_color="gold")
        self.clock_label.pack(pady=(0, 5))

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y/%m/%d")
        self.date_label.configure(text=current_date)
        self.clock_label.configure(text=current_time)
        self.after(1000, self.update_clock)


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

