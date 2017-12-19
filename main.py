#In order to simulate the spread of wild fire, lets first set some parameters for our experiment. To simulate the spread of fire we consider a lattice or 'plot of land'  The lattice contains the following rules: #####

##### 1. Trees grow with probability p at empty sites.  2.  Trees on fire will burn down at the next time step.  3. a site on fire will spread to its neighbors at the next time step. By adjusting the propability p, we can see how the spread of fires is altered.  Ultimately we will look at the distribution of fire at some distance r away from an arbitrary starting point and be able to get an idea of how likely that position is 'on fire'.  This is uselful info for instnace if you are make evacuations near a wildfire#####

##### To implement these rules, I created a 2d numpy array that contains random integers either 0,1,2.  0 = empty site, 1 = tree not on fire, 2 = tree on fire: #####

#function that takes an array and wraps it with zeros (empty trees)
def padwithzeros(vector, pad_width, iaxis, kwargs):
     vector[:pad_width[0]] = 0
     vector[-pad_width[1]:] = 0
     return vector

 #funtion creates my lattice that contains random selection of 0,1,2.  This is a 300x300 numpy array
import numpy as np
def create_arr():
    rand_arr = np.random.randint(3, size=(300,300))
    padded_arr = np.lib.pad(rand_arr, 1, padwithzeros)
    return padded_arr

#create the array (lattice)
padded_arr = create_arr()

#burn simulation function
#the burn function takes in an array returns an array after it has changed.
def burn(arr):
    #print(arr)
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            #2 above 1
            if arr[i,j] == 1:
                if (arr[i-1][j] == 2):
                    arr[i][j] = 2
                    #print('2 above 1')
                    #print(arr)
                #2 below 1
                if (arr[i+1][j] == 2):
                    arr[i][j] = 2
                    #print('2 below 1')
                    #print(arr)
                #2 to the right of 1
                if (arr[i][j+1] == 2):
                    #print('2 to right of 1')
                    arr[i][j] = 2
                    #print(arr)
                #2 to the left of 1
                if (arr[i][j-1] == 2):
                    #print('2 to left of 1')
                    arr[i][j] = 2
                    #print(arr)
                #2 top diagonal left of 1
                if (arr[i-1][j-1] == 2):
                    arr[i][j] = 2
                    #print(arr)
                #2 top diagonal right of 1
                if (arr[i-1][j+1] == 2):
                    arr[i][j] = 2
                    #print(arr)
                #2 bottom diagonal left of 1
                if (arr[i+1][j-1] == 2):
                    arr[i][j] = 2
                    #print(arr)
                #2 bottom diagonal right of 1
                if (arr[i+1][j+1] == 2):
                    arr[i][j] = 2
                    #print(arr)
            elif arr[i][j] == 2:
                arr[i][j] = 0
                #print('2 becomes arrero')
                #print(arr)
    return arr

#p is probability of tree growing in empty site zero
#grow() is a function that for a given p updates empty sites for 1 time step
#the function works such that it assigns a random number to y between 0 and 100.  We construct the prob p using the notion that there is a 20% chance that y will be less than 20.  The same logic follows for all p
def grow(p, arr):
    #print('original:')
    #print(arr)
    for i in range(1, len(arr)-1):
        for j in range(1, len(arr[i])-1):
            if arr[i][j] == 0:
                y = np.random.randint(100)
                #print(y)
                if y<=p:
                    arr[i][j] = 1
                    #print('changed array')
                    #print(arr)
    return arr

#grow(30, padded_arr)

def update_arr(arr, p):
    future = burn(arr)
    future_1 = grow(p, future)
    return future_1


def count_2(arr):
    count = 0
    for i in range(0, len(arr)):
        for j in range(0, len(arr[i])):
            if arr[i][j] == 2:
                    count+=1
    return count

def run_sim()
    s = 0
    final_arr = []
    number_of_2 = []
    while s<100:
        final_arr.append(update_arr(padded_arr, 5).copy())
        number_of_2.append(count_2(final_arr[s]))
        s+=1

    final_arr = np.array(final_arr)
    return final_arr

# create evenly spaced integers between 0,100 to represent time (x axis)
import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0,100,100,endpoint=False)
