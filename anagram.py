def anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    split_string_1 = sorted(list(str1.lower()))
    split_string_2 = sorted(list(str2.lower()))

    count = 0
    for index in range(0, len(split_string_1)):
        for inner_index in range(0, len(split_string_2)):
            if index is inner_index and split_string_2[index] is split_string_1[inner_index]:
                count +=1
        continue

    if count == len(split_string_1):
        return True
    else:
        return False


print(anagram('hello', 'edlloh'))
