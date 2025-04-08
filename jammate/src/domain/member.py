from __future__ import annotations
import dataclasses
from value_objects.uuid import Uuid
from band import Band

@dataclasses.dataclass(frozen=True)
class Member:
    id: Uuid
    name: str
    # TODO: 楽器パート追加
    introduction: str
    icon_url: str
    favorite_genres: str
    joined_bands: list[Band]

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    def to_dict(self):
        return dataclasses.asdict(self)
