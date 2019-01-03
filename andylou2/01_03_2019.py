# This problem was asked by Google.

# Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

# Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

# For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

# Hint: Try working backwards from the end state.

def interleve(arr):
    q = []
    while len(arr) > 1:
        q.append(arr.pop())
        q.append(arr.pop())
        arr.append(q.pop(0))
    for ele in q:
        arr.append(ele)

    q2 = []
    while len(arr) > 0:
        q2.append(arr.pop())

    for ele in q2:
        arr.append(ele)
    return arr

def main():
    arr = [1, 2, 3, 4, 5]
    sol = interleve(arr)
    print(sol)

if __name__ == '__main__':
    main()
