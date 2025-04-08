from __future__ import annotations
import dataclasses

@dataclasses.dataclass(frozen=True)
class Profile:
    name: str
    introduction: str
    icon_url: str
    favorite_genres: str

    # TODO: バリデーション
