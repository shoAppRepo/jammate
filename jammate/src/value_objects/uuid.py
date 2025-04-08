from __future__ import annotations
import dataclasses

@dataclasses.dataclass(frozen=True)
class Uuid:
    value: str
    def __post_init__(self):
        if not isinstance(self.value, str):
            raise TypeError(f"Expected str, got {type(self.value).__name__}")
        if len(self.value) != 36:
            raise ValueError(f"Invalid UUID length: {len(self.value)}")