import customtkinter as tk
from pathlib import Path

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
        #スクロールバーを配置
        self.scroll_frame = tk.CTkScrollableFrame(self.border, fg_color="transparent")
        self.scroll_frame.pack(fill="both", expand=True, padx=5, pady=5)

        folder_path = Path(self.path)

        for p in folder_path.iterdir():
            btn_text = f"{p.name}"

            file_btn = tk.CTkButton(
                self.scroll_frame,
                text=btn_text,
                anchor="w",
                fg_color="transparent",
                hover_color="#3a3a3a",
                command=lambda path=p: self.open_target(path)
            )
            file_btn.pack(fill="x", padx=5, pady=2)


        #クリック時の判定
        self.bind_id = self.root.bind_all("<Button-1>", self.check_mouse)



    def exists(self):
        return self.window.winfo_exists()

    #マウスが枠外を触ったらウィンドウを削除
    def check_mouse(self, event):
        if not self.exists():
            self.root.unbind("<Button-1>", self.bind_id)
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

            self.root.unbind("<Button-1>", self.bind_id)
    
    def open_target(self, target_path):
        import os
        os.startfile(target_path)
        self.window.destroy()
        self.root.unbind("<Button-1>", self.bind_id)