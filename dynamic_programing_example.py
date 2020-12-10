

from numpy import random
from time import time

random.seed(323134)
list = random.randint(10000, size=(2000))
list2 = list.copy()


def buble():
    # print(list)
    lenght = len(list) - 1

    for index in range(lenght):
        for index in range(lenght):
            if (list[index] > list[index + 1]):
                list[index], list[index + 1] = list[index + 1], list[index]

    return list


def buble2():
    # print(list2)
    lenght = len(list2) - 1
    for index in range(lenght):
        for index in range(lenght):
            backward = lenght - index
            median = lenght / 2;
            if (index <= median):
                if (list[index] > list[index + 1]):
                    list[index], list[index + 1] = list[index + 1], list[index]
            if (backward > median):
                if (list[backward] < list[backward - 1]):
                    list[backward], list[backward - 1] = list[backward - 1], list[backward]

    return list



def peformance(call):
    start = time()

    sorted = call()
    # print(sorted)
    end = time()
    print(end - start)


def zad1(n):
    if (n == 1) or (n == 2):
        return n
    else:
        return zad1(n - 1) + zad1(n - 2)




def fib_memo(n):
    memo = [None] * (n + 1)
    return zad1mem(n, memo)

def zad1mem(n, memo):
    if (memo[n] is not None):
        result = memo[n]
        return result
    if (n == 1) or (n == 2):
        return n
    else:
       result = zad1mem(n - 1,memo) + zad1mem(n - 2,memo)

    memo[n] = result
    return result


print(fib_memo(20))
print(zad1(10))

peformance(buble)
peformance(buble2)
