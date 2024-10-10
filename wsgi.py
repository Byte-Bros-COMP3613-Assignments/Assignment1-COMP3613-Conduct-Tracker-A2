#-------------------------------------------
#Group Information:
#-------------------------------------------
#Group Name: Byte Bros
#Group Members: Isaiah Rambhajan, Javonte Baldeo, Pranav Soondar, Teal Trim
#-------------------------------------------
#Assignment Information:
#-------------------------------------------
#Course: Software Engineering II (COMP3613)
#Assignment: COMP3613 Assignment 2
#Date: 11/10/2024
#-------------------------------------------




#-------------------------------------------
#Import Statements:
#-------------------------------------------
import click
from flask import Flask
from flask.cli import with_appcontext, AppGroup
from App.database import db, get_migrate
from App.main import create_app
from App.controllers import (initialize)
from App.controllers.student import (add_student_command_controller, get_student_command_controller, list_students_command_controller)
from App.controllers.review import (add_review_command_controller, get_reviews_command_controller)

from flask_migrate import Migrate
from App.database import db
#-------------------------------------------




#-------------------------------------------
#Database Initialization:
#-------------------------------------------
app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    print('Intializing Database')
    initialize()
    print('Database Intialized')
#-------------------------------------------




#-------------------------------------------
#Student Commands:
#-------------------------------------------
student_cli = AppGroup('student', help='Student management commands')

@student_cli.command('add', help='Add a new student')
@click.argument('name')
def add_student_command(name):
    add_student_command_controller(name)

@student_cli.command('get', help='Get a student by name')
@click.argument('name')
def get_student_command(name):
    get_student_command_controller(name)

@student_cli.command('list', help='List all students')
def list_students_command():
    list_students_command_controller()

@student_cli.command('review', help='Add a review for a student')
@click.argument('student_id')
@click.argument('comment')
@click.argument('is_positive', type=bool)
def add_review_command(student_id, comment, is_positive):
    add_review_command_controller(student_id, comment, is_positive)


@student_cli.command('reviews', help='View reviews for a student')
@click.argument('student_id')
def get_reviews_command(student_id):
    get_reviews_command_controller(student_id)

app.cli.add_command(student_cli)
#-------------------------------------------
