"""
Commitify - Fake Commit Generator for GitHub

Copyright (C) 2024-2024 Liam Arguedas

This file is part of Commitify, a free CLI tool designed to generate fake commits
for GitHub repositories.

Commitify is distributed under the terms of the GNU General Public License (GPL),
either version 3 of the License, or any later version.

Commitify is provided "as is", without warranty of any kind, express or implied,
including but not limited to the warranties of merchantability, fitness for a
particular purpose, and noninfringement. See the GNU General Public License for
more details.

You should have received a copy of the GNU General Public License along with
Commitify. If not, see <https://www.gnu.org/licenses/>.
"""

from pathlib import Path
import random
import os
import json
from .comment_builder import CommentBuilder
from .file_builder import FileBuilder

BLANK = ""


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
        with open(self.filepath / "cfg" / "config.json", "r", encoding="utf-8") as file:
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
        command = f'git init'
        os.system(command)
        
    def set_remote_repository(self, repo):
        """todo"""
        command = f'git remote add origin {repo}'

        os.system(command)

    def add(self):
        command = "git add ."
        os.system(command)

    def commit(self, message: str):
        command = f'git commit -m "{message}"'
        os.system(command)

    def push(self):
        """todo"""
        command = f"git push origin {self.branch}"
        os.system(command)

    def execute(self, push=True):
        """todo"""
        self.file_generator.create_file(self.directory)
        self.add()
        comment = self.comment_generator.comment()
        self.commit(message=comment)
        if push:
            self.push()
