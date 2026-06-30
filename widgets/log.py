import customtkinter as tk


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