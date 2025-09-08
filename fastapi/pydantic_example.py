from pydantic import BaseModel
from typing import List

class LessonContent(BaseModel):
    title : str
    tldr : str
    main_image_url : str
    body : List[str]

class Lesson(BaseModel):
    id : int
    lesson_index : int
    title : str
    is_locked : bool
    content : LessonContent

class Module(BaseModel):
    id : int
    index : int
    title : str
    is_locked : bool
    lessons : List[Lesson]
    completed_lessons : List[Lesson]

class Course(BaseModel):
    id : int 
    title : str
    prereq_courses_ids : List[int] | None = None
    is_locked : bool
    modules : List[Module]
    completed_modules : List[Module]

Course.model_rebuild()