import matplotlib.pyplot as plt
import pandas as pd

def placement_trend(df) :
    sorted_df = df.sort_values(by="Placement_Score")
    top10 = sorted_df.head(10)
    plt.figure()
    plt.plot(top10.index,top10["Placement_Score"] ,color='#a00000' , linestyle='-' , linewidth=2 , marker='o' , label='placement trend' )
    plt.xlabel("Student Index (sorted)")
    plt.ylabel("Placement Score")
    plt.title("Placement Score Trend")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(r'D:\Projects\CareerPulse\reports\score_trend_line_plot.png')
    plt.close()