lst = eval(input("Enter list elements: "))
print(lst)
minimum, maximum = lst[0], lst[0]
for i in range(len(lst)):
    if lst[i] > maximum:
        maximum = lst[i]
    if lst[i] < minimum:
        minimum = lst[i]
print("Maximum:", maximum)
print("Minimum:", minimum)
