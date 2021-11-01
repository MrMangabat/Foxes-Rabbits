from fuck_your_encoding import Simulation, World, Population
import simulation
import reporting
import parameters as para
import sys

def main_menu():
    user_input = input("Options: Select 1 default parameter settings, 2 quick setup, 3 for advanced, 4 run, 5 for quit ")

    ##Default parameters    
    if int(user_input) == 1:
        parameters()

    elif int(user_input) == 2:
        quick_setup()

    elif int(user_input) == 3:
        ad_setup()   
    elif int(user_input) == 4:
        run()
    else:
        int(user_input) == 5
        sys.exit()

def parameters():
    print("Default settings for simulation")
    simulation_default = para.Simulation()
    print(simulation_default.__str__())


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

        # check if rabbit population is bigger or smaller than surface area
        #def check_population_vs_area():
        #    if rabbit_initial_size and 

        # check if fox population is bigger or smaller than surface area
        ## Reporting

##  Advanced setup
def ad_setup():
        print("Set advanced options ")
        # Values for fox population
        ad_fox_initial_size = int(input("Input the initial fox population size ")) ## Noget med initial size og population skal ændres
        ad_fox_metabolism = int(input("Input fox metabolism as an integer "))
        ad_fox_max_age = int(input("Input fox maximum age as an integer "))
        ad_fox_maximum_energy = int(input("Input maximum energy for foxes "))
        ad_fox_reproduction_rate = float(input("Input reproductionrate for foxes "))
        ad_fox_reproduction_cost = int(input("Input reproduction cost for foxes "))
        ad_fox_reproduction_age = int(input("Input fox fertility age "))

        ad_fox_population = Population('foxes', ad_fox_initial_size, ad_fox_metabolism, ad_fox_max_age, ad_fox_maximum_energy, ad_fox_reproduction_rate, ad_fox_reproduction_cost, ad_fox_reproduction_age)

        #Values for bunny population
        ad_bunny_initial_size = int(input("Input the initial rabbit population size "))
        ad_bunny_metabolism = int(input("Input rabbit metabolism as an integer "))
        ad_bunny_max_age = int(input("Input rabbit maximum age as an integer "))
        ad_bunny_maximum_energy = int(input("Input maximum energy for rabbits "))
        ad_bunny_reproduction_rate = float(input("Input reproduction rate for rabbits "))  
        ad_bunny_reproduction_cost = int(input("Input reproduction cost for rabbits "))
        ad_bunny_reproduction_age = int(input("Input rabbit fertility age "))

        ad_bunny_population = Population('rabbits', ad_bunny_initial_size, ad_bunny_metabolism, ad_bunny_max_age, ad_bunny_maximum_energy, ad_bunny_reproduction_rate, ad_bunny_reproduction_cost, ad_bunny_reproduction_age)
        print(ad_bunny_population)
    
    ## Reporting


    
def run():
    para.simulation.run()   



def exit():
    SystemExit()
    exit(user_input)


main_menu()






