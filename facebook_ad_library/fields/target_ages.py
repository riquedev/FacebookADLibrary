from typing import List

from facebook_ad_library.fields.base import ADField


class TargetAges(ADField, List[str]):
    field_name = "target_ages"