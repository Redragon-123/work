import pandas

data = pandas.read_csv("lifestyle_data.csv")

# For each of the following pieces of information, try and use pandas to find the answer from the dataset in 'data'
# leave your code under the comments.

# Find the total number of students

# Find the mean average GPA of the students

# Find the standard deviation of how much sleep students get per day

# Find the maximum amount of study hours per day

# Sort the students by social hours per day ascending (lowest -> highest)

# Add a column 'Total_hours' which adds together all the Hours_Per_Day columns into one

# Filter all students with a 'high' stress level, and all the students with a 'low' stress level.
# Can you work out whether having a higher stress level leads to a higher GPA?
totle_students = data.shape[0]
print(f"Total number of students:{totle_students}")
mean_gpa=data["GPA"].mean()
print(f"Mean average of students:{mean_gpa}")
std_sleep=data["Sleep_Hours_Per_Day"].std()
print(f"Standard deviation of how much sleep students get per day:{std_sleep}")
max_study_hours=data["Study_Hours_Per_Day"].max()
sorted_social_hours=data.sort_valuse(by="Social_Hours_Per_Day",ascending=True)
data["Total_hours"]=data["Study_Hours_Per_Day"]+data["Extracurricular_Hours_Per_Day"]+data["Sleep_Hours_Per_Day"]+data["Social_Hours_Per_Day"]+data["Physical_Activity_Hours_Per_Day"]
high_stress=data[data["Stress_level"]=="high"]
low_stress=data[data["Stress_level"]=="low"]
high_stress_gpa=high_stress["GPA"].mean()
low_stress_gpa=low_stress["GPA"].mean()
if high_stress_gpa>low_stress_gpa:
    print("Having a higher stress level leads to a higher GPA")
elif high_stress_gpa<low_stress_gpa:
    print("Having a lower stress level leads to a higher GPA")
elif high_stress_gpa==low_stress_gpa:
    print("Stress level does not affect GPA")