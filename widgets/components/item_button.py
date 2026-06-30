import customtkinter as tk


class FileItemButton:
    def __init__(self, master, path, action):
        self.path = path
        self.action = action

        file_btn = tk.CTkButton(
            master,
            text=self.path.name,
            anchor="w",
            fg_color="transparent",
            hover_color="#3a3a3a",
            command=lambda: self.open_target(self.path)
        )
        file_btn.pack(fill="x", padx=5, pady=2)

    def open_target(self, target_path):
        self.action(target_path)