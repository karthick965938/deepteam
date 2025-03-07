from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.competition import CompetitionType


class Competition(BaseVulnerability):
    def __init__(self, types: List[CompetitionType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of CompetitionType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, CompetitionType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type CompetitionType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Competition"
