
# import os 
# Path_to_files=os.path.realpath(__file__)

# Path_to_files=Path_to_files.replace("\\"+os.path.basename(__file__),"")

# os.setchdir=Path_to_files

import simulation
import reporting
import parameters 
import sys
import math


def is_int2(user_input): # Use case 1
    """[This function valideates and convers the user_input to an integer and handles potential errors by getting the user to chouse again]

    Args:
        user_input ([str]): [takes the users choise as a string variable]

    Returns:
        [int]: [Returns user_input as integer]
    """
    
    # We use the comand try to catch when the int comando would have failed and give the user a secound chance to input a valid interger 
    try:
        return int(user_input)
    except ValueError:
        return is_int2(input("Please enter a valid integer: "))
    
def is_float(user_input): # Use case 2
    """[This function valideates and convers the user_input to float and handles potential errors by getting the user to chouse again]

    Args:
        user_input ([str]): [takes the users choise as a string variable]

    Returns:
        [float]: [Returns user_input as float]
    """
    # We use the comand try to catch when the float comando would have failed and give the user a secound chance to input a valid float 
    try:
        return float(user_input)
    except ValueError:
        return is_float(input("Please enter a valid float: "))

def is_bool(user_input): # Use case 3
    """[This function checks if the input is binary and convers the input to a bool variable. The function also handles potential errors by getting the user to chouse again if its falis the check]

    Args:
        user_input ([str]): [takes the users choise as a string variable]

    Returns:
        [bool]: [Returns user_input as bool]
    """
    # is_int2 convers the string user_input to a integer and check if the user_input is a valid integer 
    user_input                              = is_int2(user_input)
    
    # checks if user_input is binary
    if user_input in [0, 1]:
        return bool(user_input)
    else:
        return is_bool(input("Please enter a valid binary value (0 or 1): "))

def above_value_i(user_input,above): # Use case 4
    """[This function valideates an integer input to be above a certain value]

    Args:
        user_input ([str]): [user input as string from the user]
        above ([int]): [The value the user_input have to be above]

    Returns:
        [int]: [The controled value]
    """
    # interger control of user_input
    user_input                              = is_int2(user_input)
    # checks if user_input is above the variable "above"
    if user_input>above:
        return user_input
    else:
        return above_value_i(input("The value must be above {}: ".format(above)),above)
    
def above_value_f(user_input,above): # Use case 5
    """[This function valideates an float input to be above a certain value]

    Args:
        user_input ([str]): [user input as string from the user]
        above ([int]): [The value the user_input have to be above]

    Returns:
        [float]: [The controled value]
    """
    # float control of user_input
    user_input                              = is_float(user_input)
    
    # checks if user_input is above the variable "above"
    if user_input > above:
        return user_input
    else:
        return above_value_f(input("The value must be above {}: ".format(above)),above)
    
def validate_percentage_input(user_input): # Use case 6
    """[Validate an convert user_input to a floating and control if it is between 0 and 1]
        
    Args:
        user_input ([str]): [user input as string from the user]

    Returns:
        [float]: [The controled value]
    """
    
    # float control in input
    user_input                              = is_float(user_input)
    
    # checks if the user_inout is between 0 and 1
    if user_input >= 0 and user_input <= 1.0:
        return user_input
    else:
        return validate_percentage_input(input("Please enter a valid value (between 0.0 and 1.0): "))

def world_size(user_input,Call_place,sim): # Use case 7
    """[Function control and validate that the user_input is an integer and fulfills the condition of the world being big enough for the population ]
    Args:
        user_input ([str]): [User input as string of the user]
        Call_place ([str]): [Attribiuts instans]
        sim ([Class]): [A class from the module parameters called Simulation used here to get a varible]
    Returns:
        [int]: [The controld integer value]
    """
    # integer kontrol of user_input
    user_input                              = is_int2(user_input)
    
    # Getting the minimum value of the world area of the world
    limit_pop                               = max([int(sim.rabbits.initial_size),int(sim.foxes.initial_size)])
    
    # calculation of the minimum value of the world in one dimension when the other is set
    limit_above                             = math.ceil(limit_pop/int(getattr(sim.world,Call_place)))
    
    # controls the user_input is above the minimum lenght for the population to exist
    if int(limit_above) <= user_input:
        return user_input
    else:
        return world_size(input("The value must be {} or above: ".format(limit_above)),Call_place,sim)

