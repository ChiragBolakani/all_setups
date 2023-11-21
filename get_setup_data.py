import mysql.connector
import pandas as pd
import numpy as np
import json
import pandas.io.sql

connection = mysql.connector.connect(user = "root", host = "localhost", password = "r@ndom06", database = "regression_db")
cursor = connection.cursor()

setup_df = pd.read_csv("setup.csv")
setups = setup_df["setups"].tolist()

for setup in setups:

    sql = '''SELECT 
    functional_test.id,
    functional_test.testrun_id,
    functional_test.comments,
    functional_test.result_per_step,
    functional_test.fr,
    functional_testcase.mnemonic
FROM
    functional_test
        INNER JOIN
    testrun ON functional_test.testrun_id = testrun.id
        INNER JOIN
    setup ON testrun.setup_id = setup.id
        INNER JOIN
    functional_testcase ON functional_testcase.id = functional_test.testcase_id
WHERE
    setup.name = %s
        AND testrun.date >= DATE('2022-08-01')
        AND LENGTH(functional_test.comments) != 0
        AND (functional_test.nb_steps_fail > 0
        OR functional_test.nb_steps_not_run > 0)
ORDER BY testrun.date DESC
'''
    val = (setup,)
    cursor.execute(sql,val)

    
    rows_json = [dict((cursor.description[i][0], value) \
               for i, value in enumerate(row)) for row in cursor.fetchall()]
    
    
    json_output = json.dumps(rows_json, default=str)
    print(type(json_output))
    with open("setup_data/"+setup+".json", "w") as jsonf:
        jsonf.write(json_output)


    # for row in records:
    #     print(row)

connection.close()
