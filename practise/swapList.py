# Given a list, write a Python program to swap first and last element of the list
#https://www.practicepython.org/exercises/

''' Aprogram to test'''

def swaplist(alist):
    ''' A Simple program '''
    my_list = alist[1:(len(alist) -1)]
    n_last = alist.pop()
    n_first = alist.pop(0)
    return [n_last] + my_list + [n_first]



#print(swaplist([1,2,3,4,5]))