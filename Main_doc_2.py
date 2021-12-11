
import simulation
import reporting
from parameters import Execution, Simulation, World, Population
import sys
import math


def is_int2(user_input):
    """[This function valideates an input and handles potential errors for datatype int]

    Args:
        user_input ([int]): [Validates if a user input is an interger]

    Returns:
        [int]: [Returns input as integer]
    """
    try:
        return int(user_input)
    except ValueError:
        return is_int2(input("Please enter a valid integer: "))
    
    
    
def is_float(user_input):
    """[This function valideates an input and handles potential errors for datatype float]

    Args:
        user_input ([float]): [Validates if a user input is a float]

    Returns:
        [float]: [Returns input as float]
    """
    try:
        return float(user_input)
    except ValueError:
        return is_float(input("Please enter a valid value: "))

def is_bool(user_input):  
    """[This function valideates an input and handles potential errors for datatype integer, and returns a boolean value]

    Args:
        user_input ([int]): [Validates if a user input is a integer]

    Returns:
        [bool]: [Returns input as bool]
    """
    # integer control in input
    user_input                              = is_int2(user_input)
    
    if user_input in [0, 1]:
        return bool(user_input)
    else:
        return is_bool(input("Please enter a valid binary value (0 or 1): "))
        

def above_value_i(user_input,ab):
    """[This function valideates an input to be above a certain value.]

    Args:
        user_input ([int]): [Will be an input from either quick setup]
        ab ([type]): [description]

    Returns:
        [int]: [description]
    """
    # interger control in input
    user_input                              = is_int2(user_input)
    if user_input>ab:
        return user_input
    else:
        return above_value_i(input("The value must be above {}: ".format(ab)),ab)
    
def above_value_f(user_input,ab):
    """[summary]

    Args:
        user_input ([float]): [description]
        ab ([type]): [description]

    Returns:
        [float]: [description]
    """
    # float control in input
    user_input                              = is_float(user_input)
    
    if user_input>ab:
        return user_input
    else:
        return above_value_f(input("The value must be above {}: ".format(ab)),ab)


def world_size(user_input,Call_place,sim):
    """[Function that handles the parameters for world configuration]

    Args:
        user_input ([int]): [User input]
        Call_place ([type]): [description]
        sim ([Class]): [Accesses and stores new values for simulation]

    Returns:
        [int]: [The new stored values for world size]
    """
    # integer kontrol of input
    user_input                              = is_int2(user_input)
    
    # Getting the minimum value of the world area of the world
    limit_pop                               = max([int(sim.rabbits.initial_size),int(sim.foxes.initial_size)])
    
    # calculation of the minimum value of the world in in one dimension
    limit_above                             = math.ceil(limit_pop/int(getattr(sim.world,Call_place)))
    
    if int(limit_above) <= int(user_input):
        return user_input
    else:
        return world_size(input("The value must be {} or above: ".format(limit_above)),Call_place,sim)

def pop_size(user_input,sim):
    """[Function which checks that population size is not bigger than the world area andControls the integer inpput.]

    Args:
        user_input ([int]): [An input from user]
        sim ([Class]): [Accesses and stores new values for simulation]

    Returns:
        [int]: [If world area is less than population size, ]
    """
    # integer kontrol of input
    user_input                            = above_value_i(user_input,0)
    # Getting the limit for the population
    limit_pop                             = sim.world.area()
    
    if int(limit_pop) >= above_value_i(user_input,0):
        return user_input
    else:
        return pop_size(input("The value must be {} or below: ".format(limit_pop)),sim)


###############################

def main_menu(sim = Simulation()):
    """[Function that gives the simulation an menu to navigate]

    Args:
        sim ([Class], optional): [Accesses the default values from the module paramters]. Defaults to Simulation().
    """
    while True:

        user_input = is_int2(input("Options: Press a number, then enter to select\n1 Display parameter settings\n2 quick setup\n3 for advanced settings\n4 run\n5 for quit\n\n"))
        
        ## Default parameters 
        if user_input == 1:                                     # Prints values for either quick setup or advanced settings.
            print(sim.__str__())

        ## Quick setup
        elif user_input == 2:                                   # Takes user to quick setup simulation options.
            qs(sim)
        ## Advanced menu settings
        elif user_input == 3:                                   # Takes user to advanced_menu_settings to configure advanced setup.
            advanced_menu_settings(sim)
        ## Run simulation
        elif user_input == 4:                                   # Runs the simulation, this is not functional as of yet.
            dummy=simulation.run(sim) ## <---- not fixed yet
            reporting_menu(dummy)
        ## Exit program
        elif user_input == 5:                                   # Exits the program 
            sys.exit()
        ## Returns to main menu with default settings

