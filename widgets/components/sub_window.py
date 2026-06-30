import customtkinter as tk


class SubWindow:
    def __init__(self, master):
        self.master = master

        #サブウィンドウを生成
        self.window = tk.CTkToplevel()
        self.window.overrideredirect(True)
        self.window.geometry("300x400+400+300")
        self.window.attributes("-topmost", True)

        #枠線を配置
        self.border = tk.CTkFrame(self.window, corner_radius=10, border_width=2, border_color="gold")
        self.border.pack(fill="both", expand=True, padx=0, pady=0)

        self.bind_id = self.master.bind_all("<Button-1>", self.check_mouse)

    #枠外のクリックで閉じる
    def check_mouse(self, event):
        if not self.exists():
            self.master.unbind("<Button-1>", self.bind_id)
            return

        mx = self.window.winfo_pointerx()
        my = self.window.winfo_pointery()
        
        wx = self.window.winfo_rootx()
        wy = self.window.winfo_rooty()
        ww = self.window.winfo_width()
        wh = self.window.winfo_height()
        
        if not (wx <= mx <= wx + ww and wy <= my <= wy + wh):
            print("destroy")
            self.window.destroy()
            
            self.master.unbind("<Button-1>", self.bind_id)
    
    #存在判定
    def exists(self):
        return self.window.winfo_exists()