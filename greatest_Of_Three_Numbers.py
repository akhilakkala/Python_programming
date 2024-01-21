n1 = int(input("Enter the first number : "))
n2 = int(input("Enter the second number : "))
n3 = int(input("Enter the third number : "))

# BY USING IF-ELIF-ELSE STATEMENTS
if n1 >= n2:
    if n1 >= n3:
        print(f"n1 = {n1} is the greatest among {n1} , {n2} and {n3}")
elif n2 >= n1:
    if n2 >= n3:
        print(f"n2 = {n2} is the greatest among {n1} , {n2} and {n3}")
    else :
        print(f"n3 = {n3} is the greatest among {n1} , {n2} and {n3}")
        
        
# BY USING IF-ELSE STATEMENT
# if n1>n2:
#     if n1>n3:
#         print(f"n1 = {n1} is the greatest among {n1} , {n2} and {n3}")
#     else:
#         print(f"n3 = {n3} is the greatest among {n1} , {n2} and {n3}")
# else:
#     if n2>n3:
#         print(f"n2 = {n2} is the greatest among {n1} , {n2} and {n3}")
#     else:
#         print(f"n3 = {n3} is the greatest among {n1} , {n2} and {n3}")
               