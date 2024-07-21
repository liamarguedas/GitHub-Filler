from datetime import datetime, timedelta
from win32api import GetSystemTime, SetSystemTime


class DateChanger:
    """todo"""

    def __init__(self, starting_date: tuple, ending_date: tuple):
        """
        date format = (year, month, day)
        NOTE: ending_date cannot be future, maximum today.
        """
        self.starting_date = datetime(*starting_date)
        self.ending_date = datetime(*ending_date)
        self.current_iteration_day = self.starting_date
        self.current_system_date = datetime.now()
        self.days = (self.ending_date - self.starting_date).days

    @staticmethod
    def create_systemtime_object(timeobject):
        """todo"""

        os_date = GetSystemTime()
        return (
            timeobject.year,  # Year
            timeobject.month,  # Month
            os_date[2],  # Day of the week (not used for setting the date)
            timeobject.day,  # Day
            os_date[4],  # Hour
            os_date[5],  # Minute
            os_date[6],  # Second
            os_date[7],  # Milliseconds
        )

    def change_date(self, to_future=False):
        """
        Can only be done using admin cmd
        """
        new_date = self.create_systemtime_object(
            self.current_system_date if to_future else self.current_iteration_day
        )
        SetSystemTime(*new_date)

    def next_day(self, days=1):
        """todo"""
        self.current_iteration_day += timedelta(days=days)
