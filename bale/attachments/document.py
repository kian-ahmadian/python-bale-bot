"""
MIT License

Copyright (c) 2023 Kian Ahmadian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from typing import Dict, Optional
from bale import PhotoSize
from .file import BaseFile

__all__ = (
	"Document",
)

class Document(BaseFile):
	"""This object shows a Document.

    Attributes
    ----------
        file_id: :class:`str`
            Identifier for this file, which can be used to download or reuse the file.
        file_unique_id: :class:`str`
            Unique identifier for this file, which is supposed to be the same over time and for different bots. Can’t be used to download or reuse the file.
        thumbnail: Optional[:class:`bale.PhotoSize`]
            document thumbnail as defined by sender.
        file_name: Optional[:class:`str`]
            Original document filename as defined by sender.
        mime_type: Optional[:class:`str`]
            MIME type of file as defined by sender.
        file_size: Optional[:class:`int]
            File size in bytes, if known.
    """
	__slots__ = (
        "thumbnail",
        "file_name",
        "mime_type"
	)

	def __init__(self, file_id: str, file_unique_id: str, file_name: Optional[str], thumbnail: Optional["PhotoSize"], mime_type: Optional[str], file_size: Optional[int]):
		super().__init__(file_id, file_unique_id, file_size)
		self.thumbnail = thumbnail
		self.file_name = file_name
		self.mime_type = mime_type
		self.file_size = file_size

		self._lock()

	@classmethod
	def from_dict(cls, data: Optional[Dict], bot):
		data = BaseFile.parse_data(data)
		if not data:
			return None

		data["thumbnail"] = PhotoSize.from_dict(data.get('thumbnail'), bot)

		return super().from_dict(data, bot)
