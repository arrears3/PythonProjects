A = input("Enter string: ")
list1 = A.split()
print(list1[0])
name, sic, redg, mobile = set(), set(), set(), set()
for i in list1:
    if i.isdigit():
        if len(i)==10 and i[0]=='9':
            mobile.add(i)
        elif len(i)==10 and i[0]=='2':
            redg.add(i)
    elif i.isalpha() and not (i.isdigit() and i.isalnum()):
            name.add(i)
    elif i.isalnum() and not (i.isalpha() and i.isdigit()):
            sic.add(i)
print("name:",name)
print("sic:",sic)
print("redg:",redg)
print("mobile:",mobile)


