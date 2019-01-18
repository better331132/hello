import random
from pprint import pprint
# import operator
data = {
    "A" : [
        [9, -9, -4,  3,  6],
        [7, -3, -8,  4,  4],
        [7, -9,  1, -2,  8],
        [5, -3, -4, -9, -8],
        [8,  5, -5,  4,  6]
    ],

    "B" : [
        [ 2, -7,  2, -2,  0],
        [ 1,  8,  2,  2, -2],
        [ 6, -2,  5, -2,  5],
        [-4,  9, -5, -9, -7],
        [ 8,  0, -9,  2, -7]
    ],

    "C" : [
        [-9,  5, -1,  9,  4],
        [ 3, -4, -6, -3,  3],
        [ 6,  6,  7, -3, -6],
        [-8,  9,  6, -1, -2],
        [-10, 2, -8, -4,  9]
    ]
}

lst = data.keys()
matrix_sum = {}
for matrix in lst:
    sum = 0
    for i, a in enumerate(data[matrix]):
        row_sum = a[i] + a[-1-i]
        sum += row_sum
    matrix_sum[matrix] = sum
print(matrix_sum)

# t = min(matrix_sum, key=lambda k: matrix_sum[k])
# print("Result is {}".format(t))

t = min(matrix_sum.items(), key=lambda k: k[1])
print("Result is {}".format(t[0]))

reverse_dict = dict((v,k) for k,v in matrix_sum.items())
print(reverse_dict)
l = min(reverse_dict.keys())
print(reverse_dict[l])


# sorted_matrix_sum = sorted(matrix_sum.items(), key=operator.itemgetter(1))
# least_value_matrix = sorted_matrix_sum.pop(0)
# print("Result is {}".format(least_value_matrix[0]))

# t = min(matrix_sum.items(), key=lambda x: x[1]) 