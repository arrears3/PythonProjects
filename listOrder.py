size=int(input("Enter the size of list :"))
l1=[]
l2=[]
print("Enter the elements of list 1")
for i in range(size):
    l1.append(int(input()))
print("Enter the elements of list 2")
for i in range(size):
    l2.append(int(input()))
print("List 1 show")
for i in range(size):
    print(l1[i],end=", ")
print("\n")
print("List 2 show")
for j in range(1,size+1):
    print(l2[-j],end=", ")
