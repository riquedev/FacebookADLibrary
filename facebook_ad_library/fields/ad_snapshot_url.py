from typing import List

from facebook_ad_library.fields.base import ADField


class AdSnapshotUrl(ADField, str):
    field_name = "ad_snapshot_url"
