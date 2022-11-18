#(1)+(1*2)+(1*2*3)+.......

a=int(input('enter the number: '))
s=0
m=1
while a>0:
    for i  in range(1,a+1):
        m*=i
        s+=m
    a-=1
    m=0
print('the sum of the series is: ',s)