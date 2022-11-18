a=int(input('enter a number: '))
prime=True
if a==1:
    print('one is universal')
else: 
 for i in range(2,a):
    if a%i==0:
        prime=False        #if any number within the range divides the given number then set prime to false and break out of the loop
        break
 if prime:
    print('prime')
 else:
    print('not prime')

