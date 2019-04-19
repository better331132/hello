from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
import random

# xor_data = [
#     [0, 0, 0],
#     [0, 1, 1],
#     [1, 0, 1],
#     [1, 1, 0]
# ]

# df = pd.DataFrame(xor_data)
# print(df.head)
# clf = svm.SVC(gamma='auto')
# clf.fit(df.loc[:, 0:1], df.loc[:, 2])

# pred = clf.predict([[0, 1], [1, 0], [1, 1], [2, -1]])
# score = metrics.accuracy_score([1,1,0, 1], pred)
# print("df=",df)
# print("df head=",df.head)
# print(pred)
# print(score)


# test_data =[
#     [0, 0, 0],
#     [1, 1, 1],
#     [2, 2, 4],
#     [3, 3, 27],
#     [4, 4, 64],
#     [1, 2, 1],
#     [2, 3, 8],
#     [3, 2, 9]
# ]

# testdf = pd.DataFrame(test_data)
# clf.fit(testdf.loc[:, 0:1], testdf.loc[:, 2])

# testpred = clf.predict([[2,4]])
# print("testpred=", testpred)

# gara_data =[]
# for i in range(100):
#     for j in range(100):
#         gara_data.append( [i, j, 2 * i + 3 * j - round(random.uniform(-(i+j), (i+j))/10, 2)])
# print(gara_data)

# garadf = pd.DataFrame(gara_data)
# clf.fit(garadf.loc[:, 0:1], garadf.loc[:,2])
# garapred = clf.predict([[12.5,13]])
# print("garapred=", garapred)

# score = metrics.accuracy_score([64], garapred)
# print(score)

test_data2 = [
    [-1, 0, 0, 0],
    [0, -1, 0, 0],
    [0, 0, -1, 0],
    [0, 0, 0, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 2],
    [2, 1, 0, 2],
    [1, 2, 0, 2],
    [0, 1, 2, 2],
    [0, 2, 1, 2],
    [1, 0, 2, 2],
    [2, 0, 1, 2]
]
testdf2 = pd.DataFrame(test_data2)
clf = svm.SVC(gamma='auto')
clf.fit(testdf2.loc[:, 0:2], testdf2.loc[:,3])
test2pred = clf.predict([[-1, -1, -1], [0.1, 0.1, 0.1], [0,0,0.9], [0,0.9,0], [0.9,0,0], [0,0,1.1], [0,1.1,0], [1.1,0,0], [0, 0.9, 0.9], [0, 1.1, 1.1], [2, 2, 2]])

print("test2pred = ", test2pred)
