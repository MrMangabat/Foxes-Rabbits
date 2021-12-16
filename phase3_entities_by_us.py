from typing import Optional, Tuple
import parameters
import random
## Create entitites module
class Patch:
    

    # Class attributes for regarding grass
    min_grass_growth = 1
    max_grass_growth = 4
    max_grass_amount = 30


    def __init__(x: int, y:int):
        self._coordinates = (x,y)
        self._foxes = []
        self._rabbits = []
        # Inserts some random amount of grass ----> Ikke sikker på om det er 100 % korrekt, men tænker det.
        self._grass = random.randrange(Patch.max_grass_amount)

# Getters for class Patch.
    def coordinates(self) -> Tuple[int, int]:
        """[Return coordinates of the current patch]

        Returns:
            Tuple[int, int]: [Returns coordinates as a tuple wiht integers.]
        """        
        return self._coordinates

    def grass(self) -> int:
        """[Returns current amunt of grass within a patch.]

        Returns:
            int: [A number which defines the amount of grass on current patch.]
        """       
        return self._grass

## Setters for class Patch.
    def tick(self):
        pass

    def has_alive_fox(self) -> bool:
        pass

    def has_alive_rabbit(self) -> bool:
        pass
    def add(self, animal:Animal):
        pass

    def remove(self, animal:Animal):
        pass

    # def animals(self):
    #     pass


class Animal:

    def __init__(self, population: parameters.Population, patch: Patch, energy: int, age: int ):
        self._parameters = population
        self._energy = energy
        self._age = age
        self._patch = patch
        self._patch.add(self)

## Getters for class Animal.
    def age(self) -> int:
        return self._age

    def can_eproduce(self) -> bool:
        pass

    def energy(self) -> int:
        return self._energy

    def feed(self):

        pass

    def is_alive(self) -> bool:

        return self._energy > 0 and self._age < self._parameters.max_age

    def move_to(self):
        pass

    def patch(self) -> Patch:
        return self._patch

    def predatator_in(self, patch:Patch) -> bool:
        """[]

        Args:
            patch (Patch): [description]

        Returns:
            bool: [description]
        """        
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

