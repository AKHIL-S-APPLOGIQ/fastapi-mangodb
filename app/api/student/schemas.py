from pydantic import BaseModel
from datetime import datetime

class StudentBase(BaseModel):
    name: str
    age: int
    grade: str
    address: str
    phone_number: str
    email: str
    dob: str  # Date of birth
    gender: str
    enrollment_date: str  # Date of enrollment
    nationality: str
    parent_name: str
    parent_contact: str
    guardian_name: str
    guardian_contact: str
    emergency_contact: str
    joined_year: int  # Year of joining

    created_at: datetime = datetime.now()  # Timestamp of when the student was created
    updated_at: datetime = datetime.now()  # Timestamp for when the student was last updated

class StudentCreate(StudentBase):
    pass

class StudentResponse(StudentBase):
    id: str
