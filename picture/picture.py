from .design import PictureDesign

class PictureWidget:
    def __init__(self, master, image_path):
        self.master = master
        self.picture_design = PictureDesign(master, image_path)

    def get_widget(self):
        return self.picture_design