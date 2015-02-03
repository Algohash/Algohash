'''
Author: Harisankar Namasivayam
This is simple python scripts calculates 
the student grades given their scores 
and the weightage for each scores
'''

#Student database using dictionaries
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

#list of students
students = [lloyd, alice, tyler]

# Getting the average of numbers
def average(numbers):
    total = sum(numbers)
    total = float(total)
    avg=total/len(numbers)
    return avg

'''
Getting weighted average of numbers
In this case the weighted average of students
'''
def get_average(student):
    hw=average(student["homework"])
    qz=average(student["quizzes"])
    ts=average(student["tests"])
    
    wt_avg=0.1*hw + 0.3*qz + 0.6*ts
    return wt_avg
    
#converting the score into letter grades
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
  

def get_class_average(students):
    results=[]
    for st in students:
        student_avg = get_average(st)
        results.append(student_avg)
    class_avg = average(results)   
    return class_avg

#Finally getting the grade of students.       
#print get_letter_grade(get_average(alice))

print get_class_average(students)
