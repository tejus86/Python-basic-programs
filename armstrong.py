#Armstrong number is a number that is equal to the sum of cubes of its digits. For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
# 153 = 1^3 + 5^3 + 3^3 = 153
n = int(input('enter the number: '))
temp = n
armstrong = 0
while(n>0):
    dig = n%10
    armstrong = armstrong + dig**3
    n = n//10
if(temp == armstrong):
    print("num is armstrong")
else:
     print("num is not armstrong")
