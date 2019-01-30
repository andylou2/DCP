# This problem was asked by Google.

# You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

#   1
#  2 3
# 1 5 1
# We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

# Write a program that returns the weight of the maximum weight path.
def left_parent((x,y)):
    x = x - 1
    y = y - 1
    if x >= 0 and y >= 0:
        return (x, y)
    else:
        return None

def right_parent((x,y)):
    x = x - 1
    if x >= 0:
        return (x, y)
    else:
        return None

def left_child((x, y)):
    return (x+1, y)

def right_child((x, y)):
    return (x+1, y+1)

def val(tri, (x,y)):
    try:
        return tri[x][y]
    except:
        return None

def max_path(tri):
    # stack = [(0,0)]
    # while len(stack > 0):
    #     curr = stack.pop()
    #     l = left_child(curr)
    #     r = right_child(curr)
    #     v = val(tri, curr)

    # for i in range(len(tri) - 1, -1, -1):
    bot = len(tri) - 1
    max_paths = []
    for i in range(len(tri[bot])):
        max_paths.append(max_path_recurse(tri, (bot, i)))

    print("max paths is: ")
    print(max(max_paths))
    return max(max_paths)


def max_path_recurse(tri, (x, y)):
    l = left_parent((x, y))
    r = right_parent((x, y))
    curr_val = val(tri, (x, y))
    print(x, y, curr_val)
    print("left: {}, right: {}".format(l, r))
    if curr_val == None:
        return 0
    if l == None and r == None:
        return 0
    elif l == None and r != None:
        return curr_val + max_path_recurse(tri, r)
    elif l != None and r == None:
        return curr_val + max_path_recurse(tri, l)
    else:
        return curr_val + max(max_path_recurse(tri, l), max_path_recurse(tri, r))

    # max_path_recurse(tri, left_parent((x, y)))
    # max_path_recurse(tri, right_parent())





def main():
    tri = [[1], [2, 3], [1, 5, 1]]
    max_path(tri)

if __name__ == '__main__':
    main()