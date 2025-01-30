def swap_case(s):
    num = ""
    for letter in s:
        if letter.isupper() == True:
            num+=(letter.lower())
        else:
            num+=(letter.upper())
    return num


print(swap_case('IsaAn'))