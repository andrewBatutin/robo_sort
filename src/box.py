
a = [1,2,3,4,5]

def average_1(list):
    res = 0
    return res

def average_2(list):
    res = 0
    for i in list:
        res += i
    return res/len(list)

def brain(list, goal):
    res1 = average_1(list)
    res2 = average_2(list)

    if abs(res1 - goal) < abs(res2 - goal):
        print("average_1")
    else:
        print("average_2")

brain(a, 3)
