# Step 1: Open a file called 'student_data.csv' to read each student's grades.
# hint: skip the header row with data[1:]
# hint: you could handle file errors with try/except

# Step 2: Read each student's grades and calculate their average grade
# hint: CSV data comes as strings, convert grade columns to int() for maths
# hint: student_data.csv has columns: ID, Name, Mathematics, Science, History
# hint: average = (maths + science + history) / 3

# Step 3: Sort the students by their average grade in descending order.
# hint: you might want to store each student as a dictionary with name and average
# hint: use the sorted() function with a key parameter, or list.sort()

# Step 4: Open a file called 'report.txt'
# Write each student's name and their average grade to the report in order
# hint: use 'w' mode to create a fresh report each time
# hint: format averages nicely, maybe to 2 decimal places with :.2f
with open('student_data', 'r') as infile:
    next (infile)
    for line in infile:
        data=[line.strip().split(',')for line in data]
        id, name, mathematics, science, history = data[0], data[1], int(data[2]), int(data[3]), int(data[4])
        average = (mathematics + science + history) / 3
    print({'name': name, 'average': average})
    sorted_students=sorted(name, key=lambda x: x['average'], reverse=True)
    with open('report.txt', 'w') as outfile:
        for student in sorted_students:
            outfile.write(f"{student['name']}: {student['average']:.2f}\n")
        