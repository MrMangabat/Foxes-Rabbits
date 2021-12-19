from typing import Optional, Tuple
import parameters
import random


## Create entitites module
class Patch:
    

    # Class attributes for grass
    minGrassGrowth = 1
    maxGrassGrowthh = 4
    maxGrassAmout = 30

    def __init__(self, x: int, y:int):
        self._coordinates = (x,y)
        self._foxes = []
        self._rabbits = []
        # Inserts some random amount of grass ----> Ikke sikker på om det er 100 % korrekt, men tænker det.
        self._grass = random.randrange(Patch.maxGrassAmout)

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

    def tick(self):
        
        if self._grass < Patch.maxGrassAmout:
            grassGrowth = self._grass + random.randrange(Patch.minGrassGrowth, Patch.maxGrassGrowthh)
            self._grass = min(grassGrowth, Patch.maxGrassAmout)

    def has_alive_fox(self) -> bool:
        """[Checks the list of foxes, to see whether or not it is alive through is_alive function call]

        Returns:
            bool: [If fox is alive, return True, else False.]
        """        
        for aliveFox in self._foxes:
            if aliveFox.is_alive():
                return aliveFox

    def has_alive_rabbit(self) -> bool:
        """[Checks the list of rabbits, to see whether or not it is alive through is_alive function call.]

        Returns:
            [bool]: [If rabbit is alive, return True, else False.]
        """        
        for aliveRabbit in self._rabbits:
            if aliveRabbit.is_alive():
                return aliveRabbit

    def animalPopulation(self, animal):
        """[Adds an animal type to the one of the followings lists in class:Patch constructor - _foxes or _rabbtis.
        This is also used to verify whether or not an animal is alive]

        Args:
            animal ([Integer]): [Can be either a fox or rabbit.]

        Returns:
            [List]: [description]
        """        
        if type(animal) is Fox:
            self.animalPopulation(animal).append(animal)
            return self._foxes
        else:
            type(animal) is Rabbit
            self.animalPopulation(animal).append(animal)
            return self._rabbits

    def animals(self):
        """[Validates to see if which kind of animals is on the a patch.]

        Returns:
            [Integer]: [An updated list for both foxces and rabbits.]
        """        
        return self._foxes + self._rabbits

    def add(self, animal):
        """[Adds an animal, either fox or rabbit to the total population.]

        Args:
            animal ([List]): [List of animals.]
        """        
        self.animalPopulation(animal).append(animal)
        
    def remove(self, animal):
        """[Removes an animal, can be either fox or rabbit.]

        Args:
            animal ([Integer]): [List of animals.]
        """        
        self.animalPopulation(animal).remove(animal)

class Animal:

    def __init__(self, population: parameters.Population, patch: Patch, energy: int, age: int):
        self._parameters = population
        self._energy = energy
        self._age = age
        self._patch = patch
        self._patch.add(self)
        

    def age(self) -> int:
        return self._age

    def can_eproduce(self) -> bool:
        
        return self.is_alive() and self._energy >= self._parameters.reproduction_min_energy and self._parameters.reproduction_min_age

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

