from facebook_ad_library.fields.base import ADField
from facebook_ad_library.types.insights_range_value import InsightsRangeValue


class Impressions(ADField, InsightsRangeValue):
    field_name = "impressions"