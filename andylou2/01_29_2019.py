# This problem was asked by Twitter.

# A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.

# Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

def apply_permutation(str, perm):
    # arr = [None for i in range(len(str))]
    # print(arr)
    # for i in range(len(str)):
    #     arr[i] = str[perm[i]]
    # print(arr)

    for i in range(len(str)):
        temp = str[i]
        str[i] = str[perm[i]]
        str[perm[i]] = temp
        temp2 = perm[i]
        perm[i] = perm[perm[i]]
        perm[temp2] = temp2

    print(str)

def main():
    str = ["a", "b", "c"]
    permutations = [2, 1, 0]
    apply_permutation(str, permutations)


if __name__ == '__main__':
    main()