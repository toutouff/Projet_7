
def bubble_sort(list, key=None, reverse=False):
    if key == None:
        for i in range(len(list), 1, -1):
            sorted = True
            for j in range(0, i-1):
                if list[j+1] < list[j]:
                    temp = permutation(j, list)

                    sorted = False
            if sorted:
                break
    elif key != None:
        for i in range(len(list), 1, -1):
            sorted = True
            for j in range(0, i-1):
                if key(list[j+1]) < key(list[j]):
                    temp = permutation(j, list)
                    list = temp
                    sorted = False
            if sorted:
                break
    if reverse:
        return list.reverse()
    else:
        return list


def permutation(i, list):
    temp = list[i]
    list[i] = list[i+1]
    list[i+1] = temp
    return list
