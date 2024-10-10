from .user import create_user
from .student import (add_student)
from .review import (add_review)
from App.database import db

def initialize():
    db.drop_all()
    db.create_all()
    #-------------------------------------------
    #Initial Values for testing purposes:
    #-------------------------------------------
    print ("Adding Testing Values to database.")
    create_user('bob', 'bobpass')
    add_student("Isaiah_Rambhajan")
    add_student("Javonte_Baldeo")
    add_student("Pranav_Soondar")
    add_student("Teal_Trim")
    add_review(1, "He's a good Student.", 1)
    add_review(2, "He's a great Student.", 1)
    add_review(3, "He's a bad Student.", 0)
    add_review(4, "He's a awful Student.", 0)
    print ("Testing values added to database.")
    #-------------------------------------------
