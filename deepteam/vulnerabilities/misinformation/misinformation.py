from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.misinformation import MisinformationType


class Misinformation(BaseVulnerability):
    def __init__(self, types: List[MisinformationType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of MisinformationType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, MisinformationType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type MisinformationType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Misinformation"
