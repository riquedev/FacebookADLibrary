from enum import Enum
from facebook_ad_library.types.ad_library_type import AdLibraryType


class AdType(AdLibraryType, Enum):
    ALL = 'ALL'
    CREDIT_ADS = 'CREDIT_ADS'
    EMPLOYMENT_ADS = 'EMPLOYMENT_ADS'
    HOUSING_ADS = 'HOUSING_ADS'
    POLITICAL_AND_ISSUE_ADS = 'POLITICAL_AND_ISSUE_ADS'

    def __repr__(self):
        return f"ad_type={self.value}"
