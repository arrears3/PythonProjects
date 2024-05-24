def readfile():
    f=open("read.txt","r")
    print (f.read())
    f.close()

def appendfile():
    f=open("read.txt","a")
    f.write(input("enter a string"))
    f.close()
    
def writefile():
    f=open("read.txt", "w+")
    f.write(input("enter the string")) 
    f.close()
    
input=int(input("enter 1 to read,enter 2 to append,enter 3 to write"))   
  if input== 1
    print("read the statement")
 elif input==2
    