from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize, add_student


from App.database import db
from App.controllers.student import *
from App.controllers.review import *
from App.controllers.user import *
from App.controllers.auth import *
from App.models import Student


index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


#######################################TESTING ROUTES####################################

@index_views.route('/test_post', methods=['POST'])
def testing2():
    return jsonify(message='I WORKED!')

@index_views.route('/test_create_review', methods=['POST'])
def testing_create_review():
    data = request.json
    student_id = data.get('Student_id')
    comment = data.get('Comment')
    is_positive = data.get('Is_positive')
    if add_review(student_id, comment, is_positive):
        return jsonify(message='Successfully added review')
    return jsonify(message='Failed to add review')

@index_views.route('/test_get_reviews', methods=['POST'])
def testing_get_reviews():
    data = request.json
    student_id = data.get('Student_id')
    all_reviews = get_reviews_for_student(student_id)
    reviews_json = [review.get_json() for review in all_reviews]
    return jsonify(reviews=reviews_json)

@index_views.route('/test_create_user', methods=['POST'])
def testing_create_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if create_user(username, password):
        return jsonify({"message": "User Created"}), 201
    return jsonify({"message": "Failed to Create User"}), 400

@index_views.route('/testing_login', methods=['POST'])
def testing_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if login(username,password):
        return jsonify({"message": "Successful Login"}), 201  # Great Success
    return jsonify({"message": "Failed Login"}), 400  # Great Failure    

@index_views.route('/add_student', methods=['POST'])
def testing_add_student():
        data = request.json
        student_name = data.get('Name')
        if student_name:
            result = add_student(student_name)
            return jsonify({"message": "Successfully added student"}), 201  # Great Success
        else:
            return jsonify({"error": "Great Failure"}), 400 # Great Failure

@index_views.route('/test_get', methods=['GET'])
def testing_get_route():
    return jsonify(message='I WORKED!') 

@index_views.route('/test_get_students', methods=['GET'])
def testing_get_students():
    all_students = get_all_students()
    students_json = [student.get_json() for student in all_students]
    return jsonify(students=students_json) 

   
@index_views.route('/test_update_review/<int:review_id>', methods=['PUT'])
def testing_update_reviews(review_id):
    data = request.json
    student_id = data.get('Student_id')
    comment = data.get('Comment')
    is_positive = data.get('Is_positive')
    if update_review(review_id, student_id, comment, is_positive):
        return jsonify(message='Successfully Updated!') 
    return jsonify(message='Failed to Update!')  

@index_views.route('/test_delete_review/<int:review_id>', methods=['DELETE'])
def testing_delete_review(review_id):
    if delete_review(review_id):
        return jsonify(message='Successfully Deleted!') 
    return jsonify(message='Failed to Delete!')  
 
