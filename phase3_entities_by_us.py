from typing import Optional, Tuple
import parameters
import random


## Create entitites module
class Patch:
    """[A class for making a patch of grass on a specifk cordinate, with the posiblity of adding foxes and rabbits to it]

    Returns:
        [Patch]: [The patch og grass on a specif cordinat]
    """
    # This saves memory and secure your class so it does not get more attibuts 
    __slots__= ('_coordinates','_foxes','_rabbits','_grass')

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
        self._foxes = []  # Det kun en vlrdi den skal indeholde så tænker ikke at lave det til en liste
        self._rabbits = []
        # Inserts some random amount of grass ----> Tænker vi skal have en mimimum værdi af grass (fx max greassGrowthh)
        self._grass = random.randrange(Patch.maxGrassGrowthh,Patch.maxGrassAmout)

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
        """[Making the grass grow]
        """

        if self._grass < self.maxGrassAmout:
            grassGrowth = self._grass + random.randrange(self.minGrassGrowth, self.maxGrassGrowthh)
            self._grass = min(grassGrowth, self.maxGrassAmout)

    def _has_alive_fox(self) -> bool:
        """[Checks the list of foxes, to see whether or not it is alive through is_alive function call]

        Returns:
            bool: [If fox is alive, return True, else False.]
        """        
        if self._foxes:
            return self._foxes[0].is_alive()
        else: 
            return False

    def _has_alive_rabbit(self) -> bool:
        """[Checks the list of rabbits, to see whether or not it is alive through is_alive function call.]

        Returns:
            [bool]: [If rabbit is alive, return True, else False.]
        """        
        if self._rabbits:
            return self._rabbits[0].is_alive()
        else: 
            return False

    def _animalPopulation(self, animal):
        """[Adds an animal type to the one of the followings lists in class:Patch constructor - _foxes or _rabbtis.
        This is also used to verify whether or not an animal is alive]

        Args:
            animal ([Integer]): [Can be either a fox or rabbit.]

        Returns:
            [List]: [description]
        """        
        if not animal in self.animals():
            if type(animal) is Fox: 
                self._foxes.append(animal)
            else:
                self._rabbits.append(animal)


    def animals(self):
        """[Validates to see if which kind of animals is on the a patch.]

        Returns:
            [List]: [An updated list for both foxces and rabbits.]
        """        
        return self._rabbits + self._foxes

    def add(self, animal):
        """[Adds an animal, either fox or rabbit to the total population.]

        Args:
            animal ([List]): [List of animals.]
        """        
        if not animal in self.animals():
            if type(animal) is Fox: 
                self._foxes.append(animal)
            else:
                self._rabbits.append(animal)
        
    def remove(self, animal):
        """[Removes an animal, can be either fox or rabbit.]

        Args:
            animal ([Integer]): [List of animals.]
        """        
        if animal in self.animals():
            if type(animal) is Fox: 
                self._foxes.remove(animal)
            else:
                self._rabbits.remove(animal)

