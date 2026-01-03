import matplotlib.pyplot as plt
import pandas as pd

def multi_scatter(df):

    salary_map = {
        "less than 3 LPA": 2,
        "3-6 LPA": 4.5,
        "6-10 LPA": 8,
        "10-18 LPA": 14
    }

    df["Salary_Num"] = df["Salary_Range"].map(salary_map)

    plt.figure()

    # Scatter 1: Placement Score vs Salary
    plt.scatter(df["Placement_Score"].head(25), df["Salary_Num"].head(25),
                marker='o', color="#5e4c5f", label="Placement Score vs Salary")

    # Scatter 2: Internships vs Salary (second different data)
    plt.scatter(df["Internships"].head(25), df["Salary_Num"].head(25),
                marker='+', color="#999999", label="Internships vs Salary")

    plt.xlabel("Score / Internship Count")
    plt.ylabel("Salary (LPA)")
    plt.title("Placement Score & Internships vs Salary")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.savefig(r"D:\Projects\CareerPulse\reports\multi_scatter_salary.png")
    plt.close()

