from dataclasses import dataclass, field
from typing import List, Union

from facebook_ad_library.fields.base import ADField


@dataclass
class BeneficiaryPlayer:
    beneficiary: str = field(default_factory=str)
    current: bool = field(default_factory=bool)
    payer: str = field(default_factory=str)


class BeneficiaryPlayers(ADField, List[BeneficiaryPlayer]):
    field_name = "beneficiary_payers"

    def __init__(self, values: List[Union[BeneficiaryPlayer,dict]], *args, **kwargs):
        _nvalues = []
        for value in values:

            if isinstance(value, dict):
                value = BeneficiaryPlayer(**value)
            elif not isinstance(value, BeneficiaryPlayer):
                raise ValueError("Invalid value")

            _nvalues.append(value)

        super().__init__(_nvalues)
