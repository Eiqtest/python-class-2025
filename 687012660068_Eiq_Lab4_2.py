import random

subject_keys = ["Eng", "Programming", "Networking", "Math"]
students = {}

for i in range(1, 51):
    student_id = f"S{i:03d}"
    
    scores = {key: random.randint(0, 100) for key in subject_keys}
    total = sum(scores.values())
    avg = total / 4
    gpa = round(avg / 25,2)
 
    grades = {}
    for key in subject_keys:
        score = scores[key]
        if score >= 80:
            grades[key] = 'A'
        elif score >= 70:
            grades[key] = 'B'
        elif score >= 60:
            grades[key] = 'C'
        elif score >= 50:
            grades[key] = 'D'
        else:
            grades[key] = 'F'
    students[student_id] = {
        **grades,
        "Sum": round(gpa, 4)  
    }

import pprint
pprint.pprint(students)