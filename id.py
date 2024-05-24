i=input("Enter a string")
if i[:2] == "21" and i[2:4] == "01":
    print("regular")
    if (i[4:7]=="341"):
        print ("btech in regular batch in 2021")
    else:
        print(" btech in regular but not of sit 2021")
elif (i[:2] == "22" and i[2:4] == "21"):
    print("LE")
    if(i[4:7]=="341"):
         print("Btech lateral student of sitwest of 2022 batch")
    else:
         print("Btech lateral student of but not of sitwest of 2022 batch")
else:
    print("invalid")
