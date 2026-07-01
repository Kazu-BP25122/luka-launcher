from widgets import *
from position import PositionManager


WIDGET_MAP = {
    "clock": ClockWidget,
    "cpu": CPUWidget,
    "log": LogWidget
}



class WidgetManager:
    def __init__(self, master, json_data, logger, log_widget):
        self.master = master
        self.logger = logger
        self.log = log_widget
        self.pos_manager = PositionManager()

        for widget_data in json_data.get("widgets", []):
            widget_type = widget_data.get("type")

            data = widget_data.copy()
            data.pop("type", None)

            widget_class = WIDGET_MAP.get(widget_type)

            if widget_class:
                instance = widget_class(self.master, data)

                layout = data.get("layout", {})
                
                target_frame = instance.get_frame()
                
                self.pos_manager.place_at(
                    target_frame,
                    row=layout["row"],
                    col=layout["col"],
                    W=layout["W"],
                    H=layout["H"]
                )