def factorial(i):
    if i==0:
        return 1
    else:
        return factorial(i-1)*i 

i=int(input("enter a no."))
print(factorial(i))