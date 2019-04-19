from sklearn import svm, metrics
import pandas as pd
from sklearn.externals import joblib
from pathlib import Path

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

#serialize할 파일 경로
pklFile = "./data/mnist.pkl"
clf = None

#피클 파일 존재 여부 파악
if Path(pklFile).exists():
    print("File Exists!!")
    clf = joblib.load(pklFile) #파일이 이미 존재하므로 clf 인스턴스를 새로 만들지 않고 desiralize
# # training ---------------------------
if not clf: #clf instance가 없다면 데이터를 읽어 새로운 clf instance를 생성
    train = readCsv('./data/train.csv', 60000)   # 학습용 데이터가 많아질수록 스코어 상승!
    clf = svm.SVC(gamma='auto')
    clf.fit(train['images'], train['labels'])
    joblib.dump(clf, pklFile) #clf instance를 serialize
    print("New file created")

