from school.models import PrimaryClassDB, CollegeClassDB, HighSchoolClassDB

# Primary classes
p_grade_1 = PrimaryClassDB(
    grade="first grade",
    type="primary",
)
p_grade_2 = PrimaryClassDB(
    grade="second grade",
    type="primary",
)
p_grade_3 = PrimaryClassDB(
    grade="third grade",
    type="primary",
)
p_grade_4 = PrimaryClassDB(
    grade="fourth grade",
    type="primary",
)
p_grade_5 = PrimaryClassDB(
    grade="fifth grade",
    type="primary",
)
p_grade_6 = PrimaryClassDB(
    grade="sixth grade",
    type="primary",
)

c_grade_1 = CollegeClassDB(
    grade="first college year",
    type="college",
)
c_grade_2 = CollegeClassDB(
    grade="second college year",
    type="college",
)
c_grade_3 = CollegeClassDB(
    grade="third college year",
    type="college",
)

h_grade_1 = HighSchoolClassDB(
    grade="first high school year",
    type="high_school",
)
h_grade_2 = HighSchoolClassDB(
    grade="second high school year",
    type="high_school",
)
h_grade_3 = HighSchoolClassDB(
    grade="third high school year",
    type="high_school",
)