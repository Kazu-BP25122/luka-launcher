import time
from .design import ClockDesign


class ClockWidget():
    def __init__(self, master):
        self.master = master
        self.clock_design = ClockDesign(master)
        self.update_clock()

    def update_clock(self):
        self.current_time = time.strftime("%H:%M:%S")
        self.current_date = time.strftime("%Y/%m/%d")
        self.clock_design.update_view(self.current_date, self.current_time)
        self.master.after(500, self.update_clock)
    
    def get_widget(self):
        return self.clock_design