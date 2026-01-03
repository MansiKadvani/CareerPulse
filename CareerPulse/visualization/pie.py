import matplotlib.pyplot as plt
import pandas as pd

def weak_skill_distribution(df):

    #store weak skill values in the all skill list
    all_skils = []
    for s in df['weak_skills'] :
        all_skils += s.split()
    
    '''
    These two lists will store:
        • unique skill names
        • how many times each skill occurs
    '''
    skills , counts = [] , []
    for i in all_skils :
        if i not in skills :
            skills.append(i)
            counts.append(all_skils.count(i))
    
    plt.figure()
    plt.pie(counts,labels=skills,autopct='%1.1f%%',colors = ["lightskyblue", "lightcoral", "lightgreen", "plum", "wheat"])
    plt.title("Weak Skill Distribution")
    plt.tight_layout()
    # plt.show()
    plt.savefig(r'D:\Projects\CareerPulse\reports\weak_skill_pie.png')
    plt.close()