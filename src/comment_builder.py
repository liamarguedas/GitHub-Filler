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

import json
import os
import random
from pathlib import Path


class CommentBuilder:

    def __init__(self):

        self.filepath = Path(__file__).parents[0]
        self.cfg_path = self.filepath / "cfg"
        self.comments_file = self.cfg_path / "comments.json"
        self.comments = self.load_comments()

    def comments_file_exists(self):
        return os.path.exists(self.comments_file)

    def load_comments(self):
        if self.comments_file_exists():
            with open(self.comments_file, "r", encoding="utf-8") as file:
                return json.load(file)["comments"]
        return self.generic_comment()

    def generic_comment(self):
        return ["Fix( comments.json is not working, fix it )"]

    def comment(self):
        return random.choice(self.comments)
