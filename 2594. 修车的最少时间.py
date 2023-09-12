from math import sqrt
def repairCars(ranks, cars):
    ranks.sort()

    left = 1
    right = repairTime(ranks[0],cars)

    while left < right:
        totalNum = 0
        middle = calMiddel(right,left)
        for x in range(0,len(ranks)):
            totalNum = totalNum + repairNum(ranks[x],middle)
        if totalNum >=  cars:
            right = middle
        else :
            left = middle + 1
        print(f"left:{left}   right:{right}   totalNum:{totalNum}")

    return left

def calMiddel(right,left):
    return int((right + left) / 2)

def repairNum(r,t):
    return int(sqrt(t / r))

def repairTime(r,n):
    return r * n * n

ranks = [1,1,3,3]
cars = 74

repairCars(ranks,cars)
#576