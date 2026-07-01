from PIL import Image, ImageTk
import customtkinter as tk

class PictureDesign(tk.CTkFrame):
    def __init__(self, master, image_path, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        self.image_path = image_path
        
        self.image_label = tk.CTkLabel(self, text="")
        self.image_label.pack(fill="both", expand=True)
        
        self.bind("<Configure>", self.load_and_resize_image)

    def load_and_resize_image(self, event=None):
        max_width = self.winfo_width()
        max_height = self.winfo_height()
        

        if max_width <= 1 or max_height <= 1:
            return


        img = Image.open(self.image_path)
        
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)
        
        ctk_img = tk.CTkImage(light_image=img, dark_image=img, size=(img.width, img.height))
        self.image_label.configure(image=ctk_img)