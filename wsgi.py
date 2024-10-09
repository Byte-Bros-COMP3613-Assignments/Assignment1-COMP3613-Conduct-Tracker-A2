import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.controllers.student import (
    add_student, get_student_by_name, get_student, get_all_students, add_review, get_reviews_for_student
)
from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_user, get_all_users_json, get_all_users, initialize )
from flask_migrate import Migrate
from App.database import db


#comment
# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# Student commands
student_cli = AppGroup('student', help='Student management commands')

@student_cli.command('add', help='Add a new student')
@click.argument('name')
def add_student_command(name):
    student = add_student(name)
    print(f'Student {student.name} added!')

@student_cli.command('get', help='Get a student by name')
@click.argument('name')
def get_student_command(name):
    student = get_student_by_name(name)
    if student:
        print(student.get_json())
    else:
        print(f'Student {name} not found.')

@student_cli.command('list', help='List all students')
def list_students_command():
    students = get_all_students()
    for student in students:
        print(student.get_json())

@student_cli.command('review', help='Add a review for a student')
@click.argument('student_id')
@click.argument('comment')
@click.argument('is_positive', type=bool)
def add_review_command(student_id, comment, is_positive):
    review = add_review(student_id, comment, is_positive)
    print(f'Review added: {review.get_json()}')

@student_cli.command('reviews', help='View reviews for a student')
@click.argument('student_id')
def get_reviews_command(student_id):
    reviews = get_reviews_for_student(student_id)
    for review in reviews:
        print(review.get_json())


# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("username", default="rob")
@click.argument("password", default="robpass")
def create_user_command(username, password):
    create_user(username, password)
    print(f'{username} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())

app.cli.add_command(user_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)
app.cli.add_command(student_cli)
