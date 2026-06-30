import subprocess
from widgets.components import SubWindow
from widgets.components import FileScrollFrame


class DevelopWindow:
    def __init__(self, master, path, logger):
        self.logger = logger
        self.sub_win = SubWindow(master)

        def vscode_action(target_path):
            subprocess.Popen(["code", str(target_path)], shell=True)
            self.logger.log_info(f"open : {target_path.name}")
            self.sub_win.window.destroy()

        self.content = FileScrollFrame(
            master=self.sub_win.border,
            path=path,
            action=vscode_action
        )