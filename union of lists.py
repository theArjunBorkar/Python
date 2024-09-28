def union_of_lists(list_1, list_2):
    union_list = []
    for element in list_1:
        if element not in union_list:
            union_list.append(element)
    for element in list_2:
        if element not in union_list:
            union_list.append(element)
    return union_list
list_1 = eval(input("Enter list 1 elements: "))
list_2 = eval(input("Enter list 2 elements: "))
print("Union of list 1 and list 2:", union_of_lists(list_1, list_2))
