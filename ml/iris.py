from sklearn import svm, metrics
import pandas as pd
from sklearn.model_selection import train_test_split

csv = pd.read_csv('./data/iris.csv')
cdata = csv[['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth']]
cret = csv['Name']
trainData, testData, trainLabel, testLabel = train_test_split(cdata, cret)
print(trainLabel)

clf = svm.SVC(gamma='auto')  
clf.fit(trainData, trainLabel) #학습


pred = clf.predict(testData)    #검증
score = metrics.accuracy_score(testLabel, pred) #점수
print(score)