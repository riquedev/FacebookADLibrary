from typing import List

from facebook_ad_library.fields.base import ADField


class AdCreativeLinkTitles(ADField, List[str]):
    field_name = "ad_creative_link_titles"
