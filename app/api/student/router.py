from fastapi import APIRouter, HTTPException, Query
from app.api.student.schemas import StudentResponse, StudentCreate
from app.api.student.controller import (
    create_student_controller, get_student_controller, get_all_students_controller, 
    update_student_controller, delete_student_controller, 
    search_students_controller, filter_students_controller
)

router = APIRouter()

# 🔸 Create a Student
@router.post("/", response_model=StudentResponse)
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    student_id = await create_student_controller(student_dict)
    student_dict["id"] = student_id
    return student_dict

@router.get("/search", response_model=list[StudentResponse])
async def search_students(query: str, skip: int = 0, limit: int = 10):
    if not query:
        raise HTTPException(status_code=400, detail="Query string is required.")
    
    students = await search_students_controller(query, skip=skip, limit=limit)
    return students

# 🔸 Get a Student by ID
@router.get("/{student_id}", response_model= StudentResponse)
async def get_student(student_id: str):
    student = await get_student_controller(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# 🔸 Get All Students
@router.get("/", response_model=list[ StudentResponse])
async def get_all_students():
    students = await get_all_students_controller()
    return students

# 🔸 Update a Student
@router.put("/{student_id}", response_model= StudentResponse)
async def update_student(student_id: str, student:  StudentCreate):
    student_dict = student.dict()
    updated = await update_student_controller(student_id, student_dict)
    if not updated:
        raise HTTPException(status_code=404, detail="Student not found")
    student_dict["id"] = student_id
    return student_dict

# 🔸 Delete a Student
@router.delete("/{student_id}", response_model=dict)
async def delete_student(student_id: str):
    deleted = await delete_student_controller(student_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

# 🔸 Filter Students
@router.get("/filter", response_model=list[StudentResponse])
async def filter_students(
    name: str = Query(None, alias="name"),
    age: int = Query(None, alias="age"),
    grade: str = Query(None, alias="grade"),
    enrollment_date: str = Query(None, alias="enrollment_date"),
    joined_year: int = Query(None, alias="joined_year")
):
    filters = {
        "name": name,
        "age": age,
        "grade": grade,
        "enrollment_date": enrollment_date,
        "joined_year": joined_year
    }
    # Remove any filters that are None
    filters = {key: value for key, value in filters.items() if value is not None}
    
    students = await filter_students_controller(filters)
    return students
