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

        #self.excange = ExchangeWidget(master, logger=logger)
        #self.excange.pack(pady=10)

        self.wifi = WifiWidget(master)
        self.wifi.pack(pady=10)
        
        self.cpu = CPUWidget(master)
        self.cpu.pack(pady=10)

        self.ram = RAMWidget(master)
        self.ram.pack(pady=10)

        self.log.pack(pady=10)

        self.bitrate = BitrateWidget(master)
        self.bitrate.pack(pady=10)

        self.browser_button = DirectButton(master, text="CHROME", path="C:/Program Files/Google/Chrome/Application/chrome.exe", logger=self.logger)
        self.browser_button.pack(pady=5)

        self.develop_button = DevelopButton(master,text="Develop", path="C:/Users/kazuk/Develop", logger=self.logger)
        self.develop_button.pack(pady=5)

        self.assignment_button = FolderButton(master,text="Assignment", path="C:/Users/kazuk/Documents/Assignment", logger=self.logger)
        self.assignment_button.pack(pady=5)

        self.create_button = FolderButton(master,text="Create", path="C:/Users/kazuk/Create", logger=self.logger)
        self.create_button.pack(pady=5)

        self.game_button = FolderButton(master,text="Game", path="C:/Users/kazuk/Game", logger=self.logger)
        self.game_button.pack(pady=5)

        self.trash_button = DirectButton(master, text="trash", path="shell:RecycleBinFolder", logger=self.logger)
        self.trash_button.pack(pady=5)

        self.setting_button = DirectButton(master, text="setting", path="ms-settings:", logger=self.logger)
        self.setting_button.pack(pady=5)

        self.update_widgets()


    def update_widgets(self):
        self.clock.update_clock()
        self.battery.update_battery()
        self.cpu.update_cpu()
        self.ram.update_ram()
        self.bitrate.update_Bitrate()
        self.wifi.update_wifi()
        
        self.master.after(1000, self.update_widgets)