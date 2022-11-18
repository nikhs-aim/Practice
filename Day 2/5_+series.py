# (1)+(1+2)+....(1+2+...n)


a=int(input('enter the number: '))
s=0
while a>0:
    for i in range(a+1):
        s+=i
    a-=1
print('the sum of the series is', s)