import customtkinter as tk


class ClockFrame(tk.CTkFrame):
    def __init__(self, master, props, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.props = props
        self.clock_label = tk.CTkLabel(self, text="", font=(props["font"], props["text_size"], "bold"), text_color=props["text_color"])
        self.clock_label.pack(expand=True)


    def update_view(self, current_time):

        H = current_time.tm_hour
        M = current_time.tm_min
        S = current_time.tm_sec

        if self.props["show_seconds"] == 1:
            self.clock_label.configure(text=f"{H}:{M}:{S}")
        else:
            self.clock_label.configure(text=f"{H}:{M}")