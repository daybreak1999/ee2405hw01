import csv

#filename = '107061117.csv'
filename = '107061117.csv'
data = []
header = []
with open(filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   for row in mycsv:
      data.append(row)

for row in data:
    if row['HUMD'] == '-99.000' or row['HUMD'] == '999.000':
        row['HUMD'] = None

# output station_id and summation
outlist = [['C0A880', 0], ['C0F9A0', 0], ['C0G640', 0], ['C0R190', 0], ['C0X260', 0]] 

# if sum of the HUMD value from C0A880, C0F9A0, C0G640, C0R190, C0X260 can be caculated. 
computable = [False, False, False, False, False]

for row in data:
    if row['station_id'] == 'C0A880' and row['HUMD'] != None:
        outlist[0][1] = outlist[0][1] + float(row['HUMD'])
        if computable[0] == False: computable[0] = True
    elif row['station_id'] == 'C0F9A0' and row['HUMD'] != None:
        outlist[1][1] = outlist[1][1] + float(row['HUMD'])
        if computable[1] == False: computable[1] = True
    elif row['station_id'] == 'C0G640' and row['HUMD'] != None:
        outlist[2][1] = outlist[2][1] + float(row['HUMD'])
        if computable[2] == False: computable[2] = True
    elif row['station_id'] == 'C0R190' and row['HUMD'] != None:
        outlist[3][1] = outlist[3][1] + float(row['HUMD'])
        if computable[3] == False: computable[3] = True
    elif row['station_id'] == 'C0X260'and row['HUMD'] != None:
        outlist[4][1] = outlist[4][1] + float(row['HUMD'])
        if computable[4] == False: computable[4] = True

for i in range(5):
    if computable[i] == False: outlist[i][1] = 'None'
print(outlist)