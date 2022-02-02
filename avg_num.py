# program to calculate average of numbers in a list in python

n = int(input('enter the number of elements to be inserted: '))
res = []
for i in range(0,n):
    elem = int(input('enter element: '))
    res.append(elem)
    avg = sum(res)/n
print('average of elements in the list', round(avg,2))
