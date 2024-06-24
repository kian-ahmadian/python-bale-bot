# An API wrapper for Bale written in Python
# Copyright (c) 2022-2024
# Kian Ahmadian <devs@python-bale-bot.ir>
# All rights reserved.
#
# This software is licensed under the GNU General Public License v2.0.
# See the accompanying LICENSE file for details.
#
# You should have received a copy of the GNU General Public License v2.0
# along with this program. If not, see <https://www.gnu.org/licenses/gpl-2.0.html>.
from pathlib import Path
from typing import Union, Any, Optional, Type, TYPE_CHECKING
if TYPE_CHECKING:
    from bale import BaleObject


def is_file_valid(obj: Optional[Union[Path, str]]) -> Optional[Path]:
    if obj is None:
        return None

    path = Path(obj)
    return path if path.is_file() else None


def parse_file_input(
        file_input: Any,
        attachment_type: Optional[Type["BaleObject"]] = None,
        file_name: Optional[str] = None
):
    from bale import InputFile

    if isinstance(file_input, bytes):
        return InputFile(file_input, file_name=file_name)
    elif isinstance(file_input, (Path, str)):
        if result_path := is_file_valid(file_input):
            return result_path.open(mode="rb")
    elif attachment_type and isinstance(file_input, attachment_type):
        return file_input.file_id  # type: ignore
    elif isinstance(file_input, InputFile):
        return file_input

    raise TypeError(
        "You cannot give the file like this. Your file must be one of bytes, str and InputFile types."
    )
