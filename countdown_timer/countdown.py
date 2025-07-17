import time
import threading

class Countdown:
    def __init__(self):
        self.time_left = 0
        self.is_running = False
        self.timer_thread = None
        self.on_complete = None

    def set_timer(self, seconds):
        self.time_left = seconds
        if self.timer_thread is not None and self.timer_thread.is_alive():
            self.timer_thread.join()

        self.is_running = True
        self.timer_thread = threading.Thread(target=self._run_timer)
        self.timer_thread.start()

    def _run_timer(self):
        while self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1
        if self.on_complete:
            self.on_complete()

    def set_timer_complete_callback(self, callback):
        self.on_complete = callback
