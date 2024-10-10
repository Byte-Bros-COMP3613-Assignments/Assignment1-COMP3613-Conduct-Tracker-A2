from App.models import Review
from App.controllers.student import (get_student)
from App.database import db

def add_review(student_id, comment, is_positive):
    new_review = Review(student_id=student_id, comment=comment, is_positive=is_positive)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def get_reviews_for_student(student_id):
    student = get_student(student_id)
    if student:
        return student.reviews
    return []

def add_review_command_controller(student_id, comment, is_positive):
    review = add_review(student_id, comment, is_positive)
    print(f'Review added: {review.get_json()}')

def get_reviews_command_controller(student_id):
    reviews = get_reviews_for_student(student_id)
    for review in reviews:
        print(review.get_json())