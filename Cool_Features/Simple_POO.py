from dataclasses import dataclass

# Generates init (constructor) automatically
@dataclass
class Armor:
    armor: float
    description: str
    level: int = 1
