l=[]
for i in range(5):
    n=input("Enter no: ")
    sum=0
    for j in n:
     sum += ord(j)
    l.append([sum,n])
print(sorted(l,reverse=True))