class Animal:
    """[summary]
    """
    # This saves memory and secure your class so it does not get more attibuts 
    __slots__= ('_parameters','_energy','_age','_patch')

    def __init__(self, population: parameters.Population, patch: Patch, energy: int, age: int):
        """[summary]

        Args:
            population (parameters.Population): [description]
            patch (Patch): [description]
            energy (int): [description]
            age (int): [description]
        """    
        self._parameters    = population
        self._energy        = energy
        self._age           = age
        self._patch         = patch
        self._patch.add(self)
        
    def age(self) -> int:
        """[Enables the tracking of age for each individual]

        Returns:
            int: [The age of each individual in for each species.]
        """        
        return self._age

    def energy(self) -> int:
        """[Tracking of an species energy level.]

        Returns:
            int: [Returns species energy level.]
        """    
        return self._energy

    def patch(self) -> Patch:
        """[Enables the positioning of animals on patches.]

        Returns:
            Patch: [The position of the animal.]
        """    
        return self._patch

    def is_alive(self) -> bool:
        """[Function that checks if a an animal is alive, if not not it return False otherwise True.]

        Returns:
            bool: [True or False depending on whether or not the animal is alive.]
        """        
        pass

    def can_reproduce(self) -> bool:
        """[Checks if an animal is alive and validates reproduction criterias according to parameters for minimum energy and age with a True/False.]

        Returns:
            bool: [True if an animal can reproduce else False.]
        """        
        return self.is_alive() and self.energy() >= self._parameters.reproduction_min_energy and self.age() >= self._parameters.reproduction_min_age

    def tick(self):
        """[Accounts for one step in the simulation and ensure aging and energy consumption of animals.]
        """    
        if self.is_alive():
            self._age += 1
            #If the energy used makes the energy negativ we hold it to zero insted. 
            self._energy = max(0, self._energy - self._parameters.metabolism)
            if not self.is_alive():
                self._patch.remove(self)
        else:
            self._patch.remove(self) 

    def move_to(self, patch: Patch):
        """[Moves an animal from current patch to another. It checks if an animal is alive,
        if the patch is not the same patch and lastly if the animal is not of the same species.
        End of this process, it will add itself to the new patch.]

        Args:
            patch (Patch): [description]
        """        
        # Ensures that an animal must be alive for being able to move.
        if self.is_alive():
            # Ensures that the animal is remove from the patch it is coming from
            self._patch.remove(self)
            self._patch = patch
            # Ensures the animal is added to the new patch it is supposed to move to.
            self._patch.add(self)    

    def same_species_in(self, patch: Patch) -> bool:
        """[Checks if a patch is having the same type of animal on it.]

        Args:
            patch (Patch): [Positional placement of a given patch.]

        Returns:
            bool: [True or False depending on the same species is within or not]
        """
        # This works because it is being specified independently for each animal.        
        pass

    def predators_in(self, patch:Patch) -> bool:
        """[Checks if there is an predator on the patch. This will only be true for rabbits.]

        Args:
            patch (Patch): [Ensures access to the different patches.]

        Returns:
            bool: [True if a rabbit and a fox is on the same patch, False otherwise.]
        """    
        # This works because it is being specified independently for each animal.
        pass


    def feed(self):
        """[Feeds an animal with available ressourcer on the patch. Is unique for each animal.]
        """        
        # This works because it is being specified independently for each animal.
        pass

    def reproduce(self, newbornPatch: Patch) -> Optional["Animal"]:
        """[Handles the scenario when a newborn is being born into the simulation or none.]

        Args:
            patch (Patch): [The position of the animal.]

        Returns:
            [Integer]: [A newborn rabbit or foxes.]
        """
        # This works because it is being specified independently for each animal.
        pass


class Fox(Animal):
    """[summary]

    Args:
        Animal ([type]): [description]

    Returns:
        [type]: [description]
    """

    __slots__= ()

    reproduction_cost_rate = 0.85
    food_energy_per_unit = 15


    def __init__(Animal, population: parameters.Population, patch: Patch, age: int):
        """[summary]

        Args:
            Animal ([type]): [description]
            population (parameters.Population): [description]
            patch (Patch): [description]
            age (int): [description]
        """    
        # Sets the initial max energy of population rabbits to 70 % of maximum value.
        energy = round(population.max_energy * 0.7)
        ## Super is used to declare that this is a subclass from class Animals.
        # To ensure that the same goes into the subclass, we initiate the super class contructor to ensure alignment between these two.
        super().__init__(population, patch, energy, age)

    def is_alive(self) -> bool:
        """[Function that checks if a an animal is alive, if not not it return False otherwise True.]

        Returns:
            bool: [True or False depending on whether or not the animal is alive.]
        """      

        return self.energy() > 0 and self.age() < self._parameters.max_age

    def feed(self):
        """[Feeding functionality for the fox population.]
        """    
        animal = self._patch._rabbits
        if animal:
            #Kills the animal on the same patch as the fox
            animal[0].kill()
            #Calculate the totalt energy the fox got from eating the rabbit
            energy_total = self.energy() + self.food_energy_per_unit
            # if the total energy exceed the max energy we keep the max energy
            self._energy = min(self._parameters.max_energy, energy_total)
    
    def reproduce(self, newborn_patch: Patch) -> Optional["Fox"]:
        """[Provides a newborn fox into the simulation with respect to preconditions.]

        Returns:
            [entities.Fox]: [A newborn fox]
        """
        # Tjeks if the fox can reproduce
        if self.can_reproduce() and \
        random.choices([True,False], cum_weights = [self._parameters.reproduction_probability,1], k = 1):
        # The energy used for reproducsen is substracted
            self._energy = round(self.energy() - self._parameters.reproduction_min_energy * self.reproduction_cost_rate)
            return Fox(self._parameters, newborn_patch, 0)
        else:
            return None


    def predators_in(self, path: Patch) -> bool:
        """[Foxes dont have any predators, therefore this always returns False.]

        Args:"
            path (Patch): [description]

        Returns:
            bool: [description]
        """        
        return False


