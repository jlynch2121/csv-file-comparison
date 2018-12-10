# script for comparing Type metadata values in two CSVs and storing results
# Author: Joshua Lynch
# Created: 2018-12-06

import csv

# create and open a csv file to write results of comparison
writeFile = open('idhhDplaResponsibility.csv', 'w', newline='')
writer = csv.writer(writeFile)

# Open the list of local (IDHH) type metadata
idhhTypeData = csv.reader(open('idhhOriginalRecordFacets.csv'))

# Open list of values that DPLA can transform
dplaListFile = csv.reader(open('dplaTypeFilterList.csv'))

# create an array for storing DPLA values
dplaFilterList = []

# store values from CSV to array    
for row in dplaListFile:
    dplaFilterList.append(row[0])
    
# check to see if IDHH type metadata value is in the DPLA array
for row in idhhTypeData:
    field = row[0]
    # print and save values to CSV, labeling rows with values in a new column
    if field in dplaFilterList:
        print(field)
        writeThis = [[field, 'DPLA']]
        writer.writerows(writeThis)
    else:
        writeThis = [[field, '']]
        writer.writerows(writeThis)