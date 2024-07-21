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

WORDS = "random_words.txt"
FILE_TXT = "file_txt.txt"
CONFIG = "config.json"

class FileBuilder:

    def __init__(self):
        self.filepath = Path(__file__).parents[0]
        self.txt_path = self.filepath / "txt"
        self.words_file = self.txt_path / WORDS 
        self.file_txt = self.txt_path / FILE_TXT 
        self.words = self.read_text(self.words_file)
        self.file_text = self.read_text(self.file_txt)
        self.filename = None
        self.filetype = self.read_filetype()

    @staticmethod
    def path_exists(dirname):
        """todo"""
        return os.path.exists(dirname)

    @staticmethod
    def generate_extra_file(file, dirname):
        """todo"""
        _splited_file = file.split(".")
        same_name_files = [
            directory_file
            for directory_file in os.listdir(dirname)
            if _splited_file[0] in directory_file
        ]
        return f"{_splited_file[0]}{len(same_name_files) + 1}.{_splited_file[1]}"

    def write_new_file(self, filename):
        """todo"""
        with open(filename, "w", encoding="utf-8") as file:
            for line in self.file_text:
                file.write(f"{line}\n")

    def read_filetype(self):
        """todo"""
        with open(self.filepath / "cfg" / CONFIG, "r", encoding="utf-8") as file:

            file_type = json.load(file)["file"]
            return file_type

    def file_in_path(self, dirname):
        """todo"""
        return os.path.exists(f"{dirname}/{self.filename}")

    def generate_name(self):
        """todo"""
        self.filename = f"{random.choice(self.words)}.{self.filetype}"
        return self.filename

    def read_text(self, file):
        """todo"""
        if self.path_exists(file):
            with open(file, "r", encoding="utf-8") as loaded_file:
                return [line.rstrip("\n") for line in loaded_file.readlines()]
        return ["file"]

    def create_file(self, dirname):
        """todo"""
        if self.path_exists(dirname):
            file = self.generate_name()
            if self.file_in_path(dirname):
                file = self.generate_extra_file(file, dirname)
            self.write_new_file(dirname / file)
