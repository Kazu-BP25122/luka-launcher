import customtkinter as tk
import time


class ClockWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.date_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="gray")
        self.date_label.pack(pady=(5, 0), fill="both", expand=True)

        self.clock_label = tk.CTkLabel(self, text="", font=("Helvetica", 40, "bold"), text_color="gold")
        self.clock_label.pack(pady=(0, 5))

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y/%m/%d")
        self.date_label.configure(text=current_date)
        self.clock_label.configure(text=current_time)

        self.after(500, self.update_clock)