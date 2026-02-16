from .school_class_model import PrimaryClassDB, CollegeClassDB, HighSchoolClassDB
from .course_model import CourseDB
from .student_model import StudentDB
from .teacher_model import TeacherDB
from .parent_model import ParentDB
from .group_model import GroupDB
from .associations import (
    groups_course,
    groups_teacher,
    school_class_course,
    students_course,
    students_groupes,
    teachers_course,
)

__all__ = [
    "PrimaryClassDB",
    "CollegeClassDB",
    "HighSchoolClassDB",
    "CourseDB",
    "StudentDB",
    "TeacherDB",
    "ParentDB",
    "GroupDB",
    "groups_course",
    "groups_teacher",
    "school_class_course",
    "students_course",
    "students_groupes",
    "teachers_course",
]
