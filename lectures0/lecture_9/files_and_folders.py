import os
import pandas as pd

# https://www.geeksforgeeks.org/os-module-python-examples/
# join path
print(os.path.join("Output", "file.txt"))

# path exist
print(os.path.exists("Data"))

# make directory
# os.mkdir("Output")

# Example
df = pd.read_csv(os.path.join("Data", "portfolio_data.csv"))
foldername = "Output"
filename = "BTC_df.csv"
if not os.path.exists(foldername):
    os.mkdir(foldername)
    
    # Pandas - save series/dataframe to csv
    df["BTC"].to_csv(os.path.join(foldername, filename), sep=";")


# other useful options
# rename a file
# os.rename("old_file.txt", "new_file.txt")

# remove a file
# os.remove("file.txt")

# remove empty directory
# os.rmdir("directory")

# file handling
# https://www.w3schools.com/python/python_file_open.asp
# https://www.w3schools.com/python/python_file_write.asp

# write to a file
# f = open("my_file.txt", "w")
# f.write("Hello world")
# f.close()

# open and read a file
# f = open("my_file.txt", "r")
# print(f.read()) 

# create empty file
# f = open("my_file.txt", "x")