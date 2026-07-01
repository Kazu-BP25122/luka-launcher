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
        self.pos_manager.place_at(self.clock.get_widget(), 0, 0, 4, 2)

        #self.picture = PictureWidget(master, "C:/Users/kazuk/Pictures/LUKA/1761390_11.jpg")
        #self.pos_manager.place_at(self.picture.get_widget(), 5, 5, 4, 6)

        self.battery = BatteryWidget(master)
        self.pos_manager.place_at(self.battery, 18, 21, 3, 1)

        #self.excange = ExchangeWidget(master, logger=logger)
        #self.excange.pack(pady=10)

        self.wifi = WifiWidget(master)
        self.pos_manager.place_at(self.wifi, 16, 21, 3, 2)
        
        self.cpu = CPUWidget(master)
        self.pos_manager.place_at(self.cpu, 5, 0, 4, 1)

        self.ram = RAMWidget(master)
        self.pos_manager.place_at(self.ram, 6, 0, 4, 1)


        self.pos_manager.place_at(self.log, 0, 18, 6, 4)


        self.bitrate = BitrateWidget(master)
        self.pos_manager.place_at(self.bitrate, 7, 0, 4, 1)

        self.browser_button = DirectButton(master, text="CHROME", path="C:/Program Files/Google/Chrome/Application/chrome.exe", logger=self.logger)
        self.pos_manager.place_at(self.browser_button, 10, 11, 1, 1)

        self.develop_button = DevelopButton(master,text="Develop", path="C:/Users/kazuk/Develop", logger=self.logger)
        self.pos_manager.place_at(self.develop_button, 10, 12, 1, 1)

        self.assignment_button = FolderButton(master,text="Assignment", path="C:/Users/kazuk/Documents/Assignment", logger=self.logger)
        self.pos_manager.place_at(self.assignment_button, 10, 13, 2, 1)

        self.create_button = FolderButton(master,text="Create", path="C:/Users/kazuk/Create", logger=self.logger)
        self.pos_manager.place_at(self.create_button, 11, 11, 1, 1)

        self.game_button = FolderButton(master,text="Game", path="C:/Users/kazuk/Game", logger=self.logger)
        self.pos_manager.place_at(self.game_button, 11, 12, 1, 1)

        self.trash_button = DirectButton(master, text="trash", path="shell:RecycleBinFolder", logger=self.logger)
        self.pos_manager.place_at(self.trash_button, 11, 13, 1, 1)

        self.setting_button = DirectButton(master, text="setting", path="ms-settings:", logger=self.logger)
        self.pos_manager.place_at(self.setting_button, 11, 14, 1, 1)

        self.update_widgets()


    def update_widgets(self):
        self.battery.update_battery()
        self.cpu.update_cpu()
        self.ram.update_ram()
        self.bitrate.update_Bitrate()
        self.wifi.update_wifi()
        
        self.master.after(5000, self.update_widgets)