
n1 = int(input("Enter any number : "))
l = []
for i in range(1, (n1//2)+1):
    if(n1%i==0):
        l.append(i)
l.append(n1)
print(f"The factors of {n1} are : " , l)