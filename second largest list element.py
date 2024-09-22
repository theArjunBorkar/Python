def sec_largest(lst):
    if len(lst) < 2:
        return None
    largest = max(lst)
    sec_largest = None
    for i in lst:
        if i != largest and (sec_largest is None or i > sec_largest):
            sec_largest = i
    return sec_largest
lst = eval(input("Enter a list: "))
print("The second largest number is", sec_largest(lst))
