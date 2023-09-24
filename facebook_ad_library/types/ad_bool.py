from dataclasses import dataclass, field
from facebook_ad_library.types.ad_library_type import AdLibraryType


@dataclass
class AdBool(AdLibraryType):
    value: bool = field(default_factory=bool)

    def __post_init__(self):
        self.value_str = "true" if self.value else "false"


    def __repr__(self):
        raise NotImplementedError()
