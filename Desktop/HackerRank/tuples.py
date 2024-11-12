# Read input values
n, x = map(int, input().split())

# Read each subject's marks and store them in a list
marks = [list(map(float, input().split())) for _ in range(x)]

# Transpose the list to group marks by student
# Each tuple in students represents the marks of a single student in all subjects
students = zip(*marks)

# Calculate and print the average for each student
for student in students:
    average = sum(student) / x
    print(f"{average:.1f}")
