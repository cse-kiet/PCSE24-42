import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://face-attendance-system-7861d-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data ={
    "1":
        {
            "id":"1",
            "name":"Arijit Jayaswal",
            "major":"Computer Science",
            "starting_year":2020,
            "total_attendance":30,
            "standing":"G",
            "email":"arijit@gmail.com",
            "password":"1arijit",
            "year":4,
            "dob":"2001-09-18",
            "phone":"8177025927",
            "last_attendance_time":"2024-06-01 22:39:10",
            "content":"Arijit Jayaswal is a final year student in the department of Computer Science. He is regular to classes and is good academically"
        },
    "2":
        {
            "id":"2",
            "name":"Bill Gates",
            "major":"Research",
            "starting_year":2018,
            "total_attendance":32,
            "standing":"G",
            "email":"billgates@soft.com",
            "password":"2bill",
            "year":5,
            "dob":"1986-01-08",
            "phone":"7920518663",
            "last_attendance_time":"2023-10-14 09:10:00",
            "content":"Bill Gates is a great researcher in the field of technology and has published countless papers."
        },
    "3":
        {
            "id":"3",
            "name":"Elon Musk",
            "major":"Robotics",
            "starting_year":2021,
            "total_attendance":36,
            "standing":"VG",
            "email":"elonmusk@gmail.com",
            "password":"elon",
            "year":3,
            "dob":"1992-06-28",
            "phone":"9410058104",
            "last_attendance_time":"2024-06-01 19:55:11",
            "content":"Elon musk is working in the field of robotics. He is an excellent student and is always trying to level up"
        },
    "4":
        {
            "id":"4",
            "name":"Amrendra Singh",
            "major":"Computer Science",
            "starting_year":2020,
            "total_attendance":28,
            "standing":"G",
            "email":"realamrendra@gmail.com",
            "password":"amrendra",
            "year":4,
            "dob":"2002-02-07",
            "phone":"8739082323",
            "last_attendance_time":"2024-06-01 19:53:11",
            "content":"Amrendra is a final year student of Computer Science. He is good in academics and has very good communication skills."
        },        
}


for key, value in data.items():
    ref.child(key).set(value)
