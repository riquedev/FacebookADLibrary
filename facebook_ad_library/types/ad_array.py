import json
from dataclasses import dataclass, field
from facebook_ad_library.types.ad_library_type import AdLibraryType


@dataclass
class AdArray(AdLibraryType):
    searches: list = field(default_factory=list)

    def __post_init__(self):
        if isinstance(self.searches, str):
            self.searches = list(map(lambda v: str(v).strip(), self.searches.split(",")))

        self.value = json.dumps(self.searches)

    def __repr__(self):
        raise NotImplementedError()
