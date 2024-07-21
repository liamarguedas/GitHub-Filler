from pathlib import Path
import time
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

        system.change_date()

        for _ in range(git.get_commits_number()):

            git.execute(push=False)

        system.change_date(to_future=True)

        git.push()

        system.next_day()

        time_records.append(time.time() - starting_time)

        for _ in range(10):
            time = round(int(statistics.mean(time_records) * (system.days - day_counter)) / 60, 2)
            print(f"Aprox. estimated time to finish: {time}")

        day_counter += 1

def read_date(date: str):
    """todo"""
    temp = date[1:-1].split(",")
    return (int(temp[0]), int(temp[1]), int(temp[2]))


if __name__ == "__main__":
    main()
    # print(read_date("(2024, 3, 2)"))
