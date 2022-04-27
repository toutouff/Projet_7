from model import Client, Action
from bbl_sort import bubble_sort
import csv


actionlist = []

client_roi = Client()
client_benef = Client()


with open("dataset1.csv") as dataset:
    data = csv.reader(dataset, delimiter=",", quotechar="|")
    next(data)
    for row in data:
        action = Action(row)
        if action.price <= 0 or action.roi <= 0:
            continue
        else:
            actionlist.append(action)

actionlist_roi = actionlist.copy()
actionlist_benef = actionlist.copy()
bubble_sort(actionlist_roi, lambda action: action.get_roi(), True)
bubble_sort(actionlist_benef, lambda action: action.get_benef(), True)

for i in range(len(actionlist)):
    client_roi.buy(actionlist_roi[i])
    client_benef.buy(actionlist_benef[i])
    #print(str(actionlist_roi[i]), str(actionlist_benef[i]))
client_roi.get_benef()
client_benef.get_benef()
print(str(client_roi))
