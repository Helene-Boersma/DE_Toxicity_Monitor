import pandas as pd
from detoxify import Detoxify


def detoxify(x):
    results_prediction = Detoxify('original').predict(x)
    input_text="resultat"
    df = pd.DataFrame(results_prediction, index=[input_text]).round(4)

    # Converting df to list
    df_list = df.iloc[[0]].values.tolist()
    df_name_list = df.columns.tolist()
    list_value = df_list[0]
    for i in range(len(list_value)):
        list_value[i] = round(list_value[i],4)*100

    # Getting the result above 0.5 (threshold)
    if any(y >= 0.50 for y in list_value):
        resp = "In this sentence, there is "
        for i in range(len(list_value)):
            if list_value[i] >= 50:
                resp = resp + str(df_name_list[i]) + " " +  str(list_value[i]) + " , "
        return resp
    else:
        return "This sentence is not toxic"