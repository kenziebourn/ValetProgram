import csv

# data to be written row-wise in csv file
data = [['Geeks'], [4], ['geeks !']]

# opening the csv file in 'w+' mode
file = open('g4g.csv', 'w+', newline='')

# writing the data into the file
with file:
    write = csv.writer(file)
    write.writerows(data)