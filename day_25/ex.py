# CSV comma seperated values

import csv

"""
with open('D://100_days_of_code//day_25//weather_data.csv') as data_file:
    datas =csv.reader(data_file)
    # print(datas)
    temperatures = []
    for row in datas:
        # print(row)
        temperatures.append(int(row[1]))
"""

import pandas

data = pandas.read_csv('D://100_days_of_code//day_25//weather_data.csv')
# print(data)

data_dict = data.to_dict()
# print(data_dict)

temperatures = data['temp'].to_list()
# print(temperatures)

"""
Avarage temperature
"""
#print(data['temp'].mean())
#print(data['temp'].max())



# print(data[data.day == "Tuesday"])
"""
       day  temp condition
1  Tuesday    14      Rain
"""

# print(data[data.day == data.temp.max()])


monday = data[data.temp == "Monday"]
print(monday)

