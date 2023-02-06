#import needed libraries/modules
import pandas as pd
import sys

#creates list that will contain our command line arguments
file_list = []

def combiner():
#loop through the arguments
    for datafile in sys.argv[1:]:

        #adds the arguments to my empty list
        file_list.append(pd.read_csv(datafile))

        #concat function to combine the files
        combine_data = pd.concat(file_list)

        #save our new combined csv data into a new file 
        combine_data.to_csv("combined.csv")



if __name__ == "__main__":
    combiner()
    print("Combine successful!")
