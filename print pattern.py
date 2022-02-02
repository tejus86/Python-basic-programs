# print pattern below
# *
# $$
# ***
# $$$$
# *****
# $$$$$$ 

n = int(input("enter num"))
for i in range(1,n):
    if i%2==0:
        print(i * "$")
    else:
        print(i * "*")
