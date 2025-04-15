from __future__ import annotations
import dataclasses
import datetime
from value_objects.uuid import Uuid
from band import Band

@dataclasses.dataclass(frozen=True)
class Event:
    id: Uuid
    name: str
    location: str
    start_at: datetime
    memo: str
    performers: list[Band] 

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
