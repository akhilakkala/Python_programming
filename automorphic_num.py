def automorphic_num(n):
    
    val = n**2
    s = str(val)
    l = len(str(n))
    x = s[-l :]
    ns = str(n)
    if ns ==x:
        print(f"The number {n} is an automorphic number ")
    else:
        print(f"The number {n} is not an automorphic number")
        
    

num = int(input("Enter any number :"))

automorphic_num(num)

# x = str(223)
# print(type(x))
# y = x[-2:-1]
# print(y)
# print(len(y))