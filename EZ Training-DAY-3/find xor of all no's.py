#for the given number n find the xor of all numbers
n=5
xor=0
for i in range(1,n+1):
    xor=xor^i
print(xor)

#optimize
n=7
xor=0
if n%4==0:
    print(n)
elif n%4==1:
    print(1)
elif n%4==2:
    print(n+1)
elif n%4==3:
    print(0)