from widgets import *


class WidgetManager:
    def __init__(self, master):
        self.master = master

        self.clock = ClockWidget(master)
        self.clock.pack(pady=10)

        self.battery = BatteryWidget(master)
        self.battery.pack(pady=10)

        self.cpu = CPUWidget(master)
        self.cpu.pack(pady=10)

        self.ram = RAMWidget(master)
        self.ram.pack(pady=10)

        self.log = LogWidget(master)
        self.log.pack(pady=10)

        self.bitrate = BitrateWidget(master)
        self.bitrate.pack(pady=10)

        self.update_widgets()


    def update_widgets(self):
        self.clock.update_clock()
        self.battery.update_battery()
        self.cpu.update_cpu()
        self.ram.update_ram()
        self.bitrate.update_Bitrate()
        
        self.master.after(1000, self.update_widgets)