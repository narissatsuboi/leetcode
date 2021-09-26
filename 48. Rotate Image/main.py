"""
You are given an n x n 2D matrix representing an image, rotate the image
 by 90 degrees (clockwise). You have to rotate the image in-place,
 which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
"""

__version__ = '1'
__author__ = 'Narissa Tsuboi'


def rotate(matrix):
    """
    Approach TC O(N2), SC O(1)
    1. Transpose rows.
    2. Reverse rows.
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix[0])  # n x n matrix

    # Transpose rows into columns starting at 0,0 using swap
    for i in range(n):
        for j in range(i, n):
            # swap each element
            # note if you wanted to just swap a row, just use the first []
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse elements in each row
    # Use first n/2 elements as outer loop
    for i in range(n//2):
        for j in range(n):
            # j comes first because were swapping elements within a row via
            # columns j
            matrix[j][i], matrix[j][n-1-i]=matrix[j][n-1-i], matrix[j][i]


def print_matrix(matrix):
    for i in range(len(matrix[0])):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print_matrix(matrix)
    print()
    rotate(matrix)
    print_matrix(matrix)