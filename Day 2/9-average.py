a=[]
for i in range(1,11):
    num=int(input('enter the number {}: '.format(i)))
    a.append(num)
print('the average of the numbers is: ',sum(a)/10)