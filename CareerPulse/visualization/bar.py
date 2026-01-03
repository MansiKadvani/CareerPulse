import matplotlib.pyplot as plt
import pandas as pd

def top_students_placement(df):

    top10 = df.sort_values(by='Placement_Score',ascending=False).head(10)

    plt.figure()
    plt.bar(top10.index.astype(str),top10['Placement_Score'] , color='darkorange' , label="top 10 student")
    plt.title("Top 10 Students by Placement Score")
    plt.xlabel("Student Index")
    plt.ylabel("Placement Score")
    plt.legend()
    plt.ylim(85.5, 87) 
    plt.tight_layout()
    # plt.show()
    plt.savefig(r'D:\Projects\CareerPulse\reports\top_students_bar.png')
    plt.close()
    
