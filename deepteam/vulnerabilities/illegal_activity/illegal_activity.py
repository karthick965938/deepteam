from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.illegal_activity import IllegalActivityType


class IllegalActivity(BaseVulnerability):
    def __init__(self, types: List[IllegalActivityType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of IllegalActivityType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, IllegalActivityType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type IllegalActivityType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Illegal Activity"
