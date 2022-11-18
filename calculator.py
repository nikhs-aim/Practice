print('press \'1\' to perform addition' )
print('press \'2\' to perform subtraction' )
print('press \'3\' to perform multiplication' )
print('press \'4\' to perform division' )
print('press \'5\' to find the remainder' )
print('press \'6\' to find the quotient' )

a=int(input('enter a number: '))

b=int(input('enter a number: '))

operator=input('enter the sign of the operation you have to perform: ')

if operator=='1':
    print(a+b)

if operator=='2':
    print(a-b)

if operator=='3':
    print(a*b)

    
if operator=='4':
    print(a/b)

if operator=='5':
    print(a%b)

if operator=='6':
    print(a//b)