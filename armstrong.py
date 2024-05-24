print("Armstrong numbers Are :")
for i in range(200,100 , -1):

   order = len(str(i))
    
   sum = 0

   temp = i
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if i == sum:
       print(i)

print("Prime Numbers are :")
for j in range (200, 100 , -1):
    count = 0
    for i in range(2, (j//2 + 1)):
        if(j % i == 0):
            count = count + 1
            break

    if (count == 0 and j != 1):
        print(j,end='')
