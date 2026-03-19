from typing import Any, Optional
import datetime

##A function that takes name and city as parameters
def introduce(name,city):
    print(f"My name is {name}, and I'm from {city}")


introduce("Ada", "Lagos")
introduce("Obi", "Ibadan")
introduce("Kalu", "Panya")


#A function to show today's date. No parameter
def showdate():
    print(datetime.date.today())


showdate()


## A function that repeats a word a specified number of times
def repeat_word(word, times):
    for i in range(times):
        print(word)

repeat_word("Sick", 4)
repeat_word("Table", 2)

## A function for multiplying and returning result
def multiply(a,b):
    return a*b


multiply_result=multiply(3,5)
print(multiply_result)


##A function to check if number is even
def is_even(number):
    return number%2==0

Test_number_list=[2,3,4,6]
for i in Test_number_list:
    check_even=is_even(i)
    print(check_even)


## Function to get initials
def get_initials(first_name, last_name):
    first_initial=first_name[0]
    second_initial=last_name[0]
    return first_initial.upper(), second_initial.upper()


initials=get_initials("Chinedu", "Ileh")
print(f"{initials[0]}.{initials[1]}")


#Function for bad_add
def bad_add(a,b):
    print(a+b)


result=bad_add(3,4)
print(result)


def generate_report(student_name: str, subject: str, passing_score: int = 50, **scores:Any) -> dict:
    """
    Generate student report for a given subject.

    Args:
        student_name: The name of the student
        subject: The subject in focus
        passing_score: The benchmark for passing, defaults to 50
        **scores: The scores from different tests on the subject.
    

    Returns:
        A matching dictionary for the details calculated for the student.
    """
    
    passed=True
    average=sum(scores.values())/len(scores.values())
    if average<passing_score:
        passed=False
    highest=sorted(scores.values())[-1]
    lowest=sorted(scores.values())[0]
    return_dict={
        "student":student_name,
         "subject":subject,
         "average":average,
         "passed":passed,
         "highest":highest, 
         "lowest":lowest
    }
    return return_dict

chinedu_maths_report=generate_report("Chinedu", "Mathematics", test1=77, test2=80, test3=60)
chinedu_chem_report=generate_report("Chinedu", "Chemistry", 70, test1=77, test2=80, test3=60)
ada_maths_report=generate_report("Ada", "Mathematics", test1=27, test2=80, test3=60)

print(chinedu_maths_report)
print(chinedu_chem_report)
print(ada_maths_report)


def format_data(*items: Any, **options: Any) -> str:

    """
        Function that takes in any number of strings, formats them based on specified or default options and prints

        Args:
            *items: The strings for the formating to be done on
            **options: The formatting requirements. Defaults to , as separator.

        Returns:
            A clean Formatted string 
    
    
    """

    separator = options.get("separator", ", ")
    uppercase = options.get("uppercase", False)
    prefix = options.get("prefix", "")

    processed_items = []
    for item in items:
        item = str(item)
        if uppercase:
            item = item.upper()
        if prefix:
            item = prefix+item
        processed_items.append(item)

    return separator.join(processed_items)

languages = ["Python", "JavaScript", "Go", "R", "FastAPI", "SQL"]
sorted_list = sorted(languages, key=lambda item: len(item))
formatted_result = format_data(*sorted_list, separator=" | ", uppercase=True, prefix="Lang: ")
print(formatted_result)


def summarise(*words:Any)-> str:
    joined="-".join(words)
    return joined

build_tag("Hello", tag="h1", class_name="title", id="main")
# returns: '<h1 class_name="title" id="main">Hello</h1>'
def build_tag(message: str,tag: str ="p",**html: Any)->str:
    unpack_html=[]
    for key,value in html:
        attribute=f'{key}={value}'
        unpack_html.append(attibute)

    return f'<{tag} {" ".join(unpack_html)}>{message}</{tag}>'


