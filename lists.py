import csv

with open('list.csv', newline='') as csvfile:
    mylist = list(csv.reader(csvfile))

print(mylist)
