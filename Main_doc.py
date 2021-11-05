
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
    try:
        return int(user_input)
    except ValueError:
        return is_int2(input("Please enter a valid integer: "))
    
    
    
def is_float(user_input):
    try:
        return float(user_input)
    except ValueError:
        return is_float(input("Please enter a valid value: "))

def is_bool(user_input):  

    user_input=is_int2(user_input)
    if user_input in [0, 1]:
        return bool(user_input)
    else:
        return is_bool(input("Please enter a valid binary value (0 or 1): "))
        

def above_value_i(user_input,ab):
    
    user_input=is_int2(user_input)
    if user_input>ab:
        return user_input
    else:
        return above_value_i(input("The value must be above {}: ".format(ab)),ab)
    
def above_value_f(user_input,ab):
    
    user_input=is_float(user_input)
    if user_input>ab:
        return user_input
    else:
        return above_value_f(input("The value must be above {}: ".format(ab)),ab)


def world_size(user_input,Call_place,sim):

    user_input=is_int2(user_input)
    
    limit_pop=max([int(sim.rabbits.initial_size),int(sim.foxes.initial_size)])
    limit_above=math.ceil(limit_pop/int(getattr(sim.world,Call_place)))
    
    if int(limit_above) <= int(user_input):
        return user_input
    else:
        return world_size(input("The value must be {} or above: ".format(limit_above)),Call_place,sim)

def pop_size(user_input,sim):
    
    user_input=is_int2(user_input)
    limit_pop=sim.world.area()
    
    if int(limit_pop) >= int(user_input):
        return user_input
    else:
        return pop_size(input("The value must be {} or below: ".format(limit_pop)),sim)


###############################

def main_menu(sim = Simulation()):
    while True:
        """Function that containt main menu settings.

        Args:
            sim ([int], optional): [Updates simulation values if quick set has been used. Same occurs if advanced settings have been used]. Defaults to Simulation values().
        """    
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

def validate_bool_input(input):                             # Validates boolean for worl_setup, 1/true = toroid or 2/false = square
    """Function validates bool input

    Args:
        input ([bool]): [True or False statement]

    Raises:
        ValueError: [User should use 1 or 0 to decide whether or not it is true or false instead of strings or integers.]

    Returns:
        [bool]: [True or False]
    """    
    if input in [1, 0]:
        return bool(input)
    else:
        raise ValueError("Invalid input ")



def world_setup(sim):
    """Function containing confiquration for world settings

    Returns:
        [int]: [Width and length of the world]
        [bool]: [If bool = True, returns toroid shape, else a square/simple island shape]
    """
    
    sim.world.is_toroid = is_bool(input("Island shape: 1 for Toroid, 0 for Square "))
    
    sim.world.west_east_length = world_size(input("Insert vertifcal length from west to east "),"north_south_length",sim)
    
    sim.world.north_south_length  = world_size(input("Insert H length from west to east "),"west_east_length",sim)



def qs(sim):
    """[Function that greates a quick setup for the simulation of foxes and rabbits.\nUser will only have acces to set rabbit, fox population, duration of the simulation and simulation mode]
    """    

    sim.rabbits.initial_size =  pop_size(input("Rabbit populations: "),sim)
    
    sim.foxes.initial_size =    pop_size(input("Fox populations: "),sim)
    
    exe(sim)
 
    world_setup(sim)

    print("Quick setup complete, returning to main menu")



def exe(sim):
        
    sim.execution.batch = is_bool(input("Batch: Vizualization(s) 1, 0 for none ")) 
        
    sim.execution.max_steps = above_value_i(input("Input maximum step for current simulation session "),0)

    sim.execution.step_delay =above_value_f(input("Add a delay in seconds "),0)



def advanced_menu_settings(sim):
    """A Function that contains advanced menu settings

    Returns:
        [int]: [User navigates menu with intergers and commit their choices with "Enter"]
    """
    while True:
        user_input = input("Options:\n1 World settings\n2 rabbit pupolation settings\n3 fox poplation settings\n4 execution settings\n5 return to main menu\n\n")

        if int(user_input) == 1:
            world_setup(sim)
            ##Husk at send instansen rundt i funktionerne, lav ikke en ny. 
        elif int(user_input) == 2:
            ad_r(sim)
        elif int(user_input) == 3:
            ad_f(sim)
        elif int(user_input) == 4:
            exe(sim)
        elif int(user_input) == 5:
            break
        else :
            print("pleas input a value between 1 and 5 ")
            




def ad_r(sim):
    """Function that takes user through all variables rabbits have for simulation. User will have to set all parameters pr. rotation.\n
    init_s_r = initial size rabbit.\n
    meta_r = metabolism rabbit.\n
    max_age_r = maximum age rabbit.\n
    ene_r = maximum energy level rabbit.\n
    repro_prop_r = reproduction probability rate.\n
    repro_m_e_r = reproduction minimal energy rate --> Explain the min. amount of energy needed to make babies.\n
    repro_fer_r = reproduction fertility age --> Explain the minimum age for reproduction.\n

    Returns:
        [int]: [Describes the entire population for simulation]
    """
    
    sim.rabbits.initial_size                    = pop_size(input("Rabbit populations: "),sim)
    sim.rabbits.metabolism                      = above_value_i(input("Input rabbit metabolism: "),0)
    sim.rabbits.max_age                         = above_value_i(input("Input rabbit max age: "),0)           
    sim.rabbits.max_energy                      = above_value_i(input("Input rabbit max energy levels: "),0)
    sim.rabbits.reproduction_probability        = above_value_f(input("Input rabbit younglings probability "),0)
    sim.rabbits.reproduction_min_energy         = above_value_i(input("Input rabbit minimum energy for reproduction: "),0)
    sim.rabbits.reproduction_min_age            = above_value_i(input("Input rabbit age, for making mini rabbits: "),0)
    


        

def ad_f(sim):
    """Function that takes user through all variables rabbits have for simulation. User will have to set all parameters pr. rotation.\n
    init_s_r = initial size rabbit.\n
    meta_r = metabolism rabbit.\n
    max_age_r = maximum age rabbit.\n
    ene_r = maximum energy level rabbit.\n
    repro_prop_r = reproduction probability rate.\n
    repro_m_e_r = reproduction minimal energy rate --> Explains the min. amount of energy needed to make babies.\n
    repro_fer_r = reproduction fertility age --> Explains the minimum age for reproduction.\n

    Returns:
        [int]: [Describes the entire population for simulation]
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
    Gives the user the options to select which menu they want to analyse
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