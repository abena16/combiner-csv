#import needed libraries/modules
import pandas as pd
import sys
import os

#creates list that will contain our command line arguments
file_list = []

#loop through the arguments
for datafile in sys.argv[1:]:

    #adds the arguments to my empty list + used 'os' to get the base name in specified path. 
    file_list.append(pd.read_csv(datafile).assign(filename = os.path.basename(datafile)))

    
    #concat function to combine the files
    combine_data = pd.concat(file_list)

    #save our new combined csv data into a new file 
    combine_data.to_csv("combined.csv")




