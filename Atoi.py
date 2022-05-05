def myAtoi(s: str) -> int:
    extracted_number = ''
    chars_list = []
    digits_list = []
    counter = 0
    for i in s:
        if i.isdigit():
            extracted_number += i
            digits_list.append(counter)
        elif i == '-':
            extracted_number += i
        elif i.isalpha():
            chars_list.append(counter)
        counter+=1

    print("extracted_number: ", extracted_number)
    if len(chars_list)==0 or len(digits_list)==0:
        return int(extracted_number)
    elif max(chars_list) < max(digits_list):
        return 0
    elif int(extracted_number) > -2 ** 31 and int(extracted_number) < (2 ** 31) - 1:
        return int(extracted_number)
    else:
        return 0

print(myAtoi(' 56767 shobhit    '))