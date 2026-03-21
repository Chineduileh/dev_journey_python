##NUMBER GUESSING GAME USING CONTROL FLOW CONCEPTS.
import random
Target_number= random.randint(1,11) #Get random number for as guess target.
Number_of_Trials=3
correct=False

for i in range(Number_of_Trials):
    try:
        player_input=int(input("Type your guess number "+str(i+1) + " "))
    except ValueError:
        print("Input must be an integer.")
        continue 
    if player_input<Target_number:
        print("Higher")
    elif player_input>Target_number:
        print("Lower")
    else:
        print("You're a genius, Congratulations")
        correct=True
        break
try:
    if correct==True:
        pass
    else:
        print("Sorry you have exhausted your trials")
except NameError:
    print("You didn't enter any valid input")

finally:
    print("Thank You for Playing")


def analyze_grades(records: list[dict]) -> dict:
    """
    Analyse student grades and return a summary.

    Args:
        records: List of dicts with name, subject, and score keys.

    Returns:
        Dictionary with total, passed, failed, grade_map, and failed_students.
    """
    total_count = len(records)
    student_grade_map = {}

    for i, student in enumerate(records):
        score = student['score']
        match score:
            case s if s >= 90:
                grade = 'A'
            case s if s >= 80:
                grade = 'B'
            case s if s >= 70:
                grade = 'C'
            case s if s >= 60:
                grade = 'D'
            case _:
                grade = 'F'

        student_grade_map[student['name']] = grade

    failed_students = [student for student in records if student_grade_map[student['name']] == 'F']
    failed_count = len(failed_students)
    passed_count = total_count - failed_count

    return {
        'total': total_count,
        'passed': passed_count,
        'failed': failed_count,
        'grade_map': student_grade_map,
        'failed_students': failed_students
    }


students = [
    {"name": "Chinedu", "subject": "Maths", "score": 85},
    {"name": "Ada", "subject": "English", "score": 92},
    {"name": "Obi", "subject": "Science", "score": 73},
    {"name": "Kalu", "subject": "Maths", "score": 55},
    {"name": "Zara", "subject": "English", "score": 67},
    {"name": "Emeka", "subject": "Science", "score": 41},
]

result = analyze_grades(students)
print(result)

def process_numbers(numbers: list) -> dict:
    """
    Process a list of numbers, categorising each by digit length.

    Args:
        numbers: List of integers to process.

    Returns:
        Dictionary with skipped count, early stop flag, and category counts.
    """
    stopped_processing_early = False
    skipped_numbers = 0
    digit_category_map = {
        'single digit': 0,
        'double digit': 0,
        'triple digit': 0,
        'large': 0
    }

    while numbers:
        num = numbers.pop(0)

        if num < 0:
            skipped_numbers += 1
            continue

        if num == 0:
            stopped_processing_early = True
            break

        digit = len(str(num))

        match digit:
            case 1:
                digit_size = 'single digit'
            case 2:
                digit_size = 'double digit'
            case 3:
                digit_size = 'triple digit'
            case _:
                digit_size = 'large'

        digit_category_map[digit_size] += 1

    return {
        'skipped': skipped_numbers,
        'stopped_early': stopped_processing_early,
        'category_counts': digit_category_map
    }


test_numbers = [5, -3, 150, 0, 42, 7, -1, 1200, 88]
result = process_numbers(test_numbers)
print(result)
        
            