from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Citizen:
    name: str
    roles: List[str] = field(default_factory=list)
    allowed_places: List[str] = field(default_factory=list)

@dataclass
class Role:
    title: str
    allowed_places: List[str] = field(default_factory=list)
    sub_roles: List[str] = field(default_factory=list)

@dataclass
class ApalulaDataSet:
    citizens: List[Citizen]
    roles: List[Role]
