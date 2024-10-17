from App.models import Review
from App.controllers.student import (get_student)
from App.database import db

def add_review(student_id, comment, is_positive):
    new_review = Review(student_id=student_id, comment=comment, is_positive=is_positive)
    db.session.add(new_review)
    db.session.commit()
    return new_review

def update_review(review_id, student_id, comment, is_positive):
    review = Review.query.get(review_id)
    if review:
        review.student_id = student_id
        review.comment = comment
        review.is_positive = is_positive
        db.session.commit()
        return review
    return None  # Review not found


def delete_review(review_id):
    review = Review.query.get(review_id)
    if review:
        db.session.delete(review)
        db.session.commit()
        return True # Successfully deleted
    return False #Failed to delete


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
