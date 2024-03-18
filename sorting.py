import math
class Node:
    def __init__(self, value, next):
        self.value = value
        self.naxt = next

n3 = Node("third", None)
n2 = Node('econd', n3)
n1 = Node('first', n2)

#Сортировка Шела
def ShellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

#Линейный поиск
def find_index(elements, value):
    for index, element in enumerate(elements):
        if element == value:
            return index

#Алгоритм сортировки пузырём
def bubbleSort(array):
    swapped = False
    for i in range(len(array)-1,0,-1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array