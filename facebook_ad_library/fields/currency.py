from typing import List

from facebook_ad_library.fields.base import ADField


class Currency(ADField, str):
    field_name = "currency"
