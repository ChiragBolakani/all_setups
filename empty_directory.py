import os 
import shutil

shutil.rmtree("setup_columns_extracted_data")
os.mkdir("setup_columns_extracted_data")

shutil.rmtree("setup_data")
os.mkdir("setup_data")

shutil.rmtree("setup_data_column_encoded")
os.mkdir("setup_data_column_encoded")

shutil.rmtree("setup_json_data")
os.mkdir("setup_json_data")