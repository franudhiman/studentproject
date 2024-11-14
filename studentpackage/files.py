import json
import pandas as pd

def store_results(file_name, result_data):
    with open(file_name, "w") as file:
        file.write(result_data)

def import_details(file_name):
    with open(file_name, "r") as file:
        data = file.read()
        dd=json.loads(data)

        print(type(dd))
        return dd

def import_from_excel(file_name):
    df = pd.read_excel(file_name, sheet_name="data1")

    first_column_list = df.iloc[:, 0].tolist()

    second_column_list = df.iloc[:, 1].tolist()

    result= dict(zip(first_column_list,second_column_list))

    return result


def store_to_excel(file_name,result_data):
    #df = pd.DataFrame(result_data)

   # df.to_excel(file_name, index=False)
    df_nested = pd.DataFrame.from_dict(result_data, orient="index")

    # Write to Excel
    df_nested.to_excel(file_name)



