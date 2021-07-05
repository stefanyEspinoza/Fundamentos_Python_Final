import os

FILE_NAME = 'primary_results.csv'

with open( FILE_NAME, mode='r') as f:
    # data = f.readlines()
    for line in f.readlines():
      print(line)

# print(data)

