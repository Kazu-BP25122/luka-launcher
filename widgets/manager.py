from widgets import *
from .position import PositionManager
import threading

class WidgetManager:
    def __init__(self, master, logger, log_widget):
        self.master = master
        self.logger = logger
        self.log = log_widget
        self.pos_manager = PositionManager()

        #ウィジェットの配置: (widget, 行, 列, 幅,　高)
        #行:0~19, 列:0~23

        self.clock = ClockWidget(master)
        self.pos_manager.place_at(self.clock, 0, 0, 4, 2)

        self.battery = BatteryWidget(master)
        self.pos_manager.place_at(self.battery, 18, 22, 2, 1)

        #self.excange = ExchangeWidget(master, logger=logger)
        #self.excange.pack(pady=10)

        self.wifi = WifiWidget(master)
        self.pos_manager.place_at(self.wifi, 7, 10, 2, 1)
        
        self.cpu = CPUWidget(master)
        self.pos_manager.place_at(self.cpu, 5, 0, 2, 1)

        self.ram = RAMWidget(master)
        self.pos_manager.place_at(self.ram, 6, 0, 2, 1)

        self.pos_manager.place_at(self.log, 3, 4, 3, 3)

        self.bitrate = BitrateWidget(master)
        self.pos_manager.place_at(self.bitrate, 7, 0, 3, 1)

        self.browser_button = DirectButton(master, text="CHROME", path="C:/Program Files/Google/Chrome/Application/chrome.exe", logger=self.logger)
        self.pos_manager.place_at(self.browser_button, 10, 11, 2, 1)

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
        self.battery.update_battery()
        self.cpu.update_cpu()
        self.ram.update_ram()
        self.bitrate.update_Bitrate()
        self.wifi.update_wifi()
        
        self.master.after(5000, self.update_widgets)