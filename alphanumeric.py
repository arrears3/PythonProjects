for i in input("Enter the string:"):
  if i.isalnum() and not(i.isalpha() and i.isdigit()):
    print(i)
