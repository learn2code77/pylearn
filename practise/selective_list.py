'''https://www.practicepython.org/exercise/2014/04/25/12-list-ends.html
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only
the first and last elements of the given list. For practice, write this code inside a function.'''


def selective_list(a_list):
    b_list = []
    b_list.append(a_list[0])
    b_list.append(a_list[-1])
    print(" Your selective list is ", b_list)

def another_selective_list(c_list):
    print([c_list[0], c_list[-1]])


another_selective_list("1,2,3,4")
