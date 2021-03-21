from sklearn import svm, metrics
import tkinter as tk
import pandas as pd
import numpy as np
import sklearn

def svm_gui(window, filename, delimiter, predict):
    special_delimiters = {
        "space": " ",
        "tab": "\t",
        "tab2": "\t\t",
        "semicolon": ";",
        "comma": ",",
        "pipe": "|",
        "colon": ":"
    }
    for key, value in special_delimiters.items():
        if key == delimiter:
            delimiter = value
    data = pd.read_csv(filename, sep=delimiter)

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    clf = svm.SVC(kernel="rbf", C=100)
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}/1.0\nPredictions: {y_pred}\n")
    print(f"Average Temperature: {np.mean(y_pred)}")
    tk.Label(window, text=f"Accuracy: {accuracy}/1.0\nPredictions: {y_pred}\nAverage Temperature: {np.mean(y_pred)}", bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=9, column=0, sticky=tk.W)