import matplotlib.pyplot as plt
import results
import numpy as np
from statistics import mean
from math import floor


def print_summary(res: results.SimulationStats): # UC 35:
    '''
    A function to simply print the importan information in plain text

    '''

    print("\n")
    print("Number of individuals that died by old age.")
    print("Foxes")
    print(res.foxes.dead_by_old_age) 
    print("Rabbits")    
    print(res.rabbits.dead_by_old_age)       #
    print("Foxes and Rabbits")    
    print(res.rabbits.dead_by_old_age+res.foxes.dead_by_old_age) 

    print("\n")
    print("Number of rabbits that died by predation.")
    print(res.rabbits.dead_by_predation)#
    
    print("\n")
    print("Number of individuals that died by starvation.")
    print("Foxes")
    print(res.foxes.dead_by_starvation)       #
    print("Rabbits")
    print(res.rabbits.dead_by_starvation)       #
    print("Foxes and Rabbits")
    print(res.rabbits.dead_by_starvation+res.foxes.dead_by_starvation)  

    print("\n")
    print("Individuals alive and ever lived")
    print("Foxes")
    print(res.foxes.total)       #
    print("Rabbits")
    print(res.rabbits.total)       #
    print("Foxes and Rabbits")
    print(res.rabbits.total+res.foxes.total) 

    print("\n")
    print("Number of dead animals")
    dead_rab= res.rabbits.dead_by_old_age+res.rabbits.dead_by_starvation+res.rabbits.dead_by_predation
    dead_fox=res.foxes.dead_by_old_age+res.foxes.dead_by_starvation
    All_dead=dead_rab+dead_fox
    print("Foxes")
    print(dead_fox)
    print("Rabbits")
    print(dead_rab)
    print("In total")
    print(All_dead)
    
    print("\n")
    print("The lowest number of animals alive")
    print("Foxes")
    print(min(res.foxes.size_per_step))
    print("Rabbits")
    print(min(res.rabbits.size_per_step))
    print("overall")
    print(min(res.foxes.size_per_step+res.rabbits.size_per_step))

    print("\n")
    print("The largeste number of animals alive")
    print("Foxes")
    print(max(res.foxes.size_per_step))
    print("Rabbits")
    print(max(res.rabbits.size_per_step))
    print("overall")
    print(max(res.foxes.size_per_step+res.rabbits.size_per_step))

    print("\n")
    print("The avage number of animals alive \nOnly steps with a minimum of 1 animal alive has been used to calculate this")
    print("Foxes")

    # Finding out when the porpulation die out
    try:
        zero_index_fox=res.foxes.size_per_step.index(0)
    except:
        zero_index_fox=-1

    try:
        zero_index_rab=res.rabbits.size_per_step.index(0)
    except:
        zero_index_rab=-1

    print(floor(mean(res.foxes.size_per_step[0:zero_index_fox])))
    print("Rabbits")
    print(floor(mean(res.rabbits.size_per_step[0:zero_index_rab])))
    print("overall")
    print(floor(mean(res.foxes.size_per_step[0:zero_index_fox]+res.rabbits.size_per_step[0:zero_index_rab])))

    print("\n")
    print("\n")

def plot_pop_size(res: results.SimulationStats): # UC 36
    '''
    A function witch plots the size of the porpulation on each step, in a line plot and histogram
    '''


    # Creating the figure and the plot
    fig1, (ax0) = plt.subplots(1, 1)
    # getting the x axes 
    steps=list(range(len(res.foxes.size_per_step)))
    # Getting the population size in total
    all_pop=[a + b for a, b in zip(res.foxes.size_per_step, res.rabbits.size_per_step)]
    
    # plotting in the specific plot
    ax0.plot(steps,res.foxes.size_per_step, label='Fox population')
    ax0.plot(steps,res.rabbits.size_per_step, label='Rabbit population')
    ax0.plot(steps,all_pop, label='Fox and rabbit population')
    plt.grid(True)
    
    ax0.legend(loc='upper right')
    ax0.set_ylabel('Populations')  # Can use $[^oC]$' note the use of TeX math formatting
        
    # def plot_pop_size_bar(res: results.SimulationStats):
    # making the labels
    labels  =  [str(i) for i in list(range(len(res.foxes.size_per_step)))] 
    Foxes   = res.foxes.size_per_step
    Rabbits = res.rabbits.size_per_step
    width   = 1       # the width of the bars: This is done so the hare just beside eachoter
    
    # Making another figure and plot
    fig2, ax = plt.subplots(1,1)
    
    ax.bar(labels,Foxes, width, label='Foxes')
    # making the histogram so that they are on top of eachother 
    ax.bar(labels,Rabbits, width, bottom=Foxes,
           label='Rabbits')
    ax.locator_params(tight=True, nbins=4)
    ax.set_ylabel('Population')
    ax.set_title('Population by animale race')
    ax.legend()
    
    # Setting max number of labels on the x axes 
    ax.xaxis.set_major_locator(plt.MaxNLocator(11))

    # The plotting is done
    plt.draw()
    # introducing a pause
    plt.pause(0.001)


