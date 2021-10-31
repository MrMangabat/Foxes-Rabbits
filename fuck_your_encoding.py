class Simulation:
  """
  Describes the simulation setup (the world, the populations of rabbits and
  foxes, and its execution). Instance variables (world, rabbits, foxes, and
  execution) are initialised with an instance of the appropriate class (World,
  Population, or Execution) containing default values for all parameters.
  """

  __slots__ = [
    '_world',
    '_rabbits',
    '_foxes',
    '_execution'
    ]

  def __init__(self):
    self._world = World()
    self._rabbits = Population(
      'rabbits',
      100, # initial_size
      3,   # metabolism
      25,  # max_age
      45,  # max_energy
      .5,  # reproduction_rate
      5,   # reproduction_cost
      10,  # reproduction_age
      )
    self._foxes = Population(
      'foxes',
      30,  # initial_size
      2,   # metabolism
      50,  # max_age
      200, # max_energy
      .5,  # reproduction_rate
      120, # reproduction_cost
      10,  # reproduction_age
      )
    self._execution = Execution()

  @property
  def world(self):
    """
    Parameters for the simulated world. See class World.
    """
    return self._world

  @property
  def rabbits(self):
    """
    Parameters for the rabbit population. See class Population.
    """
    return self._rabbits

  @property
  def foxes(self):
    """
    Parameters for the fox population. See class Population.
    """
    return self._foxes

  @property
  def execution(self):
    """
    Parameters for the simulation execution. See class Execution.
    """
    return self._execution

  def __str__(self) -> str:
    return f"world: {self.world}\n{self.rabbits}\n{self.foxes}\nexecution: {self.execution}"

    
class World:
  """
  Describes the simulated 2D world in its shape (toroid or island) and size.

  See __init__ for defaults.
  """
  
  __slots__ = [
      'is_toroid',
      '_north_south_length',
      '_west_east_length'
      ]

  def __init__(self,
               north_south_length = 20,
               west_east_length = 20,
               is_toroid = True):
    self.is_toroid = is_toroid
    self.north_south_length = north_south_length
    self.west_east_length = west_east_length

  def shape(self) -> str:
    """
    Returns the name of the shape of the world ('toroid' or 'island').
    """
    return 'toroid' if self.is_toroid else 'island'
    
  @property
  def north_south_length(self) -> int:
    """
    The north-south length of the simulated world.
    
    Precondition: integer and non-negative.
    """
    return self._north_south_length

  @north_south_length.setter
  def north_south_length(self,length : int):
    self._north_south_length = length

  @property
  def west_east_length(self) -> int:
    """
    The west-east length of the simulated world.
    
    Precondition: integer and non-negative.
    """
    return self._west_east_length

  @west_east_length.setter
  def west_east_length(self,length : int):
    self._west_east_length = length

  def area(self) -> int:
    """
    Returns the total area of the world.
    """
    return self.north_south_length * self.west_east_length

  def __repr__(self):
    return f"World({self.north_south_length},{self.west_east_length},{self.is_toroid})"

  def __str__(self):
    return f"{self.shape()} {self.north_south_length} by {self.west_east_length}"
    
