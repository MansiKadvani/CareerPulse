import pandas as pd
import numpy as np

def predict_salary(df) :

    score = df['Placement_Score']
    
    df["Salary_Range"] = np.where(df["Placement_Score"] >= 85, "10-18 LPA", np.where(df["Placement_Score"] >= 70, "6-10 LPA",np.where(df["Placement_Score"] >= 50, "3-6 LPA","less than 3 LPA")))

    return df