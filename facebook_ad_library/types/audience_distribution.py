from dataclasses import dataclass, field
from typing import List, Union

from facebook_ad_library.fields.base import ADField


@dataclass
class AudienceDistribution:
    age: str = field(default_factory=str)
    gender: str = field(default_factory=str)
    percentage: str = field(default_factory=str)
    region: str = field(default_factory=str)