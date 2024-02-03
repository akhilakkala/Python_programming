
p = int(input("Enter a power number : "))
b = int(input("Enter a base number: "))

def reccur_pow(b,p):
     if p==1:
         return b
     else:
         return b * reccur_pow(b,p-1)

# By recurrsive function
print(reccur_pow(b,p))

# By using direct inbuilt func    
print(pow(b,p))

