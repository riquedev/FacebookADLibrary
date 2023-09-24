import json

from facebook_ad_library.types.ad_array import AdArray


class SearchPageIds(AdArray):
    def __post_init__(self):
        if isinstance(self.searches, str):
            self.searches = list(map(lambda v: int(v), self.searches.split(",")))

        self.value = json.dumps(self.searches)

    def __repr__(self):
        return f"search_page_ids={self.value}"