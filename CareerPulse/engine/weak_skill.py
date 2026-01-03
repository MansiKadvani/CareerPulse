import pandas as pd
import numpy as np 

def detect_weak_skill(df) :

    weak = []

    #checking the weak skill
    for col in ['cgpa_score','intership_score' , 'project_score' , 'certi_score','aptitude_score','softskills_score'] :
        weak.append((col , df[col] < 0.6))

    #creting one column 
    df['weak_skills'] = ""
    for col , i in weak :
        df.loc[i,"weak_skills"] += col + " "

    return df 