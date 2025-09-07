**📚 Course Management Web App**

A fully functional Course Management Web Application built with Python and Streamlit, featuring CRUD operations, course recommendations, and detailed course management.

**Features**

✅ Core Features

Add Course: Admins can add a new course with details:

Title

Description

Instructor Name

Duration

Fees

Mode (Online/Offline)

View Courses: Display all courses with clear, readable layout.

Update Course: Edit course details easily.

Delete Course: Remove courses if no longer offered.

Search & Recommendation: Users can type a course name and see related courses in the same category.

**Tech Stack**

Frontend: Streamlit (Interactive web interface)

Backend: Python (Business logic & database handling)

Database: SQLite (Lightweight storage for courses)

Optional AI: For recommendation (based on course name matching)

**Project Structure**
course_management_app/
│
├── app.py                  # Main Streamlit app
├── db.py                   # Database handling (CRUD operations)
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .venv/                  # Python virtual environment

**Setup & Installation**
Clone the repository

git clone <https://github.com/vidya-MLAI/Course-Management-Web-App>
cd course_management_app

**Create virtual environment and activate**

python -m venv .venv
# Windows
.venv\Scripts\activate
# Mac/Linux
source .venv/bin/activate

**Install dependencies**

pip install -r requirements.txt


**Run the app**

streamlit run app.py

**Usage**

Use the sidebar to navigate between Add, View, Update, and Delete courses.

Search for a course in the recommendation field to see related courses in the same category.

Fill in all fields carefully when adding or updating a course.

**Notes**

Make sure to have the SQLite database file in the same directory (courses.db).

This app can easily be extended with AI-powered recommendations or other advanced features.

**License**

This project is open-source and free to use for educational and personal projects.
