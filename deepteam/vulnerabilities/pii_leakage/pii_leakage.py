from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.pii_leakage import PIILeakageType


class PIILeakage(BaseVulnerability):
    def __init__(self, types: List[PIILeakageType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of PIILeakageType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, PIILeakageType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type PIILeakageType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "PII Leakage"
