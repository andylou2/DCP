# This problem was asked by Facebook.

# Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

# For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".

# consider multiple types of brackets:


def balance(s):
    stack = []
    res = ""
    count = 0
    for c in s:
        if c == '(':
            stack.append(c)
            res += c
        elif len(stack) == 0 and c == ')':
            count += 1
        else:
            stack.pop()
            res += c
    if len(stack) > 0:
        for ele in stack:
            res += ')'
            count += 1
    return count, res


def main():
    s = '))()('
    edits, res = balance(s)
    print(edits, res)


if __name__ == '__main__':
    main()