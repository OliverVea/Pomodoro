import time
import typer

from climodoro.input import InputManager
from climodoro.pomodoro_configuration import PomodoroConfiguration

class Pomodoro:
    def __init__(self, sample_period: float = 0.05):
        self._reset()

        self.sample_period = sample_period

        self.input_manager = InputManager(0.05)
        
        self.input_manager.on_pause.register(self.on_pause)
        self.input_manager.on_quit.register(self.on_quit)
        self.input_manager.on_skip.register(self.on_skip)
    
    def _reset(self):
        self.quit = False
        self.skip = False
        self.paused = False

    def on_skip(self):
        self.skip = True

    def on_quit(self):
        self.quit = True

    def on_pause(self):
        self.paused = not self.paused
        if self.paused:
            typer.echo("\nPaused!")
        else:
            typer.clear()
            print(self.input_manager)

    def run(self, config: PomodoroConfiguration):
        self._reset()
        typer.clear()
        print(self.input_manager)
        self.input_manager.start_input_thread()
        with typer.progressbar(length=config.duration*1000, label=config.description) as progress_bar:
            while not (progress_bar.finished or self.skip or self.quit):

                time.sleep(self.sample_period)
                if not self.paused:
                    progress_bar.update(self.sample_period * 1000)