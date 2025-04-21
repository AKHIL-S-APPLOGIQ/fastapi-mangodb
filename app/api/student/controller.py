from app.config.database import db
from bson import ObjectId

student_collection = db["students"]

# 🔸 Create Student
async def create_student_controller(data: dict):
    result = await student_collection.insert_one(data)
    return str(result.inserted_id)

# 🔸 Get one by ID
async def get_student_controller(student_id: str):
    student = await student_collection.find_one({"_id": ObjectId(student_id)})
    if student:
        student["id"] = str(student["_id"])
        del student["_id"]
    return student

# 🔸 Get all students
async def get_all_students_controller():
    students = []
    async for student in student_collection.find():
        student["id"] = str(student["_id"])
        del student["_id"]
        students.append(student)
    return students

# 🔸 Update Student
async def update_student_controller(student_id: str, data: dict):
    result = await student_collection.update_one(
        {"_id": ObjectId(student_id)},
        {"$set": data}
    )
    return result.modified_count > 0

# 🔸 Delete Student
async def delete_student_controller(student_id: str):
    result = await student_collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0

# 🔸 Search Students with Text Index
async def search_students_controller(query: str, skip: int = 0, limit: int = 10):
    students = []
    query_regex = {"$regex": query, "$options": "i"}  # Case-insensitive regex search

    cursor = student_collection.find({
        "$or": [
            {"name": query_regex},
            {"grade": query_regex},
            {"enrollment_date": query_regex}
        ]
    }).skip(skip).limit(limit)

    async for student in cursor:
        student["id"] = str(student["_id"])
        del student["_id"]
        students.append(student)

    return students

# 🔸 Filter Students by Specific Fields
async def filter_students_controller(filters: dict):
    students = []
    query = {}

    # Add filters based on provided fields
    if "name" in filters:
        query["name"] = {"$regex": filters["name"], "$options": "i"}  # Case-insensitive search
    if "age" in filters:
        query["age"] = filters["age"]
    if "grade" in filters:
        query["grade"] = {"$regex": filters["grade"], "$options": "i"}  # Case-insensitive search
    if "enrollment_date" in filters:
        query["enrollment_date"] = filters["enrollment_date"]
    if "joined_year" in filters:
        query["joined_year"] = filters["joined_year"]

    async for student in student_collection.find(query):
        student["id"] = str(student["_id"])
        del student["_id"]
        students.append(student)

    return students


async def search_students_controller1(query: str, skip: int = 0, limit: int = 10):
    students = []
    cursor = student_collection.aggregate([
        {"$match": {"$text": {"$search": query}}},
        {"$skip": skip},
        {"$limit": limit},
        {"$sort": {"name": 1}}  # Sort by name
    ])
    
    async for student in cursor:
        student["id"] = str(student["_id"])
        del student["_id"]
        students.append(student)

    return students