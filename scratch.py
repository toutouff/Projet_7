import csv
from data import Client,Action

actionlist = []
b_client = Client()


with open('dataset1_Python+P7.csv') as dataset:
    data = csv.reader(dataset,delimiter=',',quotechar='|')
    data.next()
    for row in data:actionlist.append(Action(row))

actionlist.sort(reverse =True,key=Action.get_roi)

for action in actionlist:
    b_client.buy(action)


print(b_client.get_benef(),b_client.money)
for action in b_client.wallet:
    print(action.__str__())
