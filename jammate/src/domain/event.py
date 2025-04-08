from __future__ import annotations
import dataclasses
import datetime
from value_objects.uuid import Uuid

@dataclasses.dataclass(frozen=True)
class Event:
    id: Uuid
    name: str
    location: str
    start_at: datetime
    memo: str
    # TODO: 参加バンド追加    

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
