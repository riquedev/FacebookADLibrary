from dataclasses import dataclass, field
from typing import List, Union

from facebook_ad_library.fields.base import ADField


@dataclass
class AgeGenderReachBreakdown:
    age_range: str = field(default_factory=str)
    female: int = field(default_factory=int)
    male: int = field(default_factory=int)
    unknown: int = field(default_factory=int)


class AgeCountryGenderReachBreakdown(ADField, List[AgeGenderReachBreakdown]):
    field_name = "age_country_gender_reach_breakdown"

    def __init__(self, values: List[Union[AgeGenderReachBreakdown,dict]], *args, **kwargs):
        _nvalues = []
        for value in values:

            if isinstance(value, dict):
                value = AgeGenderReachBreakdown(**value)
            elif not isinstance(value, AgeCountryGenderReachBreakdown):
                raise ValueError("Invalid value")

            _nvalues.append(value)

        super().__init__(_nvalues)
