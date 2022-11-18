#direct method

a=int(input('enter a number: '))
b=int(input('enter a number: '))
print('{} rise to {} is {}'.format(a,b, a**b))



#using loops

a=int(input('enter a number: '))
b=int(input('enter a number: '))
d=b
c=1
while b>0:
    c*=a
    b-=1
print('{} rise to {} is {}'.format(a,d,c))