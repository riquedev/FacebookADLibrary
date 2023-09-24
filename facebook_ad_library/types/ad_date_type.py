import datetime
from dataclasses import dataclass

from facebook_ad_library.types.ad_library_type import AdLibraryType


@dataclass
class AdDateType(AdLibraryType):
    date: datetime.date
    date_str_format: str = '%Y-%m-%d'

    def __post_init__(self):
        if isinstance(self.date, str):
            self.date = datetime.datetime.strptime(self.date, self.date_str_format).date()
        elif isinstance(self.date, datetime.datetime):
            self.date = self.date.date()

    def __repr__(self):
        raise NotImplementedError()
