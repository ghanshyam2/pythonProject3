def reverse_string(string):
    str_ing = string.split()
    # print(" ".join(str_ing[::-1]))  #one liner
    left, high = 0, len(str_ing) - 1
    while left <= high:
        str_ing[left], str_ing[high] = str_ing[high], str_ing[left]
        left += 1
        high -= 1
    # return str_ing # print string as list
    return " ".join(str_ing)


print(reverse_string("learning python is easy"))
print(reverse_string("nothing is permanent so chill"))
print(reverse_string("everything comes at some cost try not pay early"))
print(reverse_string("someday you have to move from the place where you at today"))
