from enum import Enum
from facebook_ad_library.types.ad_library_type import AdLibraryType


class SearchType(AdLibraryType, Enum):
    KEYWORD_UNORDERED = "KEYWORD_UNORDERED"
    KEYWORD_EXACT_PHRASE = "KEYWORD_EXACT_PHRASE"

    def __repr__(self):
        return f"search_type={self.value}"
