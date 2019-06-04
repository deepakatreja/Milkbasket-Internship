import csv 

# 'with' keyword takes care of common tasks associated with opening a file like closing it
# The with statement simplifies exception handling by encapsulating common
#preparation and cleanup tasks.

with open('MOCK_DATA.csv', newline='') as csvfile:
    lineReader = csv.reader('csvfile', delimiter=' ', quotechar='|')
    for row in lineReader:
        print(', ' .join(row))
