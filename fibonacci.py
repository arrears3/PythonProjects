def fibonacci(n):
    if n<=1:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))
j = int(input("How many terms?"))
if j <=0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(j):
        print(fibonacci(i))
