from __future__ import annotations
import dataclasses
from domain.band import Band
from value_objects.uuid import Uuid
from value_objects.profile import Profile

@dataclasses.dataclass(frozen=True)
class Member:
    id: Uuid
    # TODO: 楽器パート追加
    profile: Profile
    joined_bands: list[Band]

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
