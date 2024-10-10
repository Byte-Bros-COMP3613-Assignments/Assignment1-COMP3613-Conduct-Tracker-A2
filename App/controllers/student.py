from App.models import Student
from App.database import db

def add_student(name):
    new_student = Student(name=name)
    db.session.add(new_student)
    db.session.commit()
    return new_student

def get_student_by_name(name):
    return Student.query.filter_by(name=name).first()

def get_student(student_id):
    return Student.query.get(student_id)

def get_all_students():
    return Student.query.all()

def add_student_command_controller(name):
    student = add_student(name)
    print(f'Student {student.name} added!')

def get_student_command_controller(name):
    student = get_student_by_name(name)
    if student:
        print(student.get_json())
    else:
        print(f'Student {name} not found.')

def list_students_command_controller():
    students = get_all_students()
    for student in students:
        print(student.get_json())