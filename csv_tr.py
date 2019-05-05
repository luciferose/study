from datetime import datetime
from pprint import pprint

def conver2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights={}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
pprint(flights)
print('*'*50)

flights2={}
for k, v in flights.items():
    flights2[conver2ampm(k)] = v.title()
pprint(flights2)

