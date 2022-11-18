a=int(input("enter the range upto whic you have to find the prime numbers: "))
n=2
b=[]
for i in range(2,a+1):
        if i%n!=0:
         b.append(i)
print('the prime numbers are: ',b)
       