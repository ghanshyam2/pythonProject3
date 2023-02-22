def isValid(str1):
    stack = []
    for st in str1:
        if st == 'c':
            if stack[-2:] != ['a', 'b']:
                return False
            stack.pop()
            stack.pop()
        else:
            stack.append(st)
    return not stack


print(isValid('aabcbc'))
