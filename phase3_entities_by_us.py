from typing import Optional
import parameters
## Create entitites module
class Animal:

    def __init__(self, population: parameters.Population, patch: Patch, energy: int, age: int ):
        self._parameters = Population
        self._Fox = Fox

    def _age(self):
        pass

    def can_eproduce(self):
        pass

    def energy(self):
        pass

    def feed(self):
        pass

    def is_alive(self):
        pass

    def move_to(self):
        pass

    def patch(self):
        pass

    def predatator_in(self, patch:patch) -> bool:
        pass

    def reproduce(self, newborn_patch: Patch):
        pass

    def same_species_in(self, patch:Patch) -> bool:
        pass

    def tick(self):
        pass
   
class Rabbit:

    def __init__(Animal):
        pass

    def food_energy_per_unit(self):
        pass

    def reproduction_cost_rate(self):
        pass

class Fox:

    def __init__(Animal):
        pass

    def feeding_metabolism_rate(self):
        pass

    def reproduction_cost_rate(self):
        pass

    def kill(self):
        pass

    def was_killed(self) -> bool:
        pass

class Patch:

    def __init__(x: int, y:int):
        self._foxes = []
        self._rabbits = []
        self._coordinates = (x,y)
        self._grass = grass

    def add(self):
        pass

    def animals(self):
        pass

    def coordinates(self):
        pass

    def grass(self):
        
        min_grass_growth = 1
        max_grass_growth = 4
        max_grass_amount = 30

        pass

    def has_alive_fox(self) -> bool:
        pass

    def has_alive_rabbit(self) -> bool:
        pass

    def remove(self, animal):
        pass

    def tick(self):
        pass
