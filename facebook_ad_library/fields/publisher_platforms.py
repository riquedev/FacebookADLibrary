from typing import List

from facebook_ad_library.fields.base import ADField


class PublisherPlatformsField(ADField, List[str]):
    field_name = "publisher_platforms"