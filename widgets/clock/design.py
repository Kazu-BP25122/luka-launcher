import customtkinter as tk


class ClockDesign(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.date_label = tk.CTkLabel(self, text="", font=("Helvetica", 16), text_color="gray")
        self.date_label.pack(pady=(5, 0), fill="both", expand=True)

        self.clock_label = tk.CTkLabel(self, text="", font=("Helvetica", 40, "bold"), text_color="gold")
        self.clock_label.pack(pady=(0, 5))

    def update_view(self, current_date, current_time):
        self.date_label.configure(text=current_date)
        self.clock_label.configure(text=current_time)