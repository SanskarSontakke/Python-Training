a = int(input("Enter your first number"))
b = int(input("Enter your second number"))

def minium(x,y):
    if x >= y :
        return x
    elif y >= x :
        return y
    
print("Largest number is",minium(a,b))