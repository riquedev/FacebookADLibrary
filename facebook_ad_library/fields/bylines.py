from typing import List

from facebook_ad_library.fields.base import ADField


class Bylines(ADField, str):
    field_name = "bylines"
