from enum import Enum
from facebook_ad_library.types.ad_library_type import AdLibraryType


class MediaType(AdLibraryType, Enum):
    ALL = 'ALL'
    IMAGE = 'IMAGE'
    MEME = 'MEME'
    VIDEO = 'VIDEO'
    NONE = 'NONE'

    def __repr__(self):
        return f"media_type={self.value}"
