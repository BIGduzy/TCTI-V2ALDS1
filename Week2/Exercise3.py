from Week2.Exercise2 import MyStack


def validate_string(s):
    validation_stack = MyStack()
    brackets = {'>': '<', ']': '[', ')': '('}
    for c in s:
        if c in brackets:
            if validation_stack.is_empty() or validation_stack.pop() != brackets[c]:
                return False
        else:
            validation_stack.push(c)

    return validation_stack.is_empty()


# Test 1
print(validate_string(""))
print(validate_string("<>"))
print(validate_string("[]"))
print(validate_string("()"))
print(validate_string("{}"))
print(validate_string("(aa)"))
print()

# test 2
print(validate_string("((<>)())"))
print(validate_string("[(<>)]()(()())"))
print(validate_string("((<>))"))
print()

# test 3
print(validate_string("([)]"))
print(validate_string("(((<)>))"))
