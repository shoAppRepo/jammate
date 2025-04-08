from __future__ import annotations
import dataclasses

@dataclasses.dataclass(frozen=True)
class Song:
    value: str
