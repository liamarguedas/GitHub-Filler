"""
GitHub Filler - Fake Commit Generator for GitHub

Copyright (C) 2024-2024 Liam Arguedas

This file is part of GitHub Filler, a free CLI tool based on the original Commitify 
designed to generate fake commits for GitHub repositories.

GitHub Filler is distributed under the terms of the GNU General Public License (GPL),
either version 3 of the License, or any later version.

GitHub Filler is provided "as is", without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a
particular purpose, and noninfringement. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
GitHub Filler. If not, see <https://www.gnu.org/licenses/>.
"""


from datetime import datetime, timedelta


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

        os_date = datetime.now()

        return datetime(
            timeobject.year,  # Year
            timeobject.month,  # Month
            timeobject.day,  # Day
            os_date.hour,  # Hour
            os_date.minute,  # Minute
            os_date.second,  # Second
        )

    def change_date(self, to_future=False):
        """
        Can only be done using admin cmd
        """
        new_date = self.create_systemtime_object(self.current_iteration_day)

        return new_date.strftime("%Y-%m-%d %H:%M:%S")

    def next_day(self, days=1):
        """todo"""
        self.current_iteration_day += timedelta(days=days)
