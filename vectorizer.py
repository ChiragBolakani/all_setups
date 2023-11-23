import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer

def vectorizeReason(reason):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([reason])
    return vectors.toarray()

pkl_files = [f for f in os.listdir("setup_columns_extracted_data_with_reason")]

for pkl_file in pkl_files:
    setup_df = pd.read_pickle("setup_columns_extracted_data_with_reason/" + pkl_file)
    setup_df.set_index("id", inplace = True)
    # print(setup_df)

    setup_df["reason_encoded"] = None

    for index, row in setup_df.iterrows():
        setup_df["reason_encoded"].loc[index] = vectorizeReason(row["failed_reasons"])[0]

    data = np.array(setup_df[["reason_encoded"]])
    data
    data_lens = []
    for encoded_reason in data:
        data_lens.append(len(encoded_reason[0]))

    padded_reason_encoded_temp = []
    for encoded_reason in data:
        padded_reason_encoded_temp.append(np.pad(encoded_reason[0], (0,max(data_lens)-len(encoded_reason[0])), constant_values=(0)))
        data_lens.append(len(encoded_reason[0]))

    padded_reason_encoded = np.array(padded_reason_encoded_temp)
    with open("setup_data_column_vectorized/" + pkl_file.split(".")[0] + ".npy", "wb") as f:
        np.save(f, padded_reason_encoded)
        f.close()

    # setup_df.to_pickle("setup_data_column_encoded/" + "encoded_" + pkl_file.split(".")[0]+".pkl")

    # print(setup_df)



