from widgets import *


class WidgetManager:
    def __init__(self, master, logger, log_widget):
        self.master = master
        self.logger = logger
        self.log = log_widget

        self.clock = ClockWidget(master)
        self.clock.pack(pady=10)

        self.battery = BatteryWidget(master)
        self.battery.pack(pady=10)

        self.cpu = CPUWidget(master)
        self.cpu.pack(pady=10)

        self.ram = RAMWidget(master)
        self.ram.pack(pady=10)

        self.log.pack(pady=10)

        self.bitrate = BitrateWidget(master)
        self.bitrate.pack(pady=10)

        self.browser_button = DirectButton(master, text="CHROME", path="C:/Program Files/Google/Chrome/Application/chrome.exe", logger=self.logger)
        self.browser_button.pack(pady=5)

        self.update_widgets()


    def update_widgets(self):
        self.clock.update_clock()
        self.battery.update_battery()
        self.cpu.update_cpu()
        self.ram.update_ram()
        self.bitrate.update_Bitrate()
        
        self.master.after(1000, self.update_widgets)