import mysql.connector
import pandas as pd
import numpy as np

connection = mysql.connector.connect(user = "root", host = "localhost", password = "r@ndom06", database = "regression_db")

cursor = connection.cursor()

sql = '''select name from setup'''
cursor.execute(sql)

setups = []

for row in cursor.fetchall():
    setups.append(row[0])

setup_df = pd.DataFrame({"setups" : setups})
setup_df.to_csv("setup.csv")
connection.close()
