
import simulation
import reporting
from parameters import Execution, Simulation, World, Population
import sys

#### MIA #### 1: control feature for total population against simulation size. 2: updating of parameters(fra QS og AD rabbits & foxes).
#### MIA #### 3: Test it all

def main_menu(sim = Simulation()):
    while True:
        """Function that containt main menu settings.

        Args:
            sim ([int], optional): [Updates simulation values if quick set has been used. Same occurs if advanced settings have been used]. Defaults to Simulation values().
        """    
        user_input = input("Options: Press a number, then enter to select\n1 Display parameter settings\n2 quick setup\n3 for advanced settings\n4 run\n5 for quit\n\n")
        
        try:
            user_input = int(user_input)                    
        except ValueError:
            print(user_input, "is not and integer")
            

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

def is_int(x):
    try:
        int(x)
        # print("Is int or bolean")
        return True
    except Exception:
        # print("The inputtede varible is not a integer: " + str(x))
        return False



def in_Between(x,above=0,below=10**3):
        
    # print("\nAbove")
    is_int(above)
    
    # print("\nbelow")
    is_int(below)
    
    
    # print("\nand")
    if int(above) < int(x) and int(below) > int(x):
        # print("Aproved")  ## slettes eller laves om når vi har styr på det hele 
        return True
    else:
        # print("not between: " + str(above) + " and " + str(below))
        return False    

    
    
def Quick_setup():
    

    Quick=[0,0,0,""] #    Quick=[Size_world,Size_pop,D_limit,Sim_mode]
    Text=["Size of the world: ","Size of the populations: ","Duration limit: ","Simulation mode: "]
    for n in range(len(Quick)):
        
        if is_int(Quick[n]):
            while True:
                Quick[n]=input(Text[n])
                if (is_int(Quick[n])) and (in_Between(Quick[n])):
                    break
                else:
                    print("nope not correct")
        else:
            while True:
                Quick[n]=input(Text[n])
                if not is_int(Quick[n]):
                    break
                else:
                    print("nope not correct")
    return Quick
       
 



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
    try:
        user_input = bool(input("Island shape: 1 for Toroid, 0 for Square "))         
    except ValueError:
        print("Please enter 1 or 0 for true or false ")
        world_setup(sim)                                                                #### BBloooow up
    try:
        user_input = validate_bool_input(user_input)
    except ValueError:
        print(user_input, "Please enter 1 or 0 for true or false ")
        world_setup(sim)
    try:
        ns_length = int(input("Insert horizontal length from north to south "))
    except ValueError:
        print("please enter int")
        world_setup(sim)
    try:
        we_length = int(input("Insert vertifcal length from west to east "))
    except ValueError:
        print("Please insert an integer ")
        world_setup(sim)
    
    #sim = Simulation()
    sim.world.north_south_length = ns_length
    sim.world.west_east_length = we_length
    sim.world.is_toroid = user_input
################################ via adgang fra advanced_menu_setting lukker den bare, skal løses
    # return user_input , ns_length, we_length,


def qs(sim):
    """[Function that greates a quick setup for the simulation of foxes and rabbits.\nUser will only have acces to set rabbit, fox population, duration of the simulation and simulation mode]
    """    
    try:
        init_s_r = int(input("Input the initial rabbit population size "))
    except ValueError:
        print('Please enter an integer')
        qs(sim)
    
    Quick=[0,0,0,0]
    Text=["Rabbit populations: ","Fox populations: ","Duration limit: ","Simulation mode: "]

    for n in range(len(Quick)):
        
        while True:
            Quick[n]=input(Text[n])
            if (is_int(Quick[n])) and (in_Between(Quick[n])):
                break
            else:
                print("nope not correct")

    try:
        init_s_f = int(input("Input the initial fox population size "))
    except ValueError:
        print('Please enter an integer')
        qs(sim)
    try:
        world_setup(sim)
    except ValueError:
        print("Please make sure to enter 1 for toroid or 0 for island") ##
        qs(sim)
    try:
        exe(sim)
    except ValueError:
        print("Please make sure to")
        qs(sim)

    #sim = Simulation()
    sim.world.area
    sim.rabbits.initial_size = Quick[0]
    sim.foxes.initial_size = Quick[1]
    #sim.world.north_south_length = ns_len
    #sim.world.west_east_length = we_len

    # Call main menu with the instance of sim
    print("Quick setup complete, returning to main menu")
    return # m_s, viz, s_d, sim


def exe(sim):
    try:
        user_input = int(input("Batch: Vizualization(s) 1, 0 for none "))         
    except ValueError:
        print("Please enter 1 or 0 for true or false ")
        exe(sim)
        
    try:
        viz = validate_bool_input(user_input)                   ########## blows
    except ValueError:
        print(user_input, "Please enter 1 or 0 for true or false ")
        exe(sim)
    try:
        m_s = int(input("Input maximum step for current simulation session "))
    except ValueError:
        print("Pleas use integers as input ")
        exe(sim)
    try:
        s_d = float(input("Add a delay in seconds "))
    except ValueError:
        print("Please insert float ")
        exe(sim)
    try:
        user_input = validate_bool_input(user_input) ## Something blows up
    except ValueError:
        print(user_input, "Please enter 1 or 0 for true or false ")
    
    
    sim.execution.max_steps = m_s
    sim.execution.batch = viz
    sim.execution.step_delay = s_d


