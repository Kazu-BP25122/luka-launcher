import customtkinter as tk


class PositionManager:
    def __init__(self, total_row=20, total_col=24):
        self.total_col = total_col
        self.total_row = total_row

    def place_at(self, widget, row, col, width, height):
        rel_x = col / self.total_col
        rel_y = row / self.total_row

        rel_w = width / self.total_col
        rel_h = height / self.total_row

        widget.place(
            relx=rel_x, rely=rel_y,
            relw= rel_w, relh=rel_h
        )