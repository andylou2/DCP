# This problem was asked by Google.

# Given two rectangles on a 2D graph, return the area of their intersection. If the rectangles don't intersect, return 0.

# For example, given the following rectangles:

# {
#     "top_left": (1, 4),
#     "dimensions": (3, 3) # width, height
# }
# and

# {
#     "top_left": (0, 5),
#     "dimensions" (4, 3) # width, height
# }
# return 6.

def findIntersection(a, b):
    top_left1 = a["top_left"]
    top_left2 = b["top_left"]
    
    dim1 = a["dimensions"]
    dim2 = b["dimensions"]

    left1 = top_left1[0]
    left2 = top_left2[0]

    width1 = dim1[0]
    width2 = dim2[0]

    height1 = dim1[1]
    height2 = dim2[1]

    right1 = left1 + width1
    right2 = left2 + width2

    top1 = top_left1[1]
    top2 = top_left2[1]

    bot1 = top1 - height1
    bot2 = top2 - height2

    # print(left2, right1, right2, left1)
    # print(bot2, top1, top2, bot1)

    if left2 >= right1 or right2 <= left1:
        return 0
    if bot2 >= top1 or top2 <= bot1:
        return 0

    print("the rectangles intersect")

    width = 0
    if left2 < left1 and right2 >= right1:
        width = right1 - left1
    elif left2 >= left1 and right2 <= right1:
        width = right2 - left2
    elif left2 >= left1 and right2 >= right1:
        width = right1 - left2
    elif left2 <= left1 and right2 <= right1:
        width = right2 - left1

    height = 0
    if bot2 < bot1 and top2 >= top1:
        height = top1 - bot1
    elif bot2 >= bot1 and top2 <= top1:
        height = top2 - bot2
    elif bot2 >= bot1 and top2 >= top1:
        height = top1 - bot2
    elif bot2 <= bot1 and top2 <= top1:
        height = top2 - bot1

    print(width)
    print(height)

    return width * height


def main():
    rect1 = {"top_left": (0, 0),
             "dimensions": (1, 1)}
    rect2 = {"top_left": (0, 1),
             "dimensions": (1, 1)}
    print(findIntersection(rect1, rect2))


if __name__ == '__main__':
    main()