def advanced_menu_settings(sim):
    """A Function that contains advanced menu settings

    Returns:
        [int]: [User navigates menu with intergers and commit their choices with "Enter"]
    """
    while True:
        user_input = input("Options:\n1 World settings\n2 rabbit pupolation settings\n3 fox poplation settings\n4 execution settings\n5 return to main menu\n\n")
        try:
            user_input = int(user_input)
        except ValueError:
            print(user_input, "is not and integer")
        if int(user_input) == 1:
            world_setup(sim)
            ##Husk at send instansen rundt i funktionerne, lav ikke en ny. 
        elif int(user_input) == 2:
            ad_r(sim)
        elif int(user_input) == 3:
            ad_f(sim)
        elif (user_input) == 4:
            exe(sim)
        elif int(user_input) == 5:
            break
            




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
    ### Lav for to i en.
    try:
        init_s_r = int(input("Input rabbit population size "))
    except ValueError:
        print("Please enter an interger")
        ad_r(sim)
    try:
        meta_r = int(input("Input rabbit metabolism "))
    except ValueError:
        print("Please enter an interger")
        ad_r(sim)
    try:    
        max_age_r = int(input("Input rabbit max age "))
    except ValueError:
        print( "Please enter an interger")
        ad_r(sim)
    try:
        ene_r = int(input("Input rabbit max energy levels "))
    except ValueError:
        print( "Please enter an interger")
        ad_r(sim)
    try:
        repro_prop_r = float(input("Input rabbit younglings probability "))
    except ValueError:
        print( "Please enter an interger")
        ad_r(sim)
    try:
        repro_m_e_r = int(input("Input rabbit minimum energy for reproduction "))
    except ValueError:
        print( "Please enter a float")
        ad_r(sim)
    try:
        repro_fer_r = int(input("Input rabbit age, for making mini rabbits "))
    except ValueError:
        print("is not an integer")
        ad_r(sim)

       
    #sim = Simulation() ## Der skal kun laves én instans a sim #############################################################
    sim.rabbits.initial_size = init_s_r
    sim.rabbits.metabolism = meta_r
    sim.rabbits.max_age = max_age_r                     
    sim.rabbits.max_energy = ene_r
    sim.rabbits.reproduction_probability = repro_prop_r
    sim.rabbits.reproduction_min_energy = repro_m_e_r
    sim.rabbits.reproduction_min_age = repro_fer_r
        

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
    try:
        init_s_f = int(input("Input the initial fox population size "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
    try:
        meta_f = int(input("Input fox metabolism "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
    try:
        max_age_f = int(input("Input fox max age "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
    try:
        ene_f = int(input("Input fox max energy levels "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
    try:
        repro_prop_f = float(input("Input fox younglings probability "))
    except ValueError:
        print("is not a float")
        ad_f(sim)
    try:
        repro_m_e_f = int(input("Input fox minimum energy for reproduction "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
    try:
        repro_fer_f = int(input("Input fox age, for making mini foxes "))
    except ValueError:
        print("is not an integer")
        ad_f(sim)
##################################################################################
    #sim = Simulation()
    sim.foxes.initial_size = init_s_f
    sim.foxes.metabolism = meta_f
    sim.foxes.max_age = max_age_f4

    sim.foxes.max_energy = ene_f
    sim.foxes.reproduction_probability = repro_prop_f
    sim.foxes.reproduction_min_energy = repro_m_e_f
    sim.foxes.reproduction_min_age = repro_fer_f
    
       

## Reporting menu for user interaction
def reporting_menu(results):
    '''
    Gives the user the options to select which menu they want to analyse
    '''
    while True:
        print("Select plot to analyze\n1 Summary\n2 Population size\n3 Lifespan foxes and rabbits\n4 Energy consumption\n Kills")
        
        user_input = (input("Select: "))
        if int(user_input) == 1:
            summary()
        elif int(user_input) == 2:
            plot_population_size()
        elif int(user_input) == 3:
            plot_life_span()
        elif int(user_input) == 4:
            plot_energy()
        elif int(user_input) == 5:
            plot_kills()
        elif int(user_input) == 5:
            break


def summary():
    '''
    Prints a summary of the simulation results and basic statistics.

    '''
    print("dummy --> ")

def plot_population_size():
    '''
    Plots lifespans across population idividuals
    '''
    print("dummy --> ")

def plot_life_span():
    '''
    Plots population sizes against time
    '''
    print("Dummy --> ")

def plot_energy():
    '''
    Plots the total energry over the life of eah individual.
    '''
    print("Dummy -->")

def plot_kills():
    '''
    Plots all kills
    '''
    print("Dummy -->")

main_menu()
