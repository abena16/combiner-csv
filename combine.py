#import required libraries
#import modules
import pandas as pd
import sys

file_list = sys.argv[1:]

#reads through the files
df = [pd.read_csv(datafile) for datafile in file_list]

#concat function to combine the files
combine_data = pd.concat(df)

#save our new combined csv data into a new file 
combine_data.to_csv("combined.csv")

