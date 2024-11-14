import studentpackage
from studentpackage.files import import_details, import_from_excel
from studentpackage.studentid import Student


mystudent=[]
#student_details=import_details("result.txt")
student_details=import_from_excel("details.xlsx")
for key,value in student_details.items():
    student = Student(key,value)
    mystudent.append(student)

for student in mystudent:
    if student.marks >= 60:
        student.student_info()

subject_list=["maths","science","physics"]

mystudent[1].maxmarks=30
mystudent[1].validate_marks()
mystudent[1].save_result("results.xlsx",)