import csv
from typing import Union
import json
from pathlib import Path

def save_students(filename:str, students:list[dict])-> None:
    """
    Save a list of student dictionaries to a CSV file.

    Args:
        filename: Path to the output CSV file.
        students: List of dicts with keys name, subject, score.

    Returns:
        None
    """

    header=['name', 'subject', 'score']
    with open(filename, 'w', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(students)


def load_students(filename: str)-> Union[list[dict], None]:
    """
    Load student records from a CSV file.

    Args:
        filename: Path to the CSV file.

    Returns:
        List of student dicts, or None if file not found.
    """    

    try:
        with open(filename, 'r', encoding='UTF-8') as f:
            reader=csv.DictReader(f)
            students=list(reader)
    except FileNotFoundError:
        print(f'The file {filename} does not exist')
        return None
    else:
        for student in students:
            student['score']=int(student['score'])
        return students


def get_top_students(students: list[dict], threshold: int =70)-> list[dict]:
    """
    Filter students whose score meets or exceeds the threshold.

    Args:
        students: List of student dicts.
        threshold: Minimum score to be considered top. Defaults to 70.

    Returns:
        Filtered list of top student dicts.
    """ 
 
    top_students=[]
    for entry in students:
        if entry['score']>=threshold:
            top_students.append(entry)
    return top_students


def summarise_by_subject(students: list[dict]) -> dict:
    """
    Calculate average score per subject.

    Args:
        students: List of student dicts.

    Returns:
        Dictionary mapping subject names to average scores.
    """

    get_subjects=set()
    for entry in students:
        get_subjects.add(entry['subject'])
    subjects=list(get_subjects)
    subject_average_dict={}
    for subject in subjects:
        target_subject=subject
        subject_scores=[entry['score'] for entry in students if entry.get('subject')==subject]
        subject_average=sum(subject_scores)/len(subject_scores)
        subject_average_dict[subject]=subject_average

    return subject_average_dict


students = [
    {"name": "Chinedu", "subject": "Maths", "score": 85},
    {"name": "Ada", "subject": "Maths", "score": 62},
    {"name": "Obi", "subject": "English", "score": 74},
    {"name": "Kalu", "subject": "English", "score": 45},
    {"name": "Zara", "subject": "Science", "score": 91},
    {"name": "Emeka", "subject": "Science", "score": 55},
]

save_students("students.csv", students)
loaded = load_students("students.csv")
top = get_top_students(loaded)
summary = summarise_by_subject(loaded)

print("Top students:", top)
print("Subject summary:", summary)


def load_config(filename: str) -> dict:
    """
    Load config from a JSON file. Returns default config if file doesn't exist.

    Args:
        filename: Path to the JSON config file.

    Returns:
        Config dictionary.
    """
    path = Path(filename)
    if path.exists():
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {
            'theme': 'dark',
            'language': 'eng',
            'notifications': 'enabled',
            'version': 'v4'
        }


def save_config(filename: str, config: dict) -> None:
    """
    Save a config dictionary to a JSON file.

    Args:
        filename: Path to the output JSON file.
        config: Dictionary to save.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=4)


def update_config(filename: str, **updates) -> dict:
    """
    Load existing config, apply updates, save and return updated config.

    Args:
        filename: Path to the JSON config file.
        **updates: Key-value pairs to update in the config.

    Returns:
        The updated config dictionary.
    """
    existing = load_config(filename)
    existing.update(updates)
    save_config(filename, existing)
    return existing


# Test calls
config = load_config("config.json")
print("Initial config:", config)
save_config("config.json", config)

updated1 = update_config("config.json", theme="light")
print("After theme update:", updated1)

updated2 = update_config("config.json", language="fr", notifications="disabled")
print("After language and notifications update:", updated2)