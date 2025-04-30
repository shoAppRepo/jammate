from __future__ import annotations
import dataclasses
from member import Member
from event import Event
from value_objects.uuid import Uuid
from value_objects.song import Song

@dataclasses.dataclass(frozen=True)
class Band:
    id: Uuid
    name: str
    songs: list[Song]
    event: Event
    members: list[Member]

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)