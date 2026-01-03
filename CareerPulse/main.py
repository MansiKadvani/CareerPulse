#cleaning and predicting import
from engine.data_load import load_dataset
from engine.data_clean import clean_data
from engine.normalize import data_normalize
from engine.scores import calulate_placement_score
from engine.salary_predict import predict_salary
from engine.weak_skill import detect_weak_skill

#visualization import
from visualization.histogram import placement_score
from visualization.bar import top_students_placement
from visualization.pie import weak_skill_distribution
from visualization.line import placement_trend
from visualization.scatter import multi_scatter
from visualization.dashboard import dashboard

#width for centering
width = 80

#calling load dataset function
print(f"{'-'*width}\n{'Original Dataset':^{width}}\n{'-'*width}")
path = r"D:\Projects\CareerPulse\dataset\placementdata.csv"
df = load_dataset(path)
print("\n",df)

#callling function for cleaning the data
df = clean_data(df)
print(f"\n{'-'*width}\n{'Dataset After Cleaning(Displaying Only 5)':^{width}}\n{'-'*width}")
print("\n",df.head())

#calling function for normalizing data
df = data_normalize(df)
print(f"\n{'-'*width}\n{'Dataset After Normalizing Some Columns Values(Displaying Only 5)':^{width}}\n{'-'*width}")
print("\n",df.head())

#calling function for caluclate placement score
df = calulate_placement_score(df)
print(f"\n{'-'*width}\n{'Placement Score Of Students(Displaying Only 5)':^{width}}\n{'-'*width}")
print("\n",df[['StudentID','Placement_Score']].head())

#calling function for predicting salary 
df = predict_salary(df)
print(f"\n{'-'*width}\n{'Predicted Salary Based On Placement Score Of Students(Displaying Only 5)':^{width}}\n{'-'*width}")
print("\n",df[['StudentID','Placement_Score','Salary_Range']].head())

#calling function for detecting students weak point
df = detect_weak_skill(df)
print(f"\n{'-'*width}\n{'Weak Points Of Students(Displaying Only 5)':^{width}}\n{'-'*width}")
print('\n',df[['StudentID',"Placement_Score","Salary_Range","weak_skills"]].head())

#histogram for placement score distribution
placement_score(df)
print(f"{'-'*width}\n{'Histogram Saved Successfully':^{width}}\n{'-'*width}")

#bar chart for Top 10 Students Ranking
top_students_placement(df)
print(f"{'-'*width}\n{'Bar Chart Saved Successfully':^{width}}\n{'-'*width}")

#pie chart for weak skill distribution
weak_skill_distribution(df)
print(f"{'-'*width}\n{'Pie Chart Saved Successfully':^{width}}\n{'-'*width}")

#scatter diagram for Placement score vs Salary & Intership vs Salary
multi_scatter(df)
print(f"{'-'*width}\n{'Scatter Diagram Saved Successfully':^{width}}\n{'-'*width}")

#line chart for placement score trend
placement_trend(df)
print(f"{'-'*width}\n{'Line Chart Saved Successfully':^{width}}\n{'-'*width}")

#final dashboard 
dashboard()
print(f"{'-'*width}\n{'Dashboard Saved Successfully':^{width}}\n{'-'*width}")
