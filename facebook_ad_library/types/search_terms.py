from facebook_ad_library.types.ad_str import AdStr


class SearchTerms(AdStr):

    def __post_init__(self):
        if len(self.value) > 100:
            raise ValueError("The limit of your string is 100 characters or less")

    def __repr__(self):
        return f"search_terms={self.value}"
