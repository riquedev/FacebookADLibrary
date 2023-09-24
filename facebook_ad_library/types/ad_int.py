from dataclasses import dataclass, field
from facebook_ad_library.types.ad_library_type import AdLibraryType


@dataclass
class AdInt(AdLibraryType):
    value: int = field(default_factory=int)

    def __post_init__(self):
        if isinstance(self.value, str):
            self.value = int(self.value)

    def __repr__(self):
        raise NotImplementedError()
