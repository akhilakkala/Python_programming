# BY RECURSSION
def fibonacciNterm(n , a=0 , b=1):
    if a<=n:
        print(a , end = " ") 
        fibonacciNterm(n , b , a+b)

fibonacciNterm(5)   


# BY BASIC ITTERATION
n = int(input("Enter any number : "))
l = [0,1]
prev=0
curr=1
for i in range(2,n):
    next=prev+curr
    l.append(next)
    prev = curr
    curr = next
    
print(l)