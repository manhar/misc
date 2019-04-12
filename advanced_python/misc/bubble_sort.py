#!/anaconda/bin/python

"""
This program will count the sort a list of integers using bubble sort algorithm
"""

a = list(int(x) for x in '123')
n = len(a)
numOfSwaps = -1
TotalNumOfSwaps = 0
while numOfSwaps != 0:
    #print(TotalNumOfSwaps, numOfSwaps,a)
    numOfSwaps = 0
    for i in range(n-1):
        if a[i] > a[i+1]:
            x = a[i]
            a[i] = a[i+1]
            a[i+1] = x
            numOfSwaps += 1

    TotalNumOfSwaps +=numOfSwaps

print("Array is sorted in {} swaps.".format(TotalNumOfSwaps))
print("First Element:",a[0])
print("Last Element:",a[len(a)-1])
print(a)


