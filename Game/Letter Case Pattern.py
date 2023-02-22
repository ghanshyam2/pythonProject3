def letter_case_P(s):
    list_string = [""]
    for ch in s:
        temp = []
        if ch.isalpha():
            for out in list_string:
                temp.append(out + ch.lower())
                temp.append(out + ch.upper())
        else:
            for out in list_string:
                temp.append(out + ch)
        list_string = temp
    return list_string


print(letter_case_P("3z4"))
print(letter_case_P("a1b2"))
