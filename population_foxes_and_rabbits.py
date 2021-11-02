from fuck_your_encoding import Execution, Simulation, World, Population
import simulation
import reporting
import parameters as para
import sys

simulation_default = para.Simulation()
print(simulation_default.__str__())


def main_menu():

    user_input = input("Options:\n1 default parameter settings\n2 quick setup\n3 for advanced settings\n4 run\n5 for quit\n\n")

    ##Default parameters    
    if int(user_input) == 1:
        parameters()

    elif int(user_input) == 2:
        quick_setup()

    elif int(user_input) == 3:
        advanced_menu_settings()

    elif int(user_input) == 4:
        run_simulation()
        
    else:
        int(user_input) == 5
        sys.exit()


def parameters(): ## den skal kontrolleres, tror ikke det lever
    if parameters == quick_setup:
        rabbit_pop
        fox_pop
        world_set
    elif parameters == advanced_menu_settings:
        ad_bunny_population
        ad_fox_population
        print(ad_fox_population)
        print
    else:
        print("Default settings for simulation")
        simulation_default = para.Simulation()
        print(simulation_default.__str__())
    main_menu()


##  Quick setup
def quick_setup():
    ## Select world shape and set values for it
                        ###### SAAAAAAAAAAANDRAAAAAA fiks for advanced 
    
    input_north_south_length = int(input("Insert horizontal length from north to south "))
    input_west_east_length = int(input("Insert vertifcal length from west to east "))

    input_world_shape = input("Select 1(toroid) or 2(island), press enter ") ## No clue how to fix
    world_set = World(input_north_south_length, input_west_east_length, input_world_shape)

    ## Default values for fox population
    fox_initial_size = int(input("Input the initial fox population size "))
    
    fox_population = Population('foxes', fox_initial_size, 3, 25, 45,0.5,5,10)
    
    ## Default values for rabbit population
    rabbit_initial_size = input("Input the initial rabbit population size ")
    rabbit_population = Population('rabbits', rabbit_initial_size, 3, 25, 45,0.5,5,10)
    print(world_set)
    print(fox_population)
    print(rabbit_population)

    main_menu()


        # check if rabbit population is bigger or smaller than surface area
        #def check_population_vs_area():
        #    if rabbit_initial_size and 

        # check if fox population is bigger or smaller than surface area
        ## Reporting

    ## Advanced menu settings
def advanced_menu_settings(): ## Er stuck i et loop
    '''

    '''
    user_input = input("Options:\n1 World settings\n2 rabbit pupolation settings\n3 fox poplation settings\n4 execution settings\n5 return to main menu\n\n")   

    if user_input == 1:
        world()
    elif user_input == 2:
        rabbit_pop()
    elif user_input == 3:
        fox_pop()
    elif user_input == 4:
        execution()
    else:
        user_input == 5
        print("somesome")

        
#def ad_exetution_settings():                                       ##### Denne skal også kontrolleres og 
#    user_input = int(input()
#    if user_input == "1" or True:
#        batch_confiq = Execution(batch = True)
#        print("Simulation is vizualized ")
##    else:
#        user_input == "2" or False
#        batch_confiq = Execution(Batch = False)
#        print("Simulation is NOT vizualized ")


    ## Rabbit population settings
