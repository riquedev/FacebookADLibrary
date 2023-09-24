from dataclasses import dataclass, field
from typing import List, Union

from facebook_ad_library.fields.base import ADField


@dataclass
class TargetLocation:
    excluded: bool = field(default_factory=bool)
    name: str = field(default_factory=str)
    num_obfuscated: int = field(default_factory=int)
    type: str = field(default_factory=str)
