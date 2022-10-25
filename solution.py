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

    # remove all negative numbers from list A
    for i in A:
        if i<0:
            A.remove(i)

    # print(f"Sorted A with -ve adjust : {A} ")

    # calculate length of list A
    l = len(A)
    # print(f"Length of list A : {l} ")

    # generate indices for length l of list A
    indices = [i for i in range(l)]

    # zip indices and corresponding list element (index,element in A) eg. (0,2)
    # print("Zip")
    s = zip(indices,A)

    # print("Logic")

    # logic
    for i,j in s:
        if A[0]>1:
            return 1

        if i<=l-2:
            # print("Difference")
            if A[i+1]-A[i]>1:
                return A[i]+1
    else:
        # print("in else")
        n = A[-1]+1
        if n>=1:
            return n
        else:
            return 1


# sample test cases
A = [1,2,3,4,5]
# A = [1,3,6,4,1,2]
# A = [5,5,5,5]
# A = [-1,-2,-1,-4]
# A = [1,2,3,3,3,7,7,7]
# A = [9,8,7,6]

s = solution(A)
print(s)
