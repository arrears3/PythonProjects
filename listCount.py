size=int(input("Enter the size of the list "))
l1=[]
count=0
print("Enter a list of strings")
for i in range(size):
    l1.append(input())
for i in l1:
    l=len(i)
    if(l>=2 and i[0]==i[-1]):
        count=count+1
print("The no.of elements satisfying the condition are :",count)
