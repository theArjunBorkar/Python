def remove_dupes(lst):
    new_list = []
    for element in lst:
        if element not in new_list:
            new_list.append(element)
    return new_list
List = eval(input("Enter list elements: "))
result = remove_dupes(List)
print("List without duplicated elements:", result)
