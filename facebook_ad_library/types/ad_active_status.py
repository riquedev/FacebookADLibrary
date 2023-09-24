from enum import Enum
from facebook_ad_library.types.ad_library_type import AdLibraryType


class AdActiveStatus(AdLibraryType, Enum):
    ACTIVE = 'ACTIVE'
    ALL = 'ALL'
    INACTIVE = 'INACTIVE'

    def __repr__(self):
        return f"ad_active_status={self.value}"