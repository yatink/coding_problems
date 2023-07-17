import random

lst = random.sample(range(100000), 20)

def quicksort(inpt, pivot, lo, hi):
    if len(inpt) < 2:
        return inpt
    
    return \
        quicksort([i for i in inpt if i <= pivot], (pivot+lo)//2, lo, pivot) + \
        quicksort([i for i in inpt if i > pivot], (pivot+hi)//2, pivot, hi)

print(lst)
print(quicksort(lst, 50000, 0, 100000))