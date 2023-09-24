from facebook_ad_library.fields.base import ADField
from facebook_ad_library.types.insights_range_value import InsightsRangeValue


class EstimatedAudienceSize(ADField, InsightsRangeValue):
    field_name = "estimated_audience_size"