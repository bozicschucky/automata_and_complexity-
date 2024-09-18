def balanced_parentheses(str):
    stack = []
    # Define states
    START = 'start'
    VALID = 'valid'
    INVALID = 'invalid'

    # Initialize stack to keep track of parentheses
    stack = []

    # Define transitions
    state = START

    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                state = INVALID
                break

    if state != INVALID and not stack:
        state = VALID
    else:
        state = INVALID

    return state == VALID


input_string1 = "(())"
input_string2 = "(()"
input_string3 = "())"
input_string4 = "()()"

# True
print(f"Is '{input_string1}' balanced? {balanced_parentheses(input_string1)}")
# False
print(f"Is '{input_string2}' balanced? {balanced_parentheses(input_string2)}")
# False
print(f"Is '{input_string3}' balanced? {balanced_parentheses(input_string3)}")
# True
print(f"Is '{input_string4}' balanced? {balanced_parentheses(input_string4)}")
