import msvcrt
import threading
import time

from climodoro.callback import Callback

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class InputManager(metaclass=Singleton):
    def __init__(self, sleep_duration: float = 0.05):
        """
        Initializes the class for managing inputs.
        """
        self.sleep_duration = sleep_duration
        self.on_pause = Callback()
        self.on_skip = Callback()
        self.on_quit = Callback()
        self.running = False
        self.thread = None
    
    def __str__(self):
        return '[q] Quit | [p] Pause | [s] Skip'

    def start_input_thread(self):
        """
        Start the input thread which will wait for user input and trigger the corresponding callbacks
        """
        self.running = True
        if not self.thread:
            self.thread = threading.Thread(target=self._input_thread_target)
            self.thread.start()

    def stop_input_thread(self):
        """
        Stop the input thread
        """
        self.running = False
        if self.thread:
            self.thread.join()

    def _input_thread_target(self):
        while self.running:
            if msvcrt.kbhit():
                key = msvcrt.getch()
                if key == b'q':
                    self.on_quit()
                    self.running = False
                elif key == b'p':
                    self.on_pause()
                elif key == b's':
                    self.on_skip()
            time.sleep(self.sleep_duration)