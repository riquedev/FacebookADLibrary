import datetime
from facebook_ad_library.types.ad_date_type import AdDateType


class AdDeliveryDateMin(AdDateType):
    date: datetime.date
    date_str_format: str = '%Y-%m-%d'

    def __repr__(self):
        return f"ad_delivery_date_min={self.date.strftime('%Y-%m-%d')}"