def world_setup(sim):
    """[Function that configure the world setup. Here the user can choose the shape of the world, north/sount- and  west/east length.

    Args:
        sim ([Class]): [Accesses and stores new values into simulation ]
    """
    sim.world.is_toroid                     = is_bool(input("Island shape: 1 for Toroid, 0 for Square "))
    
    sim.world.west_east_length              = world_size(input("Insert vertifcal length from west to east "),"north_south_length",sim)
    
    sim.world.north_south_length            = world_size(input("Insert H length from west to east "),"west_east_length",sim)

    #print(sim.world.area())



def qs(sim):
    """[Function that creates the quick setup for simulation. Accesses and stores new values for species.initial_size, all execution and world parameters.]

    Args:
        sim ([class]): [description]
    """
    sim.rabbits.initial_size                =  pop_size(input("Rabbit populations: "),sim)
    
    sim.foxes.initial_size                  = pop_size(input("Fox populations: "),sim)
    
    exe(sim)
 
    world_setup(sim)

    print("Quick setup complete, returning to main menu")



def exe(sim):
    """[Function that gives access to configure the execution parameters for the simulation]

    Args:
        sim ([class]): [Accesses and stores new values into simulation.execution]
    """
    sim.execution.batch                     = is_bool(input("Batch: Vizualization(s) 1, 0 for none ")) 
        
    sim.execution.max_steps                 = above_value_i(input("Input maximum step for current simulation session "),0)

    sim.execution.step_delay                = above_value_f(input("Add a delay in seconds "),0)



def advanced_menu_settings(sim):
    """[Function that handles the advanced menu settings in the simulation.]

    Args:
        sim ([class]): [Imported module from parameters. Describes the simulation setup containing default values for all parameters.]

    Returns:
        [class]: [Returns the last configuration from the advanced menu settings]
    """
    while True:
        user_input = input("Options:\n1 World settings\n2 rabbit pupolation settings\n3 fox poplation settings\n4 execution settings\n5 return to main menu\n\n")

        if int(user_input) == 1:
            world_setup(sim)
        elif int(user_input) == 2:
            # rabbit setup
            ad_r(sim)
        elif int(user_input) == 3:
            # fox setup
            ad_f(sim)
        elif int(user_input) == 4:
            exe(sim)
        elif int(user_input) == 5:
            break
        else :
            print("pleas input a value between 1 and 5 ")
            


def ad_r(sim):
    """[Gives access to configure all parameters for rabbits in advanced settings and saves the new parameters in simulation]

    Args:
        sim ([class]): [Accesses and stores new values into simulation.rabbits]
    """

    sim.rabbits.initial_size                    = pop_size(input("Rabbit populations: "),sim)
    sim.rabbits.metabolism                      = above_value_i(input("Input rabbit metabolism: "),0)
    sim.rabbits.max_age                         = above_value_i(input("Input rabbit max age: "),0)           
    sim.rabbits.max_energy                      = above_value_i(input("Input rabbit max energy levels: "),0)
    sim.rabbits.reproduction_probability        = above_value_f(input("Input rabbit younglings probability "),0)
    sim.rabbits.reproduction_min_energy         = above_value_i(input("Input rabbit minimum energy for reproduction: "),0)
    sim.rabbits.reproduction_min_age            = above_value_i(input("Input rabbit age, for making mini rabbits: "),0)
       


def ad_f(sim):
    """[Gives access to configure all parameters for foxes in advanced settings]

    Args:
        sim ([class]): [Accesses and stores new values into simulation.foxes]
    """
    
    sim.foxes.initial_size                    = pop_size(input("Foxes populations: "),sim)
    sim.foxes.metabolism                      = above_value_i(input("Input foxes metabolism: "),0)
    sim.foxes.max_age                         = above_value_i(input("Input foxes max age: "),0)           
    sim.foxes.max_energy                      = above_value_i(input("Input foxes max energy levels: "),0)
    sim.foxes.reproduction_probability        = above_value_f(input("Input foxes younglings probability "),0)
    sim.foxes.reproduction_min_energy         = above_value_i(input("Input foxes minimum energy for reproduction: "),0)
    sim.foxes.reproduction_min_age            = above_value_i(input("Input foxes age, for making mini rabbits: "),0)
    


## Reporting menu for user interaction
def reporting_menu(results):
    """[Gives the user the options to select which kind of plot analyse they want]

    Args:
        results ([float]): [This will have the results from the simulation, for further analyzing]
    """    
    
    while True:
        print("Select plot to analyze\n1 Summary\n2 Population size\n3 Lifespan foxes and rabbits\n4 Energy consumption\n5 Kill plot \n6 Quit")
        
        user_input = (input("Select: "))
        if int(user_input) == 1:
            
            reporting.print_summary(results)
        elif int(user_input) == 2:
            
            reporting.plot_pop_size(results)
            
        elif int(user_input) == 3:
            
            reporting.plot_lifespan(results)
        elif int(user_input) == 4:
            
            reporting.plot_energy(results)
        elif int(user_input) == 5:
            
            reporting.plot_kills(results)
        elif int(user_input) == 6:
            sys.exit()
