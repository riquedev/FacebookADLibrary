import json
from dataclasses import field, dataclass
from enum import Enum
from typing import List

from facebook_ad_library.types.ad_library_type import AdLibraryType


class PublisherPlatform(AdLibraryType, Enum):
    FACEBOOK = 'FACEBOOK'
    INSTAGRAM = 'INSTAGRAM'
    AUDIENCE_NETWORK = 'AUDIENCE_NETWORK'
    MESSENGER = 'MESSENGER'
    WHATSAPP = 'WHATSAPP'
    OCULUS = 'OCULUS'

    def __repr__(self):
        raise Exception("Use 'PublisherPlatforms class, not PublisherPlatform'")

@dataclass
class PublisherPlatforms(AdLibraryType):
    values: List[PublisherPlatform] = field(default_factory=list)

    def __post_init__(self):
        self.value = json.dumps(list(map(lambda v: v.value, self.values)))

    def __repr__(self):
        return f"publisher_platforms={self.value}"
