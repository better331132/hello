from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
import struct
from pathlib import Path

csv = pd.read_csv('./data/iris.csv')       # csv[:4] : 0 ~ 4행
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']

trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)
clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel)
pred = clf.predict(testData)
score = metrics.accuracy_score(testLabel, pred)

def writeCsv(name):
    labelFile = open("./data/" + name + "-labels.idx1-ubyte", "rb")
    imageFile = open("./data/" + name + "-images.idx3-ubyte", "rb")
    csvFile = open("./data/" + name + ".csv", "w", encoding="utf-8")

    magicNo, labelCnt = struct.unpack(">II", labelFile.read(8))
    print(magicNo, labelCnt)
    magicNo, imageCnt = struct.unpack(">II", imageFile.read(8))
    print(magicNo, imageCnt)
    rows, cols = struct.unpack(">II", imageFile.read(8))
    pixels = rows * cols            # 28 X 28

    for i in range(labelCnt):
        label = struct.unpack("B", labelFile.read(1))[0]   # 답
        imgdata = list(map(lambda b: str(b), imageFile.read(pixels)))  # 28 * 28
        csvFile.write(str(label) + ",")
        csvFile.write(",".join(imgdata) + "\n")

    # for j, x in enumerate(imgdata):
    #     if j % 28 == 0:
    #         print("\n")
    #     print('{:4s}'.format(str(x)), end='')

    # print("\n\n label=", label)

    labelFile.close()
    imageFile.close()
    csvFile.close()

writeCsv('t10k')
writeCsv('train')

def readCsv(file, maxcnt):
    labels = []
    images = []
    with open(file, "r") as f:
        for i, line in enumerate(f):
            if i >= maxcnt:
                break
            cols = line.split(",")
            labels.append(int(cols.pop(0)))      # 첫번째 자리가 label
            images.append(list(map(lambda b: int(b) / 256, cols)))  # 실수 벡터화
    return {"labels": labels, "images": images}


test = readCsv('./data/t10k.csv', 10000)

# print(test['images'])
pklFile = "./data/mnist.pkl"
clf = None
if Path(pklFile).exists():              # from pathlib import Path
    print("File Exists!!")
    clf = joblib.load(pklFile)
# # training ---------------------------
if not clf:
    train = readCsv('./data/train.csv', 60000)   # 학습용 데이터가 많아질수록 스코어 상승!
    clf = svm.SVC(gamma='auto')
    clf.fit(train['images'], train['labels'])
    joblib.dump(clf, pklFile)

# test -------------------------
pred = clf.predict(test['images'])
print(pred)

score = metrics.accuracy_score(test['labels'], pred)
print("\n\nscore=", score)

print("-----------------------------------------")
report = metrics.classification_report(test['labels'], pred)
print(report)