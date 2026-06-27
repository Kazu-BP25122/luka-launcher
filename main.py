import customtkinter as tk
import os

def open(path):
    print(f"Open :{path}")
    os.startfile(path)


root = tk.CTk()

root.title("window")
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}+0+0")

browser = tk.CTkButton(root,
                       text = "CHROME",
                       command = lambda: open("C:/Program Files/Google/Chrome/Application/chrome.exe"))
browser.pack(pady=10)

assignment = tk.CTkButton(root,
                          text = "Assignment",
                          command = lambda: open("C:/Users/kazuk/Documents/Assignment"))
assignment.pack(pady = 10)

develop = tk.CTkButton(root,
                    text = "Develop",
                    command = lambda: open("C:/Users/kazuk/Develop"))
develop.pack(pady = 10)

create = tk.CTkButton(root,
                    text = "Create",
                    command = lambda: open("C:/Users/kazuk/Create"))
create.pack(pady = 10)

game = tk.CTkButton(root,
                    text = "Game",
                    command = lambda: open("C:/Users/kazuk/Game"))
game.pack(pady = 10)

trash = tk.CTkButton(root,
                     text = "Trash",
                     command = lambda: open("shell:RecycleBinFolder"))
trash.pack(pady=10)

setting = tk.CTkButton(root,
                       text = "Setting",
                       command = lambda: open("ms-settings:"))
setting.pack(pady=10)

exit = tk.CTkButton(root,
                    text = "EXIT",
                    command = root.destroy)
exit.pack(pady=10)

root.mainloop()