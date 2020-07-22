'''take an integer to find --prime or not'''

n = int(input("Enter a number: "))  
flag = 0
i = 2
while i <= n / 2:
    if n % i == 0:
        flag=1
        break
    i=i+1
    
if flag==0:
    print("The", n, "number is a PRIME number")
else:
    print("The", n, "number is not a PRIME number")