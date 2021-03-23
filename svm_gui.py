from sklearn import svm, metrics
import tkinter as tk
import pandas as pd
import numpy as np
import sklearn
 
def svm_gui(window: tk.Tk, filename: str, delimiter: str, predict: str, output_label: tk.Label):
    special_delimiters = {
        "space": " ",
        "tab": "\t",
        "tab2": "\t\t",
        "semicolon": ";",
        "comma": ",",
        "pipe": "|",
        "colon": ":"
    }
    window.geometry("650x650")
    for key, value in special_delimiters.items():
        if key == delimiter:
            delimiter = value
    if ".csv" in filename:
        pass
    else:
        filename += "".join(".csv")

    try:
        data = pd.read_csv(filename, sep=delimiter)
    except (FileNotFoundError) as e:
        output_label = tk.Label(window, text=f"{e}", bg="#161616", fg="#cc0000",
        font="none 12 bold").grid(row=10, column=0, sticky=tk.W)
    try:
        X = np.array(data.drop([predict], 1))
        y = np.array(data[predict])

        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

        clf = svm.SVC(kernel="rbf", C=100)
        clf.fit(x_train, y_train)

        y_pred = clf.predict(x_test)

        accuracy = metrics.accuracy_score(y_test, y_pred)

        print(f"Accuracy: {accuracy}/1.0\nPredictions: {y_pred}\n")
        print(f"Average Temperature: {np.mean(y_pred)}")

        output_label = tk.Label(window, text=f"Accuracy:\n{accuracy}/1.0\nPredictions: {y_pred}\nAverage Temperature: {np.mean(y_pred)}",
        bg="#161616", fg="#f7f7f7", font="none 12 bold").grid(row=10, column=0, sticky=tk.W)
    
    except (Exception, TypeError) as e:
        output_label = tk.Label(window, text=f"{e}", bg="#161616", fg="#cc0000",
        font="none 12 bold").grid(row=10, column=0, sticky=tk.W)