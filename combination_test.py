from itertools import combinations
from model import Client, Action
import csv
import time

start = time.perf_counter_ns()
actionlist = []
combined_list = list()
client_list = []
with open("dataset1_Python+P7.csv") as dataset:
    data = csv.reader(dataset, delimiter=",", quotechar="|")
    next(data)
    for row in data:    #O(n)
        action = Action(row)
        if action.price <= 0 or action.roi <= 0:
            continue
        else:
            actionlist.append(action)

actionlist.sort(key=(Action.get_roi), reverse=True) #O(n*log(n))

combined_list_1 = combinations(actionlist, len(actionlist)-1) # O[n (n-1)]


for item in combined_list_1: #O(n)^2
    temp_cli = Client()
    for action in item: #O(n)
        temp_cli.buy(action)
    client_list.append(temp_cli)
client_list.sort(key=(Client.get_benef), reverse=True) # #O(n*log(n))
print(str(client_list[0]))
print(time.perf_counter_ns()-start)

 # O(n)^2+ O(n*log(n)) + O[n (n-1)] + O(n)
