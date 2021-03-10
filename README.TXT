1. How to setup and run my program

Put 107061117.csv and hw01.py in same folder
in terminal run $ python3 hw01.py

Code Description:
Code:
filename = '107061117.csv'
data = []
header = []
with open(filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   for row in mycsv:
      data.append(row)

Description:
Input data.


Code:
for row in data:
    if row['HUMD'] == '-99.000' or row['HUMD'] == '999.000':
        row['HUMD'] = None

Description:
Remove '-99.000' & '999.000' in 'HUMD' column.

Code:
outlist = [['C0A880', 0], ['C0F9A0', 0], ['C0G640', 0], ['C0R190', 0], ['C0X260', 0]] 
computable = [False, False, False, False, False]

Description:
Declare output list(outlist), in each row: ['station_id', sum of HUMD].
Declare if sum of the HUMD value from each station can be computed.

Code:
for row in data:
    if row['station_id'] == 'C0A880' and row['HUMD'] != None:
        outlist[0][1] = outlist[0][1] + float(row['HUMD'])
        if computable[0] == False: computable[0] = True
    ......

Description:
Compute sum, and if the station's sum can be computed set its value of computable to True.

Code:
for i in range(5):
    if computable[i] == False: outlist[i][1] = 'None'
print(outlist)

Description:
If the sum cann't  be finded, set sum to 'None', and output outlist.

2. Results
[['C0A880', 14.740000000000002], ['C0F9A0', 23.57], ['C0G640', 21.8], ['C0R190', 21.999999999999993], ['C0X260', 21.65]]