def pop_size(user_input,sim): # Use case 8
    """[Function which checks that population size is not bigger than the world area and Controls if the user_input is a integer]
    Args:
        user_input ([str]): [An input from user]
        sim ([Class]): [A class from the module parameters called Simulation used here to get a varible]
    Returns:
        [int]: [The controled integer]
    """
    # integer kontrol of input
    user_input                            = above_value_i(user_input,0)
    # Getting the limit for the population
    limit_pop                             = sim.world.area()
    
    # checks if he user_input is below the limit for the population (limit_pop)
    if int(limit_pop) >= user_input:
        return user_input
    else:
        return pop_size(input("The value must be {} or below: ".format(limit_pop)),sim)

###############################

def main_menu(sim = parameters.Simulation()): # Use case 9
    """[Function that initialize the parameters.Simulation and open a menu to navigate the program]
    Args:
        sim ([Class]): [A class from the module parameters called Simulation used here to initialize our simulation and set the standart values]
    """
    
    # While loop to get around the control of the user_input.
    while True:
        
        # User input to navigate the choises 
        user_input = input("Options: Press a number, then enter to select\n1 Display parameter settings\n2 quick setup\n3 for advanced settings\n4 run\n5 for quit\n\n")
        
        ## Display parameters 
        if user_input == "1":                                     # Prints values for either quick setup or advanced settings.
            print(sim.__str__())
        ## Quick setup
        elif user_input == "2":                                   # Takes user to quick setup simulation options.
            qs(sim)
        ## Advanced menu settings
        elif user_input == "3":                                   # Takes user to advanced_menu_settings to configure advanced setup.
            advanced_menu_settings(sim)
        ## Run simulation
        elif user_input == "4":                                   # Runs the simulation, this is not functional as of yet.
            dummy=simulation.run(sim)
            reporting_menu(dummy)
        ## Exit program
        elif user_input == "5":                                   # Exits the program 
            done()
            sys.exit()
        else :
            print("\nPleae input value between 1 and 5 \n")
        ## Returns to main menu with default settings

def world_setup(sim): # Use case 10
    """[Function that configure the world setup. Here the user can choose the shape of the world, north/sount- and  west/east length.
    Args:
        sim ([Class]): [A class from the module parameters called Simulation used here to set and forward in the function used]
    """
    sim.world.is_toroid                     = is_bool(input("Island shape: 1 for Toroid, 0 for Square "))
    
    sim.world.west_east_length              = world_size(input("Insert west-east length: "),"north_south_length",sim)
    
    sim.world.north_south_length            = world_size(input("Insert north-south length: "),"west_east_length",sim)


def qs(sim): # Use case 11
    """[Function that creates the quick setup our simulation class(sim). Accesses and stores new values for "species".initial_size.]
    Args:
        sim ([Class]): [A class from the module parameters called Simulation used here to set and forward in the function used]
    """
    
    sim.world.west_east_length              = above_value_i(input("Insert west-east length: "),0)
    
    sim.world.north_south_length            = above_value_i(input("Insert north-south length: "),0)
    
    sim.rabbits.initial_size                = pop_size(input("Rabbit populations: "),sim)
    
    sim.foxes.initial_size                  = pop_size(input("Fox populations: "),sim)
    
    exe(sim)
    
    print("Quick setup complete, returning to main menu")

def exe(sim): # Use case 12.
    """[Function that gives access to configure the execution parameters for the simulation]
    Args:
        sim ([class]): [A class from the module parameters called Simulation used here to set and forward in the function used]
    """
    sim.execution.batch                     = is_bool(input("Batch: Vizualization(s) 1, 0 for none ")) 
        
    sim.execution.max_steps                 = above_value_i(input("Input maximum step for current simulation session "),0)
    
    sim.execution.step_delay                = above_value_f(input("Add a delay in seconds "),0)

def advanced_menu_settings(sim): # Use case 13
    """[Function that handles the advanced menu settings in the simulation.]
    
    Args:
        sim ([class]): [A class from the module parameters called Simulation used here to forward in the function used]
        
    """
    while True:
        user_input = input("Options:\n1 World settings\n2 rabbit pupolation settings\n3 fox poplation settings\n4 execution settings\n5 return to main menu\n\n")
        
        if user_input == "1":
            world_setup(sim)
        elif user_input == "2":
            # rabbit setup
            ad_r(sim)
        elif user_input == "3":
            # fox setup
            ad_f(sim)
        elif user_input == "4":
            exe(sim)
        elif user_input == "5":
            break
        else :
            print("pleas input a value between 1 and 5 ")

