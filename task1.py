#Objective: Build a program to store and manage student academic data. 
Student_name = input("Enter the name of the student:")
Roll_no = input("Enter the student rollno:")
Subjects = input("Enter the name of the subjects:").split(",")
Unique_subjects = set(Subjects)

Subject_marks = {}
print("Enter marks for the each unique subjects:")
for subject in Unique_subjects:
    marks = float(input(f"Enter  marks for {subject}:"))
    Subject_marks[subject] = marks

print("\n -----STUDENT DATABASE-----")
print("Student_name:",Student_name)
print("\nRool_no:",Roll_no)
print("\nSubjects:",Subjects)
print("\nUnique_subjects:",Unique_subjects)
print("\nSubmit-wise marks:")
for subject,marks in Subject_marks.items():
    print(f"{subject}: {marks}")