from dataclasses import dataclass, field
from facebook_ad_library.types.ad_library_type import AdLibraryType


@dataclass
class AdStr(AdLibraryType):
    value: str = field(default_factory=str)

    def __repr__(self):
        raise NotImplementedError()
