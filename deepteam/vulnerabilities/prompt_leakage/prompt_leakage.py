from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.prompt_leakage import PromptLeakageType


class PromptLeakage(BaseVulnerability):
    def __init__(self, types: List[PromptLeakageType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of PromptLeakageType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, PromptLeakageType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type PromptLeakageType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Prompt Leakage"