class Rabbit(Animal):
    """[summary]

    Args:
        Animal ([type]): [description]

    Returns:
        [type]: [description]
    """

    __slots__= ('_killed')

    reproduction_cost_rate  = 0.85
    feeding_Metabolism_Rate   = 2.5

    def __init__(self, population: parameters.Population, patch: Patch, age: int):
        """[summary]

        Args:
            population (parameters.Population): [description]
            patch (Patch): [description]
            age (int): [description]
        """        
        # Initial energy for population rabbits is set to 25 % of maximum value.
        energy = round(population.max_energy * 0.25)

        ## Super is used to declare that this is a subclass from class Animals.
        # To ensure that the same goes into the subclass, we initiate the super class contructor to ensure alignment between these two.
        super().__init__(population, patch, energy, age)
        self._killed = False
    
    def was_killed(self) -> bool:
        """[Checks if the rabbit had an dramatic ending of their unisex life or not.]

        Returns:
            bool: [Ture fox killed it False it keeps on fucking]
        """    
        return self._killed

    def kill(self):
        """[Tjeks if the rabbits is alive and kills it and remove it from the patch]
        """        
        if self.is_alive():
            self._killed = True
            self._patch.remove(self)

    def is_alive(self):
        """[Function that checks if a an animal is alive, if not not it return False otherwise True.]

        Returns:
            bool: [True or False depending on whether or not the animal is alive.]
        """
        return self.energy() > 0 and self.age() < self._parameters.max_age and not self.was_killed()

    def same_species_in(self, patch: Patch) -> bool:
        """[Checks of there is another rabbit on the patch.]

        Args:
            patch (Patch): [Position of an animal.]

        Returns:
            bool: [True if there is another rabbit else False.]
        """    
        return patch.has_alive_rabbit()
    
    def feed(self):
        """[summary]
        """        
        if self.is_alive():
            eating = self.patch()
            # Gives us how many times the rabbit can eat the grass 
            grass_limit = round(self.feeding_Metabolism_Rate * self._parameters.metabolism)
            for turn in range(grass_limit):
                # Tjeks if there is sill grass and if the max energt it reach 
                if eating.grass() > 0 and self.energy() < self._parameters.max_energy:
                    eating._grass   -= 1
                    self._energy    += 1

    def reproduce(self, newborn_patch: Patch) -> Optional["Rabbit"]:
        """[summary]

        Returns:
            [type]: [description]
        """
        # Tjeks if the rabbit can reproduce
        if self.can_reproduce() and random.choices([True,False], cum_weights = [self._parameters.reproduction_probability, 1], k = 1):
            # The energy used for reproducsen is substracted
            self._energy = round(self.energy() - self._parameters.reproduction_min_energy * self.reproduction_cost_rate)
            return Rabbit(self._parameters, newborn_patch, 0)
        else:
            return None

    def predators_in(self, patch: Patch) -> bool:
        """[A function that inspected the patch for predators]

        Args:
            patch (Patch): [The patch that is going to be inspected]

        Returns:
            bool: [Ture if there is a predator, False if not]
        """    
        return patch.has_alive_fox()

