import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

pkl_files = [f for f in os.listdir("setup_columns_extracted_data")]

for pkl_file in pkl_files:
    setup_df = pd.read_pickle("setup_columns_extracted_data/" + pkl_file)
    setup_df.set_index("id", inplace = True)
    # print(setup_df)

    le = LabelEncoder()
    le.fit(setup_df["failed_test_mnemonics"])
    setup_df["failed_test_mnemonics_encoded"] = le.transform(setup_df["failed_test_mnemonics"])

    le2 = LabelEncoder()
    le2.fit(setup_df["mnemonic"])
    setup_df["mnemonic_encoded"] = le2.transform(setup_df["mnemonic"])

    setup_df.to_pickle("setup_data_column_encoded/" + pkl_file.split(".")[0]+".pkl")

    # print(setup_df)



