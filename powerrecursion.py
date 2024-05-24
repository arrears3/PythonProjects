def power(a,n):
    if(n!=0):
         return(a*power(a,n-1))
    else:
        return 1
num = int(input("Enter the number to calculate the power: "))
p = int(input("Enter the power of number:"))
print("The resultant number is :",power(num,p))
    
