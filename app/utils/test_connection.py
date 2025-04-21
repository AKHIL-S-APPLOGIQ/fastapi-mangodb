from pymongo import MongoClient
import json,random
from datetime import date,datetime
from bson.objectid import ObjectId  # Needed to query using _id

# MongoDB connection URI
uri = "mongodb+srv://akhilsapplogiq:akhilsapplogiq@project01.ykcwdjt.mongodb.net/?retryWrites=true&w=majority&appName=project01"
client = MongoClient(uri)

# Connect to database and collection
db = client["schoolmanagement"]
student_collection = db["student"]

# student_collection.delete_many({})
# Helper to generate random join date
def generate_random_join_date(start_year=2008, end_year=2025):
    year = random.randint(start_year, end_year)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime(year, month, day)

# Generate student documents with department_id
def generate_students(num_students):
    departments = ["Science", "Arts", "Commerce","Math", "History", "Biology", "Chemistry", "Physics", "English", "Computer"]
    grades = ["A", "B", "C", "D"]
    classes = ["i", "ii", "iii"]
    cities = ["Chennai", "Coimbatore", "Madurai", "Trichy", "Salem"]
    states = ["Tamil Nadu", "Kerala", "Karnataka"]

    students = []

    for i in range(1, num_students + 1):
        name = f"Student{i}"
        student = {
            "name": name,
            "age": random.randint(13, 18),
            "email": f"{name.lower()}@example.com",
            "class": random.choice(classes),
            "department": random.choice(departments),
            "grade": random.choice(grades),
            "join_date": generate_random_join_date(),
            "address": {
                "city": random.choice(cities),
                "state": random.choice(states)
            },
            "is_active": random.choice([True, False])
        }
        students.append(student)

    return students

# Insert generated students
# students = generate_students(200)
# insert_result = student_collection.insert_many(students)
# print("Inserted students:", len(insert_result.inserted_ids))


def filter_students_by_year(year):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year + 1, 1, 1)

    print(start_date)
    print(end_date)

    students = student_collection.find({
        "join_date": {
            "$gte": start_date,
            "$lt": end_date  # strictly less than Jan 1 of next year
        }
    })

    student_list = list(students)

    for student in students:
        print(student)
    
    print("Number of students:", len(student_list))

# Example usage
# filter_students_by_year(2020)
# filter_students_by_year(2021)


def filter_students(students, **filters):
    def match(student):
        for key, value in filters.items():
            if isinstance(value, list):
                # If the filter value is a list, check if the student matches any value in the list
                if student.get(key) not in value:
                    return False
            elif "." in key:
                # For nested keys like 'address.city'
                keys = key.split(".")
                data = student
                for k in keys:
                    data = data.get(k, {})
                if data != value:
                    return False
            else:
                if student.get(key) != value:
                    return False
        return True

    return [s for s in students if match(s)]

# 👇 Fix is here
students = list(student_collection.find())
filtered = filter_students(students, department="Science", grade="A")

for student in filtered:
    print(student)


