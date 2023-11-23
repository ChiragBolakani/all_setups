import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import os

accuracy_list = []
setup_list = []

pkl_files = [f for f in os.listdir("setup_data_column_encoded")]

for pkl_file in pkl_files:
    setup_df = pd.read_pickle("setup_data_column_encoded/"+pkl_file)
    if setup_df.shape[0] > 40:

        labels = setup_df["fr"]
        data = setup_df[["failed_test_mnemonics_encoded", "mnemonic_encoded"]]
        knn = KNeighborsClassifier(n_neighbors=5)
        cv = ShuffleSplit(n_splits=5, test_size=0.20, random_state=42)
        scores = cross_val_score(knn, data, labels, cv=cv)
        print(scores.mean(), setup_df.shape[0], pkl_file)

        accuracy_list.append(scores.mean())
        setup_list.append(pkl_file.split(".")[0])
        result_df = pd.DataFrame({"setup" : setup_list, "knn_accuracy" : accuracy_list})
        result_df.to_csv("results/" + "knn_results.csv")
    
    else:
        continue