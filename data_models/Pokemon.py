from __future__ import annotations
from typing import Tuple, List
from abc import ABC, abstractmethod

#Here we create an abstract class, an abstract class can't be instantiated, only it's child.
class Pokemon(ABC):
    def __init__(self, name: str, pokedexId: str, level: int, living_points: int, attacking_points: int,
                 defense_points: int, attack: List[Tuple[str, int]]) -> None:
        self.name = name
        self.pokedexId = pokedexId
        self.level = level
        self.living_points = living_points
        self.attacking_points = attacking_points
        self.defense_points = defense_points
        self.attack = attack
        self.experience_points: int = 0
        self.fight_status: bool = False
        self.alive: bool = True

    @abstractmethod
    def lvlUp(self) -> Pokemon:
        pass