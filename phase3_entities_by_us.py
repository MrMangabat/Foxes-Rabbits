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
        """[This is the constructor for class Patch]

        Args:
            x (int): [Enables accesss to coordinates from west to east in the grid.]
            y (int): [Enables accesss to coordinates from north to south in the grid.]
        """    
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
        """[Enables the tracking of age for each individual]

        Returns:
            int: [The age of each individual in for each species.]
        """        
        return self._age

    def can_eproduce(self) -> bool:
        """[Checks if an animal is alive and validates reproduction criterias according to parameters for minimum energy and age with a True/False.]

        Returns:
            bool: [True if an animal can reproduce else False.]
        """        
        return self.is_alive() and self._energy >= self._parameters.reproduction_min_energy and self._parameters.reproduction_min_age

    def reproduce(self, newbornPatch: Patch) -> Optional["Animal"]:
        """[Handles the scenario when a newborn is being born into the simulation or none.]

        Args:
            patch (Patch): [The position of the animal.]

        Returns:
            [Integer]: [A newborn rabbit or foxes.]
        """    
        return None

    def energy(self) -> int:
        """[Tracking of an species energy level.]

        Returns:
            int: [Returns species energy level.]
        """    
        return self._energy

    def feed(self):

        pass

    def is_alive(self) -> bool:
        """[Function that checks if a an animal is alive, if not not it return False otherwise True.]

        Returns:
            bool: [True or False depending on whether or not the animal is alive.]
        """        
        return self._energy > 0 and self._age < self._parameters.max_age

    def move_to(self, patch:Patch):
        """[Moves an animal from current patch to another. It checks if an animal is alive,
        if the patch is not the same patch and lastly if the animal is not of the same species.
        End of this process, it will add itself to the new patch.]

        Args:
            patch (Patch): [description]
        """        
        # Ensures that an animal must be alive for being able to move.
        assert self.is_alive()
        # Ensures that another patch is used.
        assert self.patch() != patch
        # Ensures that same type of animal is not on the patch.
        assert self.same_species_in(patch) != True
        # Ensures that the animal is remove from the patch it is coming from
        self._patch.remove(self)
        self._patch = patch
        # Ensures the animal is added to the new patch it is supposed to move to.
        self._patch.add(self)

    def patch(self) -> Patch:
        """[Enables the positioning of animals on patches.]

        Returns:
            Patch: [The position of the animal.]
        """    
        return self._patch

    def predatator_in(self, patch:Patch) -> bool:
        """[Checks if there is an predator on the patch. This will only be true for rabbits.]

        Args:
            patch (Patch): [Ensures access to the different patches.]

        Returns:
            bool: [True if a rabbit and a fox is on the same patch, False otherwise.]
        """    
        pass
 
    def same_species_in(self, patch:Patch) -> bool:
        
        pass

    def tick(self):
        """[Accounts for one step in the simulation and ensure aging and energy consumption of animals.]
        """    
        if self.is_alive():
            self._age += 1
            self._energy = (self._energy - self._parameters.metabolism)
        else:
            self.is_alive and self._energy <= 0 or self._parameters.max_age == True
            self.remove(self) 
  
class Fox(Animal):

    reproduction_cost_rate = 0.85
    food_energy_per_unit = 15


    def __init__(Animal, population: parameters.Population, patch: Patch, age: int):
        # Sets the initial max energy of population rabbits to 70 % of maximum value.
        energy = round(population.max_energy * 0.70)
        ## Super is used to declare that this is a subclass from class Animals.
        # To ensure that the same goes into the subclass, we initiate the super class contructor to ensure alignment between these two.
        super().__init__(population, age, energy, patch)

    def predators_in(self, path:Patch) -> bool:
        """[Foxes dont have any predators, therefore this always returns False.]

        Args:
            path (Patch): [description]

        Returns:
            bool: [description]
        """        
        return False
    
    def same_species_in(self, patch: Patch) -> bool:
        
        return patch.has_alive_fox

    def reproduction_cost_rate(self):
        pass



class Rabbit(Animal):

    reproduction_cost_rate = 0.85
    feedingMetabolismRate = 2.5

    def __init__(self, population: parameters.Population, patch: Patch, age: int):
        
        # Initial energy for population rabbits is set to 25 % of maximum value.
        energy = round(population.max_energy * 0.25)

        ## Super is used to declare that this is a subclass from class Animals.
        # To ensure that the same goes into the subclass, we initiate the super class contructor to ensure alignment between these two.
        super().__init__(population, age, energy, patch)
        self._slayRabbit = False
    
    def same_species_in(self, patch:Patch) -> bool:
        """[Checks of there is another rabbit on the patch.]

        Args:
            patch (Patch): [Position of an animal.]

        Returns:
            bool: [True if there is another rabbit else False.]
        """    
        return patch.has_alive_rabbit
    
    def food_energy_per_unit(self):
        pass

    def reproduction_cost_rate(self):
        pass

    
    def slayRabbit(self):
        """[Kills the rabbit and removes it from the patch.]
        """        
        self._slayRabbit = True
        self._patch.remove(self)

    def was_killed(self) -> bool:
        """[Checks if the rabbit had an dramatic ending of their unisex life or not.]

        Returns:
            bool: [description]
        """    
        return self._slayRabbit
