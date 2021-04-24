# Given a list, write a Python program to swap first and last element of the list


def swaplist(alist):
    X = len(alist)
    a0 = alist[0]
    an = alist[X-1]
    alist[0] = an
    alist[X-1] = a0
    return alist


Input = input("Enter comma separated list for a list \t")
input_list = Input.split(",")
print("The swapped list is", swaplist(input_list))



