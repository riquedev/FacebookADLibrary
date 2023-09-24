from facebook_ad_library.types.ad_array import AdArray


class DeliveryByRegion(AdArray):

    def __repr__(self):
        return f"delivery_by_region={self.value}"
