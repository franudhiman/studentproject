# class def
import json

from studentpackage.files import store_results, store_to_excel


class Student:
    # class attribute
    maxmarks = 100

    # constructor
    def __init__(self, name, marks):
        # instance attributes
        self.name = name
        self.marks = marks


    def get_name(self):
        return self.name

    def set_name(self, name):  # getter setter methods
        self.name = name

    def student_info(self):
        print(f"name:", self.get_name())
        print(f"marks:", self.get_marks())
        print(f"percentage:", self.percentcalculate())

    def get_student_info(self):
        student_info={}
        student_info.update()
        student_info.update({"name:": self.get_name()})
        student_info.update({"marks:": self.get_marks()})
        student_info.update({"percentage:": self.percentcalculate()})
        return student_info




    def get_marks(self):
        return self.marks

    def set_marks(self, marks):  # getter setter methods
        self.marks = marks

    def percentcalculate(self):
        percentage = (self.marks / self.maxmarks) * 100
        return percentage

    def validate_marks(self):
        try:
            result = self.marks/self.maxmarks
            print(f"marks validated:",result)
        except ZeroDivisionError:
            print("Cannot divide by zero.")
        finally:
            print("This will run regardless of an exception.")

    def save_result(self,fn):
        data= self.get_student_info()
        store_to_excel(fn,data)

mystudent1=Student()

