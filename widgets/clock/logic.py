import time
from .frame import ClockFrame


class ClockWidget():
    def __init__(self, master, data):
        self.master = master
        props = data.get("props", {})
        
        self.frame = ClockFrame(master, props)

        self.last_sec = time.localtime().tm_sec
        self.update_clock()


    def update_clock(self):
        self.current_time = time.localtime()
        S = self.current_time.tm_sec

        if S != self.last_sec:
            self.frame.update_view(self.current_time)

        self.last_sec = S

        self.master.after(100, self.update_clock)


    def get_frame(self):
        return self.frame