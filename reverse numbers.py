n=input("Enter no ")[::-1]
print(n)
for i in set(n):
    print(i,"frequency= ",n.count(i))