def plot_kills(res: results.SimulationStats): # UC 37

    fig, ax = plt.subplots()

    image = res.kills_per_patch
    # Getting the maximum value
    top = max([max(i) for i in image]) 
    
    ax.imshow(image, cmap=plt.cm.Reds)
    psm = ax.pcolormesh(image, cmap=plt.cm.Reds, rasterized=True, vmin=0, vmax=top)
    fig.colorbar(psm, ax=ax)
    
    
    ax.set_title('Kill grid')
    
    # Move left and bottom spines outward by 10 points
    ax.spines.left.set_position(('outward', 10))
    ax.spines.bottom.set_position(('outward', 10))
    # Hide the right and top spines
    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    # Only show ticks on the left and bottom spines
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')


    # Plot the plot
    plt.draw()
    # Setting a pause
    plt.pause(0.001)    

def plot_energy(res: results.SimulationStats): # UC 38
    '''
    A function plotting the avage energy levels on each step in a line plot and histogram. 
    '''

    fig1, (ax0)  = plt.subplots(1, 1)
    # getting the x axes 
    steps       = list(range(len(res.foxes.avg_energy_per_step)))
    Foxes       = res.foxes.avg_energy_per_step
    Rabbits     = res.rabbits.avg_energy_per_step
    Both        = res.avg_energy_per_step
    
    ax0.plot(steps,Foxes, label='Fox: Average energy')
    ax0.plot(steps,Rabbits, label='Rabbit: Average energy')
    ax0.plot(steps,Both, label='Fox and rabbit: average energy')
    plt.grid(True)
    
    ax0.legend(loc='upper right')
    ax0.set_ylabel('average energy')  
    fig1.tight_layout()
    
    x = np.arange(len(steps))  # the label locations
    width = 1  # the width of the bars
    
    fig2, (ax0,ax1,ax2) = plt.subplots(1,3)
    ax0.bar(x, Foxes, width, label='Foxes')
    ax1.bar(x, Rabbits, width, label='Rabbits')
    ax2.bar(x, Both, width, label='Both')
    
    for i, a in zip([ax0,ax1,ax2],["Foxes","Rabbits", "Both"]):
    # Add some text for labels, title and custom x-axis tick labels, etc.
        i.set_ylabel('avage energy')
        i.set_title(a)
        i.set_ylim([0, 140])
        
        # setting the max number of x labels
        i.xaxis.set_major_locator(plt.MaxNLocator(3))
       
    # Giving the figure a tight layout
    fig2.tight_layout()
    
    plt.draw()
    plt.pause(0.001)
               
def plot_lifespan(res: results.SimulationStats): # UC 39
    '''
    A function ploting the age of death of each animal. This is done with the dead by old age indclued and excluded
    '''

    Foxes       = res.foxes.age_at_death
    Rabbits     = res.rabbits.age_at_death
    Both        = Foxes + Rabbits
    
    print("the animals that died of old age has been revomed for better visualizasion")
    
    fig1, (ax0,ax1,ax2)  = plt.subplots(1, 3)

    fig2, (ax00,ax01,ax02)  = plt.subplots(1, 3)
    
    # This is done to remove the lage population of dead by old age as it will be difficult to see anything if this is included.
    if max(Rabbits)<max(Foxes):
        Both2 = [i for i in Both if i != max(Rabbits)]
    else:
        Both2 = [i for i in Both if i != max(Foxes)]
        
    for i,ax, a_title in zip([Foxes, Rabbits, Both2],[ax0,ax1,ax2],["Foxes", "Rabbits","Both"]):
        limitter= [0,max(i)-1]
        n, bins, patches = ax.hist(i, max(i), facecolor='g',range = limitter)
    
        ax.set_xlabel("age") 
        ax.set_ylabel('Number of Dead') 
        ax.set_title("lifespan of {}".format(a_title))
        ax.grid(True)
    


    # For the plot with dead by old age. 
    for i,ax, a_title in zip([Foxes, Rabbits, Both],[ax00,ax01,ax02],["Foxes", "Rabbits","Both"]):
        limitter= [0,max(i)]
        n, bins, patches = ax.hist(i, max(i), facecolor='g',range = limitter)
    
        ax.set_xlabel("age") 
        ax.set_ylabel('Number of Dead') 
        ax.set_title("lifespan of {}".format(a_title))
        ax.grid(True)

    
    fig1.suptitle('Without dead by old age', fontsize=16)
    fig1.tight_layout()

    fig2.suptitle('With dead by old alge', fontsize=16)
    fig2.tight_layout()
    plt.draw()
    plt.pause(0.001)
    

# Inforamtion from matplotlib.org
