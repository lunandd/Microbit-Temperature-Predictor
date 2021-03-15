import pandas as pd
import numpy as np
import sklearn
from sklearn import datasets, svm, metrics

data = pd.read_csv("temp-data.csv")

predict = "temp"

X = np.array(data.drop([predict], axis=1))
y = np.array(data[predict])
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

clf = svm.SVC(kernel="rbf", C=100)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)


acc = metrics.accuracy_score(y_test, y_pred)

print(f"Accuracy: {acc}/1.0\n Predictions: {y_pred}\n")

predictions_df = pd.DataFrame(data=y_pred.flatten())
predictions_df.plot(kind="kde")
