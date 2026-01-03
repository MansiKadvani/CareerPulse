import pandas as pd
import numpy as np

def data_normalize(df) :

    #geting columns name
    # print(df.columns)

    df['cgpa_score'] = df['CGPA'] / 10
    df['intership_score'] = df['Internships'] / df['Internships'].max()
    df['project_score'] = df['Projects'] / df['Projects'].max()
    df['certi_score'] = df['Workshops/Certifications'] / df['Workshops/Certifications'].max()
    df['aptitude_score'] = df['AptitudeTestScore'] / 100
    df['softskills_score'] = df['SoftSkillsRating'] / 10 

    return df
