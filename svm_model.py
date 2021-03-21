from sklearn import svm, metrics
import pandas as pd
import numpy as np
import sklearn
import sys
import os

def main():
    special_delimiters = {
        "space": " ",
        "tab": "\t",
        "tab2": "\t\t",
        "semicolon": ";",
        "comma": ",",
        "pipe": "|",
        "colon": ":"
    }

    # Command line arguments are decent now and should be used
    for i in range(2, 5):
        if len(sys.argv) - 1 == 1:
            if sys.argv[1] == "-help":
                print("""python3 svm_model.py -args [file name] [delimiter] [y column]if you're on Linux or MacOS and 
                python svm_model.py -args [file name] [delimiter] [y column] if you're on Windows""")
                exit()
        elif len(sys.argv) < 3:
            print("No arguments supplied, will use the input function")
            file_name = str(input("What's the name of the file that contains the temperature data of your micro:bit?\n"))
            delimiter = str(input("What's the delimiter that is used?\n"))
            predict = str(input("Name of the y column?\n"))
            break
        elif sys.argv[1] == "-args":
            file_name = sys.argv[2]
            delimiter = sys.argv[3]
            predict = sys.argv[4]
            for key, value in special_delimiters.items():
                if key == delimiter:
                    delimiter = value
        else:
            continue

    data = pd.read_csv(file_name, sep=delimiter)

    X = np.array(data.drop([predict], 1))
    y = np.array(data[predict])

    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    clf = svm.SVC(kernel="rbf", C=100)
    clf.fit(x_train, y_train)

    y_pred = clf.predict(x_test)

    accuracy = metrics.accuracy_score(y_test, y_pred)

    print(f"Accuracy: {accuracy}/1.0\nPredictions: {y_pred}")
    print(f"Average Temperature: {np.mean(y_pred)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        try:
            sys.exit(1)
        except SystemExit:
            os._exit(1)