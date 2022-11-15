a=int(input('enter the number to find its factorial: '))
fact=1
for i in range(1,a+1):
    fact*=i
print(f'the factorial of {a} is',fact)


