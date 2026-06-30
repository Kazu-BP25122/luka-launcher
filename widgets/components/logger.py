

class Logger:
    def __init__(self, log_widget):
        self.log_widget = log_widget
    
    def log_info(self, message):
        log_text = f"{message}"
        print(log_text)

        self.log_widget.add_log(log_text)