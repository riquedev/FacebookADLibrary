from facebook_ad_library.types.ad_int import AdInt


class EstimatedAudienceSizeMin(AdInt):

    def __repr__(self):
        return f"estimated_audience_size_min={self.value}"
