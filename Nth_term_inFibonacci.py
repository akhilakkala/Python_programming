
def nth_Fibonacci_term(n):
    if n < 2:
        return n
    else:
        return nth_Fibonacci_term(n-1) + nth_Fibonacci_term(n-2)

x = int(input("Enter any number : "))

print(f"The {x}th term in fibonacci series is : " , nth_Fibonacci_term(x-1))
    
