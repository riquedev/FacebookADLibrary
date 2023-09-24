from dataclasses import dataclass, field


@dataclass
class InsightsRangeValue:
    lower_bound: str = field(default_factory=str)
    upper_bound: str = field(default_factory=str)