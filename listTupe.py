list1=[(2,5),(1,2),(4,4),(2,3),(2,1)]
l=len(list1)
temp=()
for j in range(l):
    for i in range(l-1):
        if(list1[i][1]>list1[i+1][1]):
            temp=list1[i]
            list1[i]=list1[i+1]
            list1[i+1]=temp
print(list1)
