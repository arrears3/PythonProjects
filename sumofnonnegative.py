def summation(n):
    if(n!=0):
        j=n%10
        k=n//10
        return(j+summation(k))
    else:
        return 0
i = int(input("Enter a number: "))
print("The summation is",summation(i))
