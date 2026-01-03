import pandas as pd
import numpy as np

def calulate_placement_score(df) :

    #accessing columns
    # print(df.columns)

    #Applying logic
    df['Placement_Score'] = (df['cgpa_score'] * 25) + (df['intership_score'] * 15) + (df['project_score'] * 10) + (df['certi_score'] * 10) + (df['aptitude_score'] * 25) + (df['softskills_score'] * 15)

    return df