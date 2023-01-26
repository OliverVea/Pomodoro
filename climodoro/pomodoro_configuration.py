from dataclasses import dataclass

from climodoro.constants import Constants

@dataclass
class PomodoroConfiguration:
    duration: int
    description: str


WORK = PomodoroConfiguration(
    int(Constants.WORK.total_seconds()),
    "Work")

SHORT_BREAK = PomodoroConfiguration(
    int(Constants.SHORT_BREAK.total_seconds()),
    "Short Break")

LONG_BREAK = PomodoroConfiguration(
    int(Constants.LONG_BREAK.total_seconds()),
    "Long Break")

def get_configuration_order() -> list[PomodoroConfiguration]:
    return ([WORK, SHORT_BREAK] * Constants.BREAK_RATIO)[:-1] + [LONG_BREAK]