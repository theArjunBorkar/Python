n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))
n3 = int(input("Enter the third number: "))
if n1 > n2 and n1 > n3:
    print(n1, "is the largest")
elif n2 > n3 and n2 > n1:
    print(n2, "is the largest")
else:
    print(n3, "is the largest")
