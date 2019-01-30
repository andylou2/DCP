# This problem was asked by Palantir.

# Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
import math


# def is_pali(n):
#     rev = 0
#     curr = n
#     while curr > 10:
#         end = curr % 10
#         rev += end * (10**(int(math.log10(curr))))
#         curr = curr / 10
    
#     end = curr % 10
#     rev += end
#     if rev == n:
#         return True
#     else:
#         return False

def getDigit(index, num):
    return (num / 10**index) % 10

def is_pali(n):
    numDig = int(math.log10(n))
    halfDig = numDig / 2
    for currDig in range(numDig, halfDig, -1):
        end = getDigit(currDig, n)
        start = getDigit(numDig - currDig, n)
        if end != start:
            return False
    return True

def main():
    n = 123
    print(is_pali(n))

if __name__ == '__main__':
    main()