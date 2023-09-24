from typing import List

from facebook_ad_library.fields.base import ADField


class AdDeliveryStopTime(ADField, str):
    field_name = "ad_delivery_stop_time"
