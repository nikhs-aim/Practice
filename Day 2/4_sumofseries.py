#(1*1)+(2*2)+...(n*n)


a=int(input('enter the number: '))
sum=0
for i in range(1,a+1):
    sum+=i*i
print('the sum of the series (1*1)+...+ ({}*{}) is {}'.format(a,a,sum))