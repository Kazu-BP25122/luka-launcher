import customtkinter as tk
import psutil


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