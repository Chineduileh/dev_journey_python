from student_utils import average, assign_grade

scores = [89, 43, 65, 44]
avg = average(scores)
print(avg)

grades = [assign_grade(score) for score in scores]
print(grades)