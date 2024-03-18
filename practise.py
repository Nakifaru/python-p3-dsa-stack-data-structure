def reserve_string(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed = ""
    while stack:
        reversed += stack.pop()

    return reversed

print(reserve_string("hello"))

# Without stack

# def evaluate_keystrokes(string):
#     i = len(string) - 1
#     result = ""
#     skip = 0

#     while i >= 0:
#         if string[i] == "<":
#             skip += 1
#             i -= 1
#         else:
#             if skip > 0:
#                 i -= skip
#                 skip = 0
#             else:
#                 result = string[i] + result
#                 i -= 1
#     return result

# With stack

def evaluate_keystrokes(string):
    stack = []
    for char in string:
        if char == "<":
            if len(stack) != 0:
                stack.pop()
        else:
            stack.append(char)

    result = ''
    while stack:
        result = stack.pop() + result

    return result