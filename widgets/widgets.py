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


class LogWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.log_box = tk.CTkTextbox(self, width=300, height=150, font=("Consolas", 12))
        self.log_box.pack(padx=10, pady=10, fill="both", expand=True)

    def add_log(self, message):
        self.log_box.configure(state="normal")
        self.log_box.insert("end", f"{message}\n")
        self.log_box.see("end")
        self.log_box.configure(state="disabled")


class BitrateWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        net_io = psutil.net_io_counters()
        self.last_sent = net_io.bytes_sent
        self.last_recv = net_io.bytes_recv
        
        self.download_speed_label = tk.CTkLabel(self, text="0 [KBit/s]", font=("Helvetica", 16), text_color="white")
        self.download_speed_label.pack(pady=(5, 0))
        self.upload_speed_label = tk.CTkLabel(self, text="0 [KBit/s]", font=("Helvetica", 16), text_color="white")
        self.upload_speed_label.pack(pady=(5, 0))
        
        self.update_Bitrate()
        
    def update_Bitrate(self):
        current_io = psutil.net_io_counters()
        download_speed = (current_io.bytes_recv - self.last_recv) / 1000
        upload_speed = (current_io.bytes_sent - self.last_sent) / 1000

        self.last_recv = current_io.bytes_recv
        self.last_sent = current_io.bytes_sent

        self.download_speed_label.configure(text=f"download : {download_speed} [KBit/s]")
        self.upload_speed_label.configure(text=f"upload : {upload_speed} [KBit/s]")
        self.after(1000, self.update_Bitrate)


class BatteryWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.battery_percent_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="white")
        self.battery_percent_label.pack(pady=(5, 0))
        self.update_battery()

    def update_battery(self):
        battery_percent = psutil.sensors_battery().percent
        self.battery_percent_label.configure(text=f"Battery : {battery_percent}%")
        self.after(1000, self.update_battery)