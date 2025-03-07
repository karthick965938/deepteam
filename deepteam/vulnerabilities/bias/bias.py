from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.bias import BiasType


class Bias(BaseVulnerability):
    def __init__(self, types: List[BiasType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of BiasType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, BiasType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type BiasType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Bias"
