# Topydo - A todo.txt client written in Python.
# Copyright (C) 2014 - 2015 Bram Schoenmakers <bram@topydo.org>
# Copyright (C) 2024 Niklas Ruecker 
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from topydo.lib.Command import InvalidCommandArgument
from topydo.lib.Config import config
from topydo.lib.prettyprinters.Numbers import PrettyPrinterNumbers
from topydo.lib.TodoListBase import InvalidTodoException
from topydo.lib.TodoParser import parse_line
from topydo.lib.WriteCommand import WriteCommand


class ArchiveCommand(WriteCommand):
    def __init__(self, p_args, p_todolist, #pragma: no branch
                 p_out=lambda a: None,
                 p_err=lambda a: None,
                 p_prompt=lambda a: None):
        super().__init__(p_args, p_todolist, p_out, p_err,
                p_prompt)

    def execute(self):
        if not super().execute():
            return False

        try:
            number = self.argument(0)
            print(number)
        except InvalidCommandArgument:
            self.error(self.usage())
        except InvalidTodoException:
            self.error("Invalid todo number given.")

    def usage(self):
        return """Synopsis: archive <NUMBER>"""

    def help(self):
        return """\
Archives the todo indicated by NUMBER.\
"""

