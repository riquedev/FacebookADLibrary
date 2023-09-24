from typing import List

from facebook_ad_library.fields.base import ADField


class Languages(ADField, List[str]):
    field_name = "languages"