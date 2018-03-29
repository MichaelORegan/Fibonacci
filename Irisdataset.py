# Michael O'Regan 29.03.2018

# Opening the csv file containing the Iris Data Set 

with open("data/irisdataset.csv") as f:  # the with function opens and closes a file without the need to specify close the file
    for line in f:                       # the file is set to the arbitrary  value f above, for each line in f
        print(line.split(',')[0])        # print column 0th (first column)
