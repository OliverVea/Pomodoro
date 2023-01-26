import datetime

class Constants:
    """Class that holds the constants for the Pomodoro Technique"""

    WORK_MINUTES: int = 15
    """The duration of a work period in minutes"""
    WORK: datetime.timedelta = datetime.timedelta(minutes=WORK_MINUTES)
    """The datetime.time object representing the duration of a work period"""

    SHORT_BREAK_MINUTES: int = 5
    """The duration of a short break period in minutes"""
    SHORT_BREAK: datetime.timedelta = datetime.timedelta(minutes=SHORT_BREAK_MINUTES)
    """The datetime.time object representing the duration of a short break period"""
    
    LONG_BREAK_MINUTES: int = 20
    """The duration of a long break period in minutes"""
    LONG_BREAK: datetime.timedelta = datetime.timedelta(minutes=LONG_BREAK_MINUTES)
    """The datetime.time object representing the duration of a long break period"""

    BREAK_RATIO: int = 3
    """The ratio of short breaks to long breaks, i.e. the number of short breaks that should be taken before a long break"""
