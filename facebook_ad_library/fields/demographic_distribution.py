from typing import List, Union

from facebook_ad_library.fields.base import ADField
from facebook_ad_library.types.audience_distribution import AudienceDistribution


class DemographicDistribution(ADField, List[AudienceDistribution]):
    field_name = "demographic_distribution"

    def __init__(self, values: List[Union[AudienceDistribution, dict]] = [], *args, **kwargs):
        _nvalues = []
        for value in values:

            if isinstance(value, dict):
                value = AudienceDistribution(**value)
            elif not isinstance(value, AudienceDistribution):
                raise ValueError("Invalid value")

            _nvalues.append(value)

        super().__init__(_nvalues)
