from os import sep
from sklearn import svm, metrics
import pandas as pd
import numpy as np
import sklearn
import sys

special_delimiters = {
    "space": " ",
    "tab": "\t",
    "tab2": "\t\t"
}
# Command line arguments are experimental and not complete yet. They mostly don't work
# and shouldn't be used until they're decent
for i in range(2, 5):
    if len(sys.argv) < 3:
        print("No arguments supplied, will use the input function")
        file_name = str(input("What's the name of the file that contains the temperature data of your micro:bit?\n"))
        delimiter = str(input("What's the delimiter of your file?\n"))
        predict = str(input("Name of the y column?\n"))
        break
    elif sys.argv[1] == "-args" and sys.argv[i] != None:
        print("Arguments will be used")
        file_name = sys.argv[2]
        delimiter = sys.argv[3]
        predict = sys.argv[4]
        for key, value in special_delimiters.items():
            if key == delimiter:
                delimiter = value
    else:
        continue

data = pd.read_csv(file_name, sep=delimiter, encoding="ascii")

X = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

clf = svm.SVC(kernel="rbf", C=100)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

accuracy = metrics.accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}/1.0\nPredictions: {y_pred}\n")
print(f"Average Temperature: {np.mean(y_pred)}")