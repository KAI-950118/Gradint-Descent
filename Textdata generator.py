import csv
import random

w = 0.8
b = 10.2
data_number = 100
data = [[0]*2 for i in range(data_number)]


for i in range(0, data_number):
    noise = random.uniform(-0.5, 0.5)
    x = random.uniform(1, 10)
    y = x * w + b + noise
    # print(noise)
    data[i][0] = x
    data[i][1] = y

# print(data)
with open('TrainData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
