def difference(list_1, list_2):
    diff_list = []
    for element in list_1:
        if element not in list_2:
            diff_list.append(element)
    return diff_list
list_1 = eval(input("Enter list 1 elements: "))
list_2 = eval(input("Enter list 2 elements: "))
print("Difference between list 1 and list 2:", difference(list_1, list_2))
