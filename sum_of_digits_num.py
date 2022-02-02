n = int(input('enter a number'))
sum = 0
while(n>0):
    dig = n%10
    sum = sum + dig
    n = n//10
print('sum of a given number is: ', sum)
