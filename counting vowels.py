def vowel_cnt(string):
    vowels = "aeiouAEIOU"
    count = 0
    for chr in string:
        if chr in vowels:
            count += 1
    return count
string = input("Enter a string: ")
print("Vowel count =", vowel_cnt(string))
