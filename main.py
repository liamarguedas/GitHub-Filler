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

from pathlib import Path
import time
import os, shutil
import statistics
from build import GithubFillerConfig
from src import GitBuilder
from src import DateChanger

ROOT_PATH = Path(__file__).parents[0]
FILES_DIR = ROOT_PATH / "files"


def main():
    """todo"""

    params = GithubFillerConfig().ask_configs(return_configs=True)

    start_date = read_date(params["starting_date"])
    stop_date = read_date(params["ending_date"])

    system = DateChanger(starting_date=start_date, ending_date=stop_date)

    git = GitBuilder(directory=FILES_DIR)

    git.init_repository()

    git.set_remote_repository(params["repository"])

    time_records = []
    day_counter = 0

    while system.current_iteration_day != system.ending_date:

        starting_time = time.time()

        date = system.change_date()

        for _ in range(git.get_commits_number()):

            git.execute(push=False, date=date)

        git.push()

        system.next_day()

        time_records.append(time.time() - starting_time)

        for _ in range(10):
            approx_time = round(
                int(statistics.mean(time_records) * (system.days - day_counter)) / 60, 2
            )
            print(f"Aprox. estimated time to finish: {approx_time} minutes")

        day_counter += 1


def read_date(date: str):
    """todo"""
    temp = date.split(",")
    return (int(temp[0]), int(temp[1]), int(temp[2]))

if __name__ == "__main__":
    main()
