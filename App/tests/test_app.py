import os, tempfile, pytest, logging, unittest
from werkzeug.security import check_password_hash, generate_password_hash

from App.main import create_app
from App.database import db, create_db
from App.models import User, Student, Review
from App.controllers import (
    create_user,
    get_all_users_json,
    login,
    get_user,
    get_user_by_username,
    update_user,
    add_student,
    add_review,
    update_review,
    delete_review,
    get_student_by_name,
    get_reviews_for_student
)


LOGGER = logging.getLogger(__name__)

'''
   Unit Tests
'''
class UnitTests(unittest.TestCase):

    def test_new_user(self):
        newUser = User("bob", "bobpass")
        assert newUser.username == "bob"

    # pure function no side effects or integrations called
    def test_user_get_json(self):
        newUser = User("bob", "bobpass")
        user_json = newUser.get_json()
        self.assertDictEqual(user_json, {"id": None, "username": "bob"})
    
    def test_hashed_password(self):
        password = "mypass"
        hashed = generate_password_hash(password, method='sha256')
        newUser = User("bob", password)
        assert newUser.password != password

    def test_check_password(self):
        password = "mypass"
        newUser = User("bob", password)
        assert newUser.check_password(password)

    def test_new_student(self):
        newStudent = Student("John Doe")
        assert newStudent.id == None
        assert newStudent.name == "John Doe"

    def test_student_get_json(self):
        newStudent = Student("John Doe")
        student_json = newStudent.get_json()
        self.assertDictEqual(student_json, {"id": None, "name": "John Doe", "reviews": []})

    def test_new_review(self):
        newReview = Review(1, "Positive comment about student.", True)
        assert newReview.id == None
        assert newReview.student_id == 1
        assert newReview.comment == "Positive comment about student."
        assert newReview.is_positive == True

    def test_review_get_json(self):
        newReview = Review(1, "Positive comment about student.", True)
        review_json = newReview.get_json()
        self.assertDictEqual(review_json, {"id": None, "student_id": 1, "comment": "Positive comment about student.", "is_positive": True})


'''
    Integration Tests
'''

# This fixture creates an empty database for the test and deletes it after the test
# scope="class" would execute the fixture once and resued for all methods in the class
@pytest.fixture(autouse=True, scope="module")
def empty_db():
    app = create_app({'TESTING': True, 'SQLALCHEMY_DATABASE_URI': 'sqlite:///test.db'})
    create_db()
    yield app.test_client()
    db.drop_all()


class IntegrationTests(unittest.TestCase):
    
    def test_create_user(self):
        user = create_user("bob", "bobpass")
        assert user.username == "bob"
    
    def test_authenticate(self):
        user = create_user("rick", "bobpass")
        assert login("rick", "bobpass") != None

    def test_get_all_users_json(self):
        users_json = get_all_users_json()
        self.assertListEqual([{"id":1, "username":"rick"}, {"id":2, "username":"bob"}], users_json)

    # Tests data changes in the database
    def test_update_user(self):
        update_user(1, "ronnie")
        user = get_user(1)
        assert user.username == "ronnie"

    def test_create_student(self):
        student = add_student("John")
        assert student.name == "John"

    def test_create_review(self):
        review = add_review(1, "John is an OK Student.", 1)
        assert review.student_id == 1
        assert review.comment == "John is an OK Student."
        assert review.is_positive == 1

    def test_update_review(self):
        review = add_review(1, "John is a good Student.", 1)
        review = update_review(1, 1, "John is a bad Student.", 0)
        assert review.student_id == 1
        assert review.comment == "John is a bad Student."
        assert review.is_positive == 0

    def test_delete_review(self):
        deleted = delete_review(1)
        assert deleted == True

    def test_search_student(self):
        student = add_student("Jane")
        assert get_student_by_name("Jane") != None

    def test_student_reviews(self):
        reviews = get_reviews_for_student(1)
        assert reviews != None
