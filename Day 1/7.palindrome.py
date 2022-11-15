a=input('enter the numbers or a text to find it is palindrome or not: ')
b=str(a)[::-1]
if b==a:
    print('palindrome')
else:
    print('not a palindrome')