class Population:
  """
  Describes a population in the simulation (e.g., rabbits).
  """
 
  __slots__ = [
    '_species',
    '_max_age',
    '_metabolism',
    '_max_energy',
    '_initial_size',
    '_reproduction_probability',
    '_reproduction_min_energy',
    '_reproduction_min_age'
    ]

  def __init__(self,
               species,
               initial_size,
               metabolism,
               max_age,
               max_energy,
               reproduction_probability,
               reproduction_min_energy,
               reproduction_min_age):
    """
    Arguments: see the corresponding properties and data descriptors.
    """
    self._species = species
    self.initial_size = initial_size
    self.metabolism = metabolism
    self.max_age = max_age
    self.max_energy = max_energy
    self.reproduction_probability = reproduction_probability
    self.reproduction_min_energy = reproduction_min_energy
    self.reproduction_min_age = reproduction_min_age

  @property
  def species(self) -> str:
    """
    The population species (e.g.,'rabbits').
    """
    return self._species

  @property
  def initial_size(self) -> int:
    """
    The initial size of the populatio.
    
    Precondition: integer between 0 and the avaluable surface area.
    """
    return self._initial_size

  @initial_size.setter
  def initial_size(self,value):
    self._initial_size = value

  @property
  def metabolism(self) -> int:
    """
    The amount of energy consumed during each step of the simulation.

    Precondition: non-negative.
    """
    return self._metabolism

  @metabolism.setter
  def metabolism(self,value):
    self._metabolism = value

  @property
  def max_age(self) -> int:
    """
    The maximum age (in simulation steps) a member of this species can have.
    
    Precondition: integer and positive.
    """
    return self._max_age

  @max_age.setter
  def max_age(self,value):
    self._max_age = value

  @property
  def max_energy(self) -> int:
    """
    The maximum energy level a member of this species can have.

    Precondition: positive.
    """
    return self._max_energy

  @max_energy.setter
  def max_energy(self,value : int):
    self._max_energy = value

  @property
  def reproduction_probability(self) -> float:
    """
    The probability of reproduction when all conditions on age, energy, and environment are met.
    
    Precondition: a floating point value representing a probability.
    """
    return self._reproduction_probability

  @reproduction_probability.setter
  def reproduction_probability(self,value):
    self._reproduction_probability = value

  
  @property
  def reproduction_min_age(self) -> int:
    """
    The minimum age an individual must have in order to reproduce.
    """
    return self._reproduction_min_age

  @reproduction_min_age.setter
  def reproduction_min_age(self,value):
    self._reproduction_min_age = value

  
  @property
  def reproduction_min_energy(self) -> int:
    """
    The minimum energy level an individual must have in order to reproduce.
    """
    return self._reproduction_min_energy

  @reproduction_min_energy.setter
  def reproduction_min_energy(self,value):
    self._reproduction_min_energy = value

  def __repr__(self) -> str:
    return "Population('{}', {}, {}, {}, {}, {}, {}, {})".format(
      self.species,
      self.initial_size,
      self.metabolism,
      self.max_age,
      self.max_energy,
      self.reproduction_probability,
      self.reproduction_min_energy,
      self.reproduction_min_age)

  def __str__(self) -> str:
    return f"""{self.species}: {self.initial_size}
  metabolism:    {self.metabolism}
  max_age:       {self.max_age}
  max_energy:    {self.max_energy}
  reproduction:
    probability: {self.reproduction_probability}
    cost:        {self.reproduction_min_energy}
    age:         {self.reproduction_min_age}"""

class Execution:
  """
  Contains parameters for the simulation execution.

  See __init__ for defaults.
  """
  
  __slots__ = [
      '_max_steps',
      '_step_delay',
      '_batch'
      ]

  def __init__(self,
               max_steps = 1000,
               step_delay = 0.1,
               batch = True):
    self.max_steps = max_steps
    self.step_delay = step_delay
    self.batch = batch

  @property
  def max_steps(self) -> int:
    """
    The maximum number of steps the simulation can run for.
    """
    return self._max_steps

  @max_steps.setter
  def max_steps(self,value):
    self._max_steps = value


  @property
  def step_delay(self) -> float:
    """
    A delay (in seconds) added to each step of the simulation.
    """
    return self._step_delay

  @step_delay.setter
  def step_delay(self,value):
    self._step_delay = value


  @property
  def batch(self) -> bool:
    """
    Whether the simulation executed in batch mode (no visualization) or visualising its status.
    """
    return self._batch

  @batch.setter
  def batch(self,value):
    self._batch = value

  def mode(self) -> str:
    """
    Returns the mode of execution (batch or visual) as a string.
    """
    return 'batch' if self.batch else 'visual'

  def __repr__(self) -> str:
    return f"Execution({self.max_steps},{self.step_delay},{self.batch})"

  def __str__(self) -> str:
    return f"{self.mode()} mode, {self.max_steps} steps with a delay {self.step_delay}s"
