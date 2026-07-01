import customtkinter as tk
import subprocess


class WifiWidget(tk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.ssid_label = tk.CTkLabel(self, text="SSID : ", font=("Helvetica", 16), text_color="white")
        self.ssid_label.pack(pady=(5, 0))

        self.signal_label = tk.CTkLabel(self, text="signal : ", font=("Helvetica", 16), text_color="white")
        self.signal_label.pack(pady=(0, 5))

        self.update_wifi()


    def update_wifi(self):
        ssid = "未接続"
        signal = "--"

        self.response = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"
            )

        for line in self.response.stdout.split("\n"):
            if "SSID" in line and "非表示" not in line and "BSSID" not in line:
                ssid = line.split(":")[1].strip()
            
            if "シグナル" in line or "Signal" in line:
                signal = line.split(":")[1].strip()

        self.ssid_label.configure(text=f"SSID : {ssid}")
        self.signal_label.configure(text=f"signal : {signal}")