def ad_r(sim): # Use case 14
    """[Gives access to configure all parameters for rabbits in advanced settings and saves the new parameters in simulation]
    
    Args:
        sim ([class]): [A class from the module parameters called Simulation used here to set and forward in the function used]
    """
    
    sim.rabbits.initial_size                    = pop_size(input("Rabbit populations: "),sim)
    sim.rabbits.metabolism                      = above_value_i(input("Input rabbit metabolism: "),0)
    sim.rabbits.max_age                         = above_value_i(input("Input rabbit max age: "),0)           
    sim.rabbits.max_energy                      = above_value_i(input("Input rabbit max energy levels: "),0)
    sim.rabbits.reproduction_probability        = validate_percentage_input(input("Input rabbit younglings probability "))
    sim.rabbits.reproduction_min_energy         = above_value_i(input("Input rabbit minimum energy for reproduction: "),0)
    sim.rabbits.reproduction_min_age            = above_value_i(input("Input rabbit age, for making mini rabbits: "),0)

def ad_f(sim): # Use case 14
    """[Gives access to configure all parameters for foxes in advanced settings]
    
    Args:
        sim ([class]): [A class from the module parameters called Simulation used here to set and forward in the function used]
    """
    
    sim.foxes.initial_size                    = pop_size(input("Foxes populations: "),sim)
    sim.foxes.metabolism                      = above_value_i(input("Input foxes metabolism: "),0)
    sim.foxes.max_age                         = above_value_i(input("Input foxes max age: "),0)           
    sim.foxes.max_energy                      = above_value_i(input("Input foxes max energy levels: "),0)
    sim.foxes.reproduction_probability        = validate_percentage_input(input("Input foxes younglings probability "))
    sim.foxes.reproduction_min_energy         = above_value_i(input("Input foxes minimum energy for reproduction: "),0)
    sim.foxes.reproduction_min_age            = above_value_i(input("Input foxes age, for making mini rabbits: "),0)
    


## Reporting menu for user interaction
def reporting_menu(results): # Use case 16
    """[Gives the user the options to select which kind of plot analyse they want]
    
    Args:
        results ([class]): [This will have the results from the simulation, for further analyzing]
    """    
    
    while True:
        print("Select plot to analyze\n1 Summary\n2 Population size\n3 Lifespan foxes and rabbits\n4 Energy consumption\n5 Kill plot \n6 Quit")
        
        user_input = (input("Select: "))
        if user_input == "1":
            
            reporting.print_summary(results)
        elif user_input == "2":
            
            reporting.plot_pop_size(results)
            
        elif user_input == "3":
            
            reporting.plot_lifespan(results)
        elif user_input == "4":
            
            reporting.plot_energy(results)
        elif user_input == "5":
            
            reporting.plot_kills(results)
        elif user_input == "6":
            done()
            sys.exit()
        else:
            print("\nPlease input a value between 1 and 6\n")

def done():
    
    print(r"""                                         /\
            \\\\                         ||
             \\\\\                       ||
              \\\\                       ||  
               \\\\           \\\\\      ||       
                 \\\         \\\\\\\\\   || 
          __    __\\\__    \\\\\\\|\ \\\\|| 
         /  |  /       \  \\\\\\\\|\\ ___||_    
        / | | /         \  \\\\\\\\_ \     o \____ 
     __/ /| |/      \    \\\\\\\\\/               \
    |__L/ |________  \    \\\\\\\/     \____/-----/
           __/ /\     \    \\\\\/        /
          |__L/  \ \   \    \\\/      / /     
                  \ \   \_   \/      / / 
                   \ \       /      / / 
                    \ \/           / /    
                     \ |          / /  
                      \|           /
                       |    |     /
                       \    |____/|
                        \   |  \  |
                         \  |   \ \
                          \ \    \ \
                           \ \    \ \
                            \ \    \ \
                             \ \    \_\
                              \_\    | \
                               | \   \\|
                               \\|    \|
                                \|
                                
                                """)

main_menu()
