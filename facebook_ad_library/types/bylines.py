from facebook_ad_library.types.ad_array import AdArray


class Bylines(AdArray):

    def __repr__(self):
        return f"bylines={self.value}"
