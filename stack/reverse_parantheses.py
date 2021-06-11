"""
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

For inputString = "(bar)", the output should be
reverseInParentheses(inputString) = "rab";

For inputString = "foo(bar)baz", the output should be
reverseInParentheses(inputString) = "foorabbaz";

For inputString = "foo(bar)baz(blim)", the output should be
reverseInParentheses(inputString) = "foorabbazmilb";

For inputString = "foo(bar(baz))blim", the output should be
reverseInParentheses(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
"""


def reverseInParentheses(inputString):
    stack = list()
    res = ""

    for index, value in enumerate(inputString):
        if value == '(':
            stack.append(index)
        elif value == ')':
            temp = inputString[stack[-1]:index + 1]
            inputString = inputString[:stack[-1]] + temp[::-1] + inputString[index + 1:]
            stack.pop(-1)

    for c in inputString:
        if c != '(' and c != ')':
            res += c

    return res