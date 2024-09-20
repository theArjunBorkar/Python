n = int(input("Enter the number of terms: "))
x, y = 0, 1
for i in range(x, n):
    print(x) 
    x, y = y, x + y
