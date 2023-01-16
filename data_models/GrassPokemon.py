from data_models.PokeType import PokeType
from data_models.Pokemon import Pokemon


class GrassPokemon(Pokemon):
    def __init__(self, name: str, pokedexId: str, level: int, living_points: int, attacking_points: int,
                 defense_points: int, attack):
        super().__init__(name, pokedexId, level, living_points, attacking_points,
                         defense_points, attack)

        self.type: PokeType = PokeType(2)
    def lvlUp(self) -> Pokemon:
        pass