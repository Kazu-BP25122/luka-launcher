import customtkinter as tk

class GoldPopup:
    def __init__(self, root, path):
        self.root = root
        self.path = path
        
        #サブウィンドウを生成
        self.window = tk.CTkToplevel()
        self.window.overrideredirect(True)
        self.window.geometry("300x400+400+300")
        self.window.attributes("-topmost", True)
        #枠線を配置
        self.border = tk.CTkFrame(self.window, corner_radius=10, border_width=2, border_color="gold")
        self.border.pack(fill="both", expand=True, padx=0, pady=0)

        #クリック時の判定
        self.root.bind_all("<Button-1>", self.check_mouse)
    
    def exists(self):
        return self.window.winfo_exists()

    #マウスが枠外を触ったらウィンドウを削除
    def check_mouse(self, event):
        if not self.exists():
            self.root.unbind_all("<Button-1>")
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

            self.root.unbind_all("<Button-1>")