a=[]
entry=int(input('enter how many numbers you want to enter: '))
print('start entering the number\n')
while entry>0:
    n=(input('enter the number: '))
    a.append(n)
    entry-=1
print('the maximum value is: ',max(a))
print('the minimum value is: ',min(a))


#to find max value
# maximum=a[0]
# for i in a:
#     if i>maximum:
#         maximum=i
# print(maximum)
