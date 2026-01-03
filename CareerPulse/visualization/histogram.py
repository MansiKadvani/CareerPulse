import matplotlib.pyplot as plt
import pandas as pd

def placement_score(df):

    plt.figure(figsize=(7,5))
    plt.hist(df['Placement_Score'], bins=5, color="#800074" , edgecolor='black')
    plt.title('Placement Score Distribution')
    plt.xlabel('Placement Chances')
    plt.ylabel('Number of Students')
    plt.xticks([45, 55, 65, 75, 85],['Very Low', 'Low', 'Medium', 'High', 'Very High'])
    plt.tight_layout()
    plt.savefig(r'D:\Projects\CareerPulse\reports\placement_score_histogram.png')
    plt.close()
