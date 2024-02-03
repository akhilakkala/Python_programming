def abundant_num(n):
    total=0
    for i in range(1,(n//2)+1):
        if n%i==0:
            total +=i
        
    if(total>n):
        print(f"The number {n} is an abundant number")
    else:
        print(f"The {n} is not a abundant number")
 
m = int(input("Enter a number : "))           
abundant_num(m)