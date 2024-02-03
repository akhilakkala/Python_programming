#BY Recurrsion

def factorial(n):
    if(n==0 | n==1 ):
        return n
    return n*factorial(n-1)

x = int(input("Enter any Number : "))
print(f"The value of {x}! is ",factorial(x))