def rabbit_pop():
    '''
    Gives user access to confiqure different parameters for the rabbit population
    '''
    user_input = input("Select which setting to set for rabbit population ")
    print("1 settings for initial size ")
    print("2 settings for metabolism ")
    print("3 settings for maximum age ")
    print("4 settings for maximum age ")
    print("5 settings for reproduction probability ")
    print("6 settings for reproduction cost ")
    print("7 settings for bunny fertility ")
    
    if user_input == 1:
        ad_bunny_initial_size = int(input("Input the initial rabbit population size "))
    elif user_input == 2:
        ad_bunny_metabolism = int(input("Input rabbit metabolism as an integer "))
    elif user_input == 3:
        ad_bunny_max_age = int(input("Input rabbit maximum age as an integer "))
    elif user_input == 4:
        ad_bunny_maximum_energy = int(input("Input maximum energy for rabbits "))
    elif user_input == 5:
        ad_bunny_reproduction_rate = float(input("Input reproduction rate for rabbits "))
    elif user_input == 6:
        ad_bunny_reproduction_cost = int(input("Input reproduction cost for rabbits "))
    elif user_input == 7:
        ad_bunny_reproduction_age = int(input("Input rabbit fertility age "))
    else:
        print("someshit")
    ad_bunny_population = Population('rabbits', ad_bunny_initial_size, ad_bunny_metabolism, ad_bunny_max_age, ad_bunny_maximum_energy, ad_bunny_reproduction_rate, ad_bunny_reproduction_cost, ad_bunny_reproduction_age)
    print(ad_bunny_population)
    return ad_bunny_population
    

    ## Fox population settings
def fox_pop(): ## Kan ikke komme igennem, er stuck i et loop mellem main_menu og advanced_menu_settings
    '''
    Gives user the options confiqure parameters for fox population
    '''
    user_input = input("Select which setting to set for fox population ")
    print("1 settings for initial size ")
    print("2 settings for metabolism ")
    print("3 settings for maximum age ")
    print("4 settings for maximum age ")
    print("5 settings for reproduction probability ")
    print("6 settings for reproduction cost ")
    print("7 settings for fox fertility ")

    if user_input == 1:
        ad_fox_initial_size = int(input("Input the initial fox population size ")) 
    elif user_input == 2:
        ad_fox_metabolism = int(input("Input fox metabolism as an integer "))
    elif user_input == 3:
        ad_fox_max_age = int(input("Input fox maximum age as an integer "))
    elif user_input == 4:
        ad_fox_maximum_energy = int(input("Input maximum energy for foxes "))  
    elif user_input == 5:
        ad_fox_reproduction_rate = float(input("Input reproductionrate for foxes "))
    elif user_input == 6:
        ad_fox_reproduction_cost = int(input("Input reproduction cost for foxes "))
    elif user_input == 7:
        ad_fox_reproduction_age = int(input("Input fox fertility age "))
    else:
        print("'Error\nMake a choice between 1 and 7, use whole numbers")

    ad_fox_population = Population('foxes', ad_fox_initial_size, ad_fox_metabolism, ad_fox_max_age, ad_fox_maximum_energy, ad_fox_reproduction_rate, ad_fox_reproduction_cost, ad_fox_reproduction_age)

    return ad_fox_population


    ## Reporting
def reporting_menu(): ## ikke testet
    '''
    Gives the user the options to select which menu they want to analyse
    '''
    print("Select plot to analyze\n1 Summary\n2 Population size\n3 Lifespan foxes and rabbits\n4 Energy consumption\n Kills")
    user_input = input("Select which setting to set for fox population ")
    if user_input == 1 or "summary" == True:
        summary()
    elif user_input == 2:
        plot_population_size()
    elif user_input == 3:
        plot_life_span()
    elif user_input == 4:
        plot_energy()
    elif user_input == 5:
        plot_kills()
    else:
        user_input == 5
        
    

def summary(results):
    '''
    Prints a summary of the simulation results and basic statistics.

    '''
    print(results)

def plot_population_size(results):
    '''
    Plots lifespans across population idividuals
    '''
    print("dummy --> ")

def plot_life_span(results):
    '''
    Plots population sizes against time
    '''
    print("Dummy --> ")

def plot_energy(results):
    '''
    Plots the total energry over the life of eah individual.
    '''
    print("Dummy -->")

def plot_kills(results):
    '''
    Plots all kills
    '''
    print("Dummy -->")
    
def run_simulation(): ## Lever ikke endnu
    simulation_execution = Execution()
    Simulation
    results = simulation_execution
    return results


main_menu()
