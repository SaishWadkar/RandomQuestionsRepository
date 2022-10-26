'''
    Please ignore the print statements used for debugging purpose.
'''

def solution(A):
    '''
        This function calculates smallest positive integer that does not occur in A
    :param A: an array or list of n integers
    :return: smallest positive integer (greater than 0) that does not occur in A.
    '''

    # sort the list A
    A.sort()
    print(f"Sorted A with : {A} ")

    # calculate length of list A
    l = len(A)
    print(f"Length of list A : {l} ")

    # if list is empty return None
    if l==0:
        return None

    # calculate max element of list A
    m = max(A)
    print(f"Max element of list A : {m} ")

    # if maximum integer in list is negative or 0 then naturally next positive integer would be 1
    if m<=0:
        return 1

    for i in range(1,m+1):
        if i not in A:
            return i
    else:
        return i+1


# sample test cases
# A = [1,2,3,4,5]
# A = [1,3,6,4,1,2]
# A = [5,5,5,5]
# A = [3,10,25,-1,-2,-1,-4]
# A = [1,2,3,3,3,7,7,7]
# A = [9,8,7,6]
# A = [-1,-2,-3]
A = [-1,-2,-3,0,55]
# A = []

s = solution(A)
print(s)
