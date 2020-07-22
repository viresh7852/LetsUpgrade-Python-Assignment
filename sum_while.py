'''Sum of n numbers using while'''

n= int(input("please enter the value:: "))
itr=0
sum1=0
while (itr<n):
    sum1=itr+sum1
    print (itr,"-->",sum1)
    itr=itr+1
print ("Sum of number is ",sum1)   