# Software Engineering II (COMP3613) Assignment 1
### __Group Information:__
* __Group Name:__ Byte Bros
* __Group Members:__ Isaiah Rambhajan, Javonte Baldeo, Pranav Soondar, Teal Trim

### __Project Information:__
* __Course Name:__ Software Engineering II
* __Course Code:__ COMP 3613
* __Assignment:__ COMP3613 Assignment 2
* __Date:__ 18/10/2024

# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing Dependencies
```bash
$ pip install -r requirements.txt
```

# Application Commands:
* To Initialize the Database
```bash
flask init
```

# Student Commands:
* Add Student
```bash
flask student add "<student_name>"
```

* Get Student by Name:
```bash
flask student get "<student_name>"
```

* List All Students:
```bash
flask student list
```

* Add Review for a Student:
```bash
flask student review <student_id> "<comment>" <is_positive>
```

* View Reviews for a Student: 
```bash
flask student reviews <student_id>
```

# General Notes
* This project was developed using GitHub Codespaces.