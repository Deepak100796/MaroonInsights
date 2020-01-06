import json
import pandas as pd
try:
     with open('assignment2.json', 'r') as jsonfile:
          data = jsonfile.read()
except FileNotFoundError:
     print("file not faund ! just check filename ")
jsonobj = json.loads(data)
# print(jsonobj)
df = pd.read_json('assignment2.json')
# print(df)
df.to_csv('account.csv')
print("account.csv created succesfully!")






# import json
# import csv
#
# # read file
# with open('assignment2.json', 'r') as jsonfile:
#     data = jsonfile.read()
#
# # parse file
# jsonobj = json.loads(data)
# # print(jsonobj)
#
#
# # print(jsonobj['priority'])
# keylist = []
# for key in jsonobj[0]:
#     keylist.append(key)
#
# f = csv.writer(open("test.csv", "w"))
# f.writerow(keylist)
#
# # Iterate through each record in the JSON Array
# for record in jsonobj:
# # Create placeholder to hold the data for the current record
#     currentrecord = []
# # Iterate through each key in the keylist and add the data to our current record list
#     for key in keylist:
#         currentrecord.append(record[key])
# # Write the current record as a line in our CSV
#     f.writerow(currentrecord)