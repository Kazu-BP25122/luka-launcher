import os
import customtkinter as tk

class Button:
    def __init__(self, root, text, path):
        self.root = root
        self.text = text
        self.path = path
        self.make()
    
    def action(self):
        os.startfile(self.path)
    
    def make(self):
        self.btn = tk.CTkButton(self.root,
                                text = self.text,
                                command = self.action)
        self.btn.pack(pady=10)


class FolderOpenButton(Button):
    def __init__(self, root, text, path):
        super().__init__(root, text, path)
        self.sub_window = None

    def action(self):
        if (self.sub_window is not None and self.sub_window.winfo_exists()):
            print("opening")
            return

        #サブウィンドウを生成
        window = tk.CTkToplevel()
        self.sub_window = window
        window.overrideredirect(True)
        window.geometry("300x400+400+300")
        window.attributes("-topmost", True)
        
        border = tk.CTkFrame(window, corner_radius=10, border_width=2, border_color="gold")
        border.pack(fill = "both", expand = True, padx=0, pady=0)

        def check_mouse(event):
            if not window.winfo_exists():
                self.root.unbind_all("<Button-1>")
                return


            mx = window.winfo_pointerx()
            my = window.winfo_pointery()
            

            wx = window.winfo_rootx()
            wy = window.winfo_rooty()
            ww = window.winfo_width()
            wh = window.winfo_height()
            
            if not (wx <= mx <= wx + ww and wy <= my <= wy + wh):
                print("destroy")
                window.destroy()
            
                self.root.unbind_all("<Button-1>")


        self.root.bind_all("<Button-1>", check_mouse)

        print("window")