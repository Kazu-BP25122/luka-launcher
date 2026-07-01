import customtkinter as tk
import threading
import urllib.request
import json

#memo-後でやる
#yfinanceを使用し、毎秒更新できるPro版ウィジェットの作成

class ExchangeWidget(tk.CTkFrame):
    def __init__(self, master, logger, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.logger = logger

        self.label = tk.CTkLabel(self, text="USD/JPY : ...", font=("Helvetica", 16), text_color="gray")
        self.label.pack(pady=(5, 0))

        self.update_exchange()

    
    def update_exchange(self):
        thread = threading.Thread(target=self.fetch_rate_bg, daemon=True)
        thread.start()

        self.after(10000, self.update_exchange)
    

    def fetch_rate_bg(self):
        url = "https://open.er-api.com/v6/latest/USD"

        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read().decode())

                jpy_rate = data["rates"]["JPY"]

                self.label.configure(text=f"USD/JPY : {jpy_rate:.2f}")

        except Exception as e:
            self.logger.log_info(f"[ERROR] failed getting exchange_data")
        
