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
from __future__ import annotations
from typing import TYPE_CHECKING, Optional, List, Union, Dict
from bale import BaleObject, Document, PhotoSize, Video, Audio, Animation
from bale.utils.types import FileInput, MediaInput, MissingValue, MaybeMissing

if TYPE_CHECKING:
    from bale import InlineKeyboardMarkup, MenuKeyboardMarkup, LabeledPrice, Location, Contact, InputFile, Message


class User(BaleObject):
    """This object represents a Bale user or bot.

    Attributes
    ----------
        id: :obj:`int`
            Unique identifier for this user or bot.
        is_bot: :obj:`bool`, optional
            :obj:`True`, if this user is a bot.
        first_name: :obj:`str`
            User’s or bot’s first name.
        last_name: :obj:`str`, optional
            User’s or bot’s last name.
        username: :obj:`str`, optional
            User’s or bot’s username.
    """
    __slots__ = (
        "__weakref__",
        "is_bot",
        "first_name",
        "last_name",
        "username",
        "id"
    )

    def __init__(self, user_id: int, is_bot: bool, first_name: str, last_name: Optional[str] = None,
                 username: Optional[str] = None) -> None:
        super().__init__()
        self._id = user_id
        self.is_bot = is_bot
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.id = user_id

        self._lock()

    @property
    def mention(self) -> Optional[str]:
        """:obj:`str`, optional: mention user with username."""
        if self.username:
            return "@" + self.username

        return None

    @property
    def chat_id(self) -> int:
        """Aliases for :attr:`id`"""
        return self.id
    
    def state(self, value: Any) -> None:
        """Set and save the user's state."""
        self._state = value
        # Assuming there's a method to save state, e.g., in a database
        self._save_state(value)

    def get_state(self) -> Any:
        """Load and return the user's state."""
        if not hasattr(self, '_state'):
            # Assuming there's a method to load state from storage
            self._state = self._load_state()
        return self._state

    def clear_state(self) -> None:
        """Clear the user's state."""
        if hasattr(self, '_state'):
            del self._state
        # Assuming there's a method to clear state from storage
        self._clear_state()

    def _save_state(self, value: Any) -> None:
        # Implementation for saving state to storage
        pass

    def _load_state(self) -> Any:
        # Implementation for loading state from storage
        pass

    def _clear_state(self) -> None:
        # Implementation for clearing state from storage
        pass


    @property
    def user_id(self) -> int:
        """Aliases for :attr:`id`"""
        return self.id

    async def send(self, text: str,
                   components: MaybeMissing[Union["InlineKeyboardMarkup", "MenuKeyboardMarkup"]] = MissingValue,
                   delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_message(
                chat_id=user.id, *args, **kwargs
            )

        For the documentation of the arguments, please see :meth:`bale.Bot.send_message`.

        .. hint::
            .. code:: python

                await user.send("Hi, python-bale-bot!", components = None)
        """
        return await self.get_bot().send_message(self.chat_id, text, components=components, delete_after=delete_after)

    async def send_document(self, document: Union["Document", FileInput], *, caption: MaybeMissing[str] = MissingValue,
                            components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                            delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_document(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_document`.

        .. hint::
            .. code:: python

                await user.send_document(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_document(self.chat_id, document, caption=caption, components=components,
                                                  delete_after=delete_after, file_name=file_name)

    async def send_photo(self, photo: Union["PhotoSize", FileInput], *, caption: MaybeMissing[str] = MissingValue,
                         components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_photo(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_photo`.

        .. hint::
            .. code:: python

                await user.send_photo(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_photo(self.chat_id, photo, caption=caption, components=components,
                                               delete_after=delete_after, file_name=file_name)

    async def send_video(self, video: Union["Video", FileInput], *, caption: MaybeMissing[str] = MissingValue,
                         components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_video(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_video`.

        .. hint::
            .. code:: python

                await user.send_video(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_video(self.chat_id, video, caption=caption, components=components,
                                               delete_after=delete_after, file_name=file_name)

    async def send_animation(self, animation: Union["Animation", FileInput], *,
                             duration: MaybeMissing[int] = MissingValue, width: MaybeMissing[int] = MissingValue,
                             height: MaybeMissing[int] = MissingValue, caption: MaybeMissing[str] = MissingValue,
                             components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                             delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_animation(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_animation`.

        .. hint::
            .. code:: python

                await user.send_animation(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_animation(self.chat_id, animation, duration=duration, width=width,
                                                   height=height, caption=caption, components=components,
                                                   delete_after=delete_after, file_name=file_name)

    async def send_audio(self, audio: Union["Audio", InputFile], *, caption: MaybeMissing[str] = MissingValue,
                         components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                         delete_after: Optional[Union[float, int]] = None, file_name: Optional[str] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_audio(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_audio`.

        .. hint::
            .. code:: python

                await user.send_audio(bale.InputFile("FILE_ID"), caption = "this is a caption", ...)
        """
        return await self.get_bot().send_audio(self.chat_id, audio, caption=caption, components=components,
                                               delete_after=delete_after, file_name=file_name)

    async def send_location(self, location: "Location", *,
                            components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                            delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_location(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_location`.

        .. hint::
            .. code:: python

                await user.send_location(bale.Location(35.71470468031143, 51.8568519168293))
        """
        return await self.get_bot().send_location(self.chat_id, location, components=components,
                                                  delete_after=delete_after)

    async def send_contact(self, contact: "Contact", *,
                           components: MaybeMissing["InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue,
                           delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_contact(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_contact`.

        .. hint::
            .. code:: python

                await user.send_contact(bale.Contact('09****', 'first name', 'last name))
        """
        return await self.get_bot().send_contact(self.chat_id, contact, components=components,
                                                 delete_after=delete_after)

    async def send_invoice(self, title: str, description: str, provider_token: str, prices: List["LabeledPrice"], *,
                           payload: MaybeMissing[str] = MissingValue,
                           photo_url: MaybeMissing[str] = MissingValue, need_name: MaybeMissing[bool] = False,
                           need_phone_number: MaybeMissing[bool] = False,
                           need_email: MaybeMissing[bool] = False, need_shipping_address: MaybeMissing[bool] = False,
                           is_flexible: MaybeMissing[bool] = True,
                           delete_after: Optional[Union[float, int]] = None):
        """
        Shortcut method for:

        .. code:: python

            await bot.send_invoice(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_invoice`.

        .. hint::
            .. code:: python

                await user.send_invoice(
                    "invoice title", "invoice description", "6037************", [bale.LabeledPrice("label", 2000)],
                    payload = "unique invoice payload", ...
                )
        """
        return await self.get_bot().send_invoice(self.chat_id, title, description, provider_token, prices,
                                                 invoice_payload=payload, photo_url=photo_url, need_name=need_name,
                                                 need_email=need_email,
                                                 need_phone_number=need_phone_number,
                                                 need_shipping_address=need_shipping_address, is_flexible=is_flexible,
                                                 delete_after=delete_after)

    async def send_media_group(self, media: List[MediaInput], *,
                               components: MaybeMissing[
                                   "InlineKeyboardMarkup", "MenuKeyboardMarkup"] = MissingValue) -> List["Message"]:
        """
        Shortcut method for:

        .. code:: python

            await bot.send_media_group(
                chat_id=user.id, *args, **kwargs
            )
            
        For the documentation of the arguments, please see :meth:`bale.Bot.send_media_group`.

        .. hint::
            .. code:: python

                await user.send_media_group([
                    InputMediaPhoto("File ID", caption="example caption"),
                    InputMediaPhoto("File ID"),
                    InputMediaPhoto("File ID")
                ], ...)
        """
        return await self.get_bot().send_media_group(self.id, media, components=components, reply_to_message_id=self.id)

    @classmethod
    def from_dict(cls, data: Optional[Dict], bot):
        data = BaleObject.parse_data(data)
        if not data:
            return None

        data["user_id"] = data.pop("id")

        return super().from_dict(data, bot)
