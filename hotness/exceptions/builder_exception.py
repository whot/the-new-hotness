# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
from typing import Optional


class BuilderException(Exception):
    """
    Class representing builder exception.
    This exception is raised by builder
    when it encounters error with external builder system.

    Attributes:
        message: Error message.
        output: Partial output from builder, needed for koji build id.
        std_out: Standard output of command if the exception was triggered by subprocess call.
        std_err: Error output of command if the exception was triggered by subprocess call.
    """

    def __init__(
        self,
        message: str,
        output: Optional[dict] = {},
        std_out: Optional[str] = "",
        std_err: Optional[str] = "",
    ) -> None:
        """
        Class constructor.
        """
        self.message = message
        self.output = output
        self.std_out = std_out
        self.std_err = std_err
        super(BuilderException, self).__init__(self.message)

    def __str__(self) -> str:
        """
        String representation of error.
        """
        return self.message
