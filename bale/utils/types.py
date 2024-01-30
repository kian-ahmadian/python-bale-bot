from typing import Union, Dict, Any, TypeVar, Callable, Coroutine, TYPE_CHECKING
if TYPE_CHECKING:
    # noinspection PyUnresolvedReferences
    from bale import Audio, Document, Location, PhotoSize, Video, Animation, Voice

JSONDICT = Dict[str, Any]
T = TypeVar('T')
Coro = Coroutine[Any, Any, T]
CoroT = TypeVar('CoroT', bound=Callable[..., Coro[Any]])

MediaType = Union[
    "Audio",
    "Document",
    "Location",
    "PhotoSize",
    "Video",
    "Animation",
    "Voice"
]