from typing import List

from facebook_ad_library.fields.base import ADField


class AdDeliveryStartTime(ADField, str):
    field_name = "ad_delivery_start_time"
