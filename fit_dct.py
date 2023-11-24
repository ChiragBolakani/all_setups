import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import os
import pickle

pkl_files = [f for f in os.listdir("setup_data_column_encoded")]
accuracy_list = []
setup_list = []

for pkl_file in pkl_files:
    setup_df = pd.read_pickle("setup_data_column_encoded/"+pkl_file)
    if setup_df.shape[0] > 45:

        labels = setup_df["fr"]
        data = setup_df[["failed_test_mnemonics_encoded", "mnemonic_encoded"]]
        clf = DecisionTreeClassifier(random_state=42)
        cv = ShuffleSplit(n_splits=10, test_size=0.20, random_state=42)
        scores = cross_val_score(clf, data, labels, cv=cv)
        print(scores.mean(), setup_df.shape[0], pkl_file)

        accuracy_list.append(scores.mean())
        setup_list.append(pkl_file.split(".")[0])
        result_df = pd.DataFrame({"setup" : setup_list, "dct_accuracy" : accuracy_list})
        result_df.to_csv("results/" + "dct_results.csv")
        #print(scores, setup_df.shape[0], pkl_file)

        with open("models/dct.pkl", "wb") as model_pickle_file:
            pickle.dump(clf, model_pickle_file)
            model_pickle_file.close()
        
    else:
        continue