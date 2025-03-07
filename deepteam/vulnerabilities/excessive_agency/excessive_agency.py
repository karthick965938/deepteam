from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.excessive_agency import ExcessiveAgencyType


class ExcessiveAgency(BaseVulnerability):
    def __init__(self, types: List[ExcessiveAgencyType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of ExcessiveAgencyType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, ExcessiveAgencyType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type ExcessiveAgencyType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Excessive Agency"
