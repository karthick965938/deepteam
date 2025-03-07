from typing import List

from deepteam.vulnerabilities import BaseVulnerability
from deepteam.vulnerabilities.graphic_content import GraphicContentType


class GraphicContent(BaseVulnerability):
    def __init__(self, types: List[GraphicContentType]):
        if not isinstance(types, list):
            raise TypeError(
                "The 'types' attribute must be a list of GraphicContentType enums."
            )
        if not types:
            raise ValueError("The 'types' attribute cannot be an empty list.")
        if not all(isinstance(t, GraphicContentType) for t in types):
            raise TypeError(
                "All items in the 'types' list must be of type GraphicContentType."
            )
        super().__init__(types=types)

    def get_name(self) -> str:
        return "Graphic Content"
