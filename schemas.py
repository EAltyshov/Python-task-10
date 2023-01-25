import os, os.path
from fastapi import UploadFile
import pandas as pd
os.environ["DATA_DIR"] = 'C:\\Users\\EAltyshov\\PycharmProjects\\Python-task-10'


def accum_files(files: list[UploadFile], result_filename: str):
    li = []
    for file in files:
        if file.filename.endswith(".csv"):
            df = pd.read_csv(file.file, sep=';')
            li.append(df)
        elif file.filename.endswith(".json"):
            df = pd.read_json(file.file)
            li.append(df)
    concat_df = pd.concat(li, ignore_index=True)

    path = os.path.join('data/', result_filename)
    if os.path.isfile(path):
        with open(path, "r") as original_file:
            original_df = pd.read_csv(original_file, sep=';')
            concat_df = pd.concat([original_df, concat_df], ignore_index=True)

    concat_df.to_csv(os.path.join('data/', result_filename), sep=';', index=False)