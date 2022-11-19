# decimal to binary

a=int(input('enter the decimal number: '))
d=a
c=''
while a>0:
    b=a%2
    c+=str(b)
    a//=2
print('the binary number of {} is {}'.format(d,c[-1::-1]))




#binary to decimal

a=list(input('enter the binary number: '))
b=a
a.reverse()
s=0
for i in range(len(a)):
   s+=int(a[i])*2**i
print('the decimal value of is {}'.format(s))