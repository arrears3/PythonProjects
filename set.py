A = {int(x) for x in input("Enter set A elements: ").split()}
B = {int(x) for x in input("Enter set B elements: ").split()}

not_found = False

for a in A:
    if a * a not in B:
        print(a, "is not a square of any element in set B")
        not_found = True

if not not_found:
    print("All elements in A have their squares present in set B.")
