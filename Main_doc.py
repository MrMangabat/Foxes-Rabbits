
# import os 
# Path_to_files=os.path.realpath(__file__)

# Path_to_files=Path_to_files.replace("\\"+os.path.basename(__file__),"")

# os.setchdir=Path_to_files

import simulation
import reporting
from parameters import Execution, Simulation, World, Population
import sys
import math



def is_int2(user_input):
    """
    

    Parameters
    ----------
    user_input : Positiv integer 
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    try:
        return int(user_input)
    except ValueError:
        return is_int2(input("Please enter a valid integer: "))
    
    
    
def is_float(user_input):
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    try:
        return float(user_input)
    except ValueError:
        return is_float(input("Please enter a valid value: "))

def is_bool(user_input):  
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # integer control in input
    user_input                              = is_int2(user_input)
    
    if user_input in [0, 1]:
        return bool(user_input)
    else:
        return is_bool(input("Please enter a valid binary value (0 or 1): "))
        

def above_value_i(user_input,ab):
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.
    ab : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # interger control in input
    user_input                              = is_int2(user_input)
    if user_input>ab:
        return user_input
    else:
        return above_value_i(input("The value must be above {}: ".format(ab)),ab)
    
def above_value_f(user_input,ab):
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.
    ab : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # float control in input
    user_input                              = is_float(user_input)
    
    if user_input>ab:
        return user_input
    else:
        return above_value_f(input("The value must be above {}: ".format(ab)),ab)


def world_size(user_input,Call_place,sim):
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.
    Call_place : TYPE
        DESCRIPTION.
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

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
    """
    

    Parameters
    ----------
    user_input : TYPE
        DESCRIPTION.
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    # integer kontrol of input
    user_input                            = is_int2(user_input)
    # Getting the limit for the population
    limit_pop                             = sim.world.area()
    
    if int(limit_pop) >= int(user_input):
        return user_input
    else:
        return pop_size(input("The value must be {} or below: ".format(limit_pop)),sim)


###############################

def main_menu(sim = Simulation()):
    """
    

    Parameters
    ----------
    sim : TYPE, optional
        DESCRIPTION. The default is Simulation().

    Returns
    -------
    None.

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
    """
    

    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    sim.world.is_toroid                     = is_bool(input("Island shape: 1 for Toroid, 0 for Square "))
    
    sim.world.west_east_length              = world_size(input("Insert vertifcal length from west to east "),"north_south_length",sim)
    
    sim.world.north_south_length            = world_size(input("Insert H length from west to east "),"west_east_length",sim)



def qs(sim):
    """
    

    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    sim.rabbits.initial_size                =  pop_size(input("Rabbit populations: "),sim)
    
    sim.foxes.initial_size                  = pop_size(input("Fox populations: "),sim)
    
    exe(sim)
 
    world_setup(sim)

    print("Quick setup complete, returning to main menu")



def exe(sim):
    """
    

    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    sim.execution.batch                     = is_bool(input("Batch: Vizualization(s) 1, 0 for none ")) 
        
    sim.execution.max_steps                 = above_value_i(input("Input maximum step for current simulation session "),0)

    sim.execution.step_delay                = above_value_f(input("Add a delay in seconds "),0)



def advanced_menu_settings(sim):
    """
    

    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

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
    """
    
    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    sim.rabbits.initial_size                    = pop_size(input("Rabbit populations: "),sim)
    sim.rabbits.metabolism                      = above_value_i(input("Input rabbit metabolism: "),0)
    sim.rabbits.max_age                         = above_value_i(input("Input rabbit max age: "),0)           
    sim.rabbits.max_energy                      = above_value_i(input("Input rabbit max energy levels: "),0)
    sim.rabbits.reproduction_probability        = above_value_f(input("Input rabbit younglings probability "),0)
    sim.rabbits.reproduction_min_energy         = above_value_i(input("Input rabbit minimum energy for reproduction: "),0)
    sim.rabbits.reproduction_min_age            = above_value_i(input("Input rabbit age, for making mini rabbits: "),0)
    


        

def ad_f(sim):
    """
    

    Parameters
    ----------
    sim : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    
    sim.foxes.initial_size                    = pop_size(input("Rabbit populations: "),sim)
    sim.foxes.metabolism                      = above_value_i(input("Input foxes metabolism: "),0)
    sim.foxes.max_age                         = above_value_i(input("Input foxes max age: "),0)           
    sim.foxes.max_energy                      = above_value_i(input("Input foxes max energy levels: "),0)
    sim.foxes.reproduction_probability        = above_value_f(input("Input foxes younglings probability "),0)
    sim.foxes.reproduction_min_energy         = above_value_i(input("Input foxes minimum energy for reproduction: "),0)
    sim.foxes.reproduction_min_age            = above_value_i(input("Input foxes age, for making mini rabbits: "),0)
    

       

## Reporting menu for user interaction
def reporting_menu(results):
    '''
    Gives the user the options to select which kind of plot analyse they want
    '''
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


main_menu()
