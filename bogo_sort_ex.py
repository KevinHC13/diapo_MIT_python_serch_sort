import random
def is_sorted(L):
    sort = True
    for i in range(0,len(L)-1):
        if L[i] > L[i+1]:
            sort = False
    return sort
def bogo_sort(L):
    while not is_sorted(L):
        random.shuffle(L)
    return L

lista=[2,1,7,9,10]
print(bogo_sort(lista))
