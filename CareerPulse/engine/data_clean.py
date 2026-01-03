import pandas as pd 
import numpy as np

def clean_data(df) :

    #First understanding dataset
    # print(df.info())

    #replacing missing values in number columns with columns average
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = df[col].fillna(df[col].mean())

    #replacing missing values in text columns with most common value 
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna("Unknown")

    #converting negative values with positive ones 
    for col in df.select_dtypes(include=np.number).columns:
        df[col] = abs(df[col])
    
    return df