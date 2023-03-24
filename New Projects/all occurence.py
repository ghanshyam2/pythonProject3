def all_occurrence(string):
    output = ''

    for ch in string:
        if ch not in output:
            output += ch
    return output


print(all_occurrence("aaabbcdef"))
print(all_occurrence("abbbccccddddefzib"))
