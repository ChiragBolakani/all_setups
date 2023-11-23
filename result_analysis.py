import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from functools import reduce

result_files = [f for f in os.listdir("results")]
result_files_data_frames = []

for result_file in result_files:
    result_file_df = pd.read_csv("results/" + result_file)
    result_files_data_frames.append(result_file_df)

df_merged = reduce(lambda  left,right: pd.merge(left,right,on=['setup'],how='outer'), result_files_data_frames)
# df_merged = pd.concat(result_files_data_frames)
print(df_merged)

barWidth = 0.25
X = [setup for setup in df_merged["setup"]]

setups = {
    "knn" : df_merged["knn_accuracy"],
    "dct" : df_merged["dct_accuracy"],
    "svc" : df_merged["svc_accuracy"]
}

# knn = df_merged["knn_accuracy"]
# dct = df_merged["dct_accuracy"]
# svc = df_merged["svc_accuracy"]

width = 0.25
multiplier = 0
x = np.arange(len(X)) 

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in setups.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# plt.bar(x+1, knn, 0.4, label = 'knn') 
# plt.bar(x+1, svc, 0.4, label = 'svc')
# plt.bar(x+1, dct, 0.4, label = 'dct')


ax.set_ylabel('accuracy')
ax.set_title('comparision of accuracy')
ax.set_xticks(x + width, X)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 1.2)
plt.show()

