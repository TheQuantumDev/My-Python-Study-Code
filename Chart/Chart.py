import matplotlib.pyplot as plt

student_names = ["Reodesu", "Steve", "Dori", "Nano", "CJ", "Emma", "D-Boy", "Fiona"]
student_marks = [70, 69, 69, 63, 59, 46, 65, 10]
marks_perc = []

for x in student_marks:
    res = (x / 50) * 100
    marks_perc.append(res)
print(marks_perc)

#Lines chart
plt.plot(student_names, student_marks)
plt.title("Students Grading")
plt.xlabel("Students Names")
plt.ylabel("Students Marks")
plt.show()

#Bar Chart
plt.bar(student_names, marks_perc)
plt.title("Students Grading")
plt.xlabel("Students Names")
plt.ylabel("Students Marks")
plt.show()