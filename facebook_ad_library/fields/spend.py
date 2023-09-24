from facebook_ad_library.fields.base import ADField
from facebook_ad_library.types.insights_range_value import InsightsRangeValue


class Spend(ADField, InsightsRangeValue):
    field_name = "spend"