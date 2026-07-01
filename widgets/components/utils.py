import threading


def run_bg(func):
    threading.Thread(target=func, daemon=True).start()
