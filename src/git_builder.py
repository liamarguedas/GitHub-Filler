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
import random
import os
import json
from .comment_builder import CommentBuilder
from .file_builder import FileBuilder

BLANK = ""
CONFIG = "config.json"


class GitBuilder:
    """todo"""

    def __init__(self, directory, files="."):
        self.comment_generator = CommentBuilder()
        self.file_generator = FileBuilder()
        self.directory = directory
        self.filepath = Path(__file__).parents[0]
        self.cfgs = self.read_configs()
        self.branch = self.cfgs["branch"]
        self.files = files

    @staticmethod
    def random_commits(n=25):
        """todo"""
        return random.randint(1, n)

    def read_configs(self):
        """todo"""
        with open(self.filepath / "cfg" / CONFIG, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_commits_number(self):
        """todo"""
        if not self.cfgs["commits"] == BLANK:
            try:
                return int(self.cfgs["commits"])

            except Exception as e:
                print(e)
                print("ERROR: Could not read number of commits, using random commits")

        return self.random_commits()

    def init_repository(self):
        """todo"""
        command = "git init"
        os.system(command)

    def set_remote_repository(self, repo):
        """todo"""
        command = f"git remote set-url origin {repo}"

        os.system(command)

    def add(self):
        """todo"""
        command = "git add ."
        os.system(command)

    def commit(self, message: str, date: str):
        """todo"""
        command = f'git commit --date="{date}" -m "{message}"'
        os.system(command)

    def push(self):
        """todo"""
        command = f"git push origin {self.branch}"
        os.system(command)

    def execute(self, date: str, push=True):
        """todo"""
        self.file_generator.create_file(self.directory)
        self.add()
        comment = self.comment_generator.comment()
        self.commit(message=comment, date=date)
        if push:
            self.push()
