import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import ShuffleSplit
import os


pkl_files = [f for f in os.listdir("setup_data_column_encoded")]
accuracy_list = []
setup_list = []

for pkl_file in pkl_files:
    setup_df = pd.read_pickle("setup_data_column_encoded/"+pkl_file)
    if setup_df.shape[0] > 45:

        labels = setup_df["fr"]
        data = setup_df[["failed_test_mnemonics_encoded", "mnemonic_encoded"]]
        clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
        cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=42)
        scores = cross_val_score(clf, data, labels, cv=cv)
        print(scores.mean(), setup_df.shape[0], pkl_file)
        # print(scores, setup_df.shape[0], pkl_file)
        setup_list.append(pkl_file.split(".")[0])
        accuracy_list.append(scores.mean())
        result_df = pd.DataFrame({"setup" : setup_list, "svc_accuracy" : accuracy_list})
        result_df.to_csv("results/" + "svc_results.csv")
        
    
    else:
        continue