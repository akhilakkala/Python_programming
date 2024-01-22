n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))

for n in range(n1,n2+1):
    pow_val = len(str(n))
    sum = 0
    temp = n
    while temp>0:
        dig = temp%10
        sum += dig ** pow_val
        temp //= 10
    if(sum==n):
        print(n , end = ",")

        
    