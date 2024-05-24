name=input("ENTER THE NAME OF THE STUDENT")
print(name)
a=int(input("ENTER THE MARK OF FIRST SUBJECT"))
b=int(input("ENTER THE MARK OF SECOND SUBJECT"))
c=int(input("ENTER THE MARK OF THIRD  SUBJECT"))
d=int(input("ENTER THE MARK OF FOURTH SUBJECT"))
e=int(input("ENTER THE MARK OF FIFTH SUBJECT"))
avg= int
avg=a+b+c+d+e/5
print(avg)
if avg>=90 :
    print("YOU SCORED A")
elif avg>=80 and avg<90 :
    print("YOU SCORED B")
elif avg>=70 and avg<80 :
    print("YOU SCORED C")
elif avg>=60 and avg<70 :
    print("YOU SCORED D")
else :
 rearprint("FAIL")
