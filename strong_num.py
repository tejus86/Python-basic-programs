#Strong number is a number whose sum of all digits' factorial is equal to the number 'n'. ... 
# So, to find a number whether its strong number, 
# we have to pick every digit of the number like the number is 145 
# then we have to pick 1, 4 and 5 now we will find factorial of each number i.e, 1! = 1, 4! = 24, 5! = 120.

n = int(input('enter a number: '))
temp = n
sum = 0
while(n):
    fact = 1
    i=1
    r = int(n % 10)
    while(i<=r):
        fact = fact*i
        i=i+1
    sum = sum + fact
    n = int(n//10)
if(sum == temp):
    print('strong number')
else:
    print('not strong number')
    