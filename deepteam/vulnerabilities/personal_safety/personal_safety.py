from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.personal_safety import PersonalSafetyType


class PersonalSafety(BaseVulnerability):
    def __init__(self, types: List[PersonalSafetyType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of PersonalSafetyType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, PersonalSafetyType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type PersonalSafetyType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Personal Safety"
