import customtkinter as tk
import psutil
from .components.utils import run_bg


class BitrateWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        net_io = psutil.net_io_counters()
        self.last_sent = net_io.bytes_sent
        self.last_recv = net_io.bytes_recv
        
        self.download_speed_label = tk.CTkLabel(self, text="0 [KBit/s]", font=("Helvetica", 16), text_color="white")
        self.download_speed_label.pack(pady=(5, 0), fill="both", expand=True)
        self.upload_speed_label = tk.CTkLabel(self, text="0 [KBit/s]", font=("Helvetica", 16), text_color="white")
        self.upload_speed_label.pack(pady=(5, 0), fill="both", expand=True)
        
        self.update_Bitrate()
        
    def update_Bitrate(self):
        def bg_process():

            current_io = psutil.net_io_counters()
            download_speed = (current_io.bytes_recv - self.last_recv) / 1000
            upload_speed = (current_io.bytes_sent - self.last_sent) / 1000

            self.last_recv = current_io.bytes_recv
            self.last_sent = current_io.bytes_sent

            self.download_speed_label.configure(text=f"download : {download_speed} [KBit/s]")
            self.upload_speed_label.configure(text=f"upload : {upload_speed} [KBit/s]")
        
        run_bg(bg_process)