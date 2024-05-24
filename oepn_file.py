cnt = ""
with open("demo.txt","r") as f:
    cnt = f.read()
    print(cnt)
with open("demo1.txt","w+") as f:
    f.write(cnt)