"""
SPPU Computer Engineering DSA Lab 
Group F
Experiment Sr. No. - 23

Department maintains a student information. The file contains roll number, name, division and address. Allow user to add,
delete information of student. Display information of particular employee. If record of student does not exist an 
appropriate message is displayed. If it is, then the system displays the student details. Use sequential file to main the data.
"""

import sys

INDEX_FILE = "students.txt"
DETAILS_FILE = "student_details.txt"


class Student:
    def __init__(self, roll_no, name, standard, marks):
        self.roll_no = roll_no
        self.name = name
        self.standard = standard
        self.marks = marks

    def __repr__(self):
        return f"Student(roll_no={self.roll_no}, name={self.name}, standard={self.standard}, marks={self.marks})"


def add_student(roll_no, name, standard, marks):
    with open(INDEX_FILE, "a") as index_file:
        index_file.write(f"{roll_no}\n")

    with open(DETAILS_FILE, "a") as details_file:
        details_file.write(f"{roll_no} {name} {standard} {marks}\n")


def delete_student(roll_no):
    with open(INDEX_FILE, "r") as index_file:
        lines = index_file.readlines()

    with open(INDEX_FILE, "w") as index_file:
        for line in lines:
            if line.strip() != roll_no:
                index_file.write(line)

    with open(DETAILS_FILE, "r") as details_file:
        lines = details_file.readlines()

    with open(DETAILS_FILE, "w") as details_file:
        for line in lines:
            if line.split()[0] != roll_no:
                details_file.write(line)


def display_student(roll_no):
    with open(DETAILS_FILE, "r") as details_file:
        for line in details_file:
            if line.split()[0] == roll_no:
                print(line, end="")


def main():
    student_index = set()

    with open(INDEX_FILE, "r") as index_file:
        for line in index_file:
            student_index.add(line.strip())

    while True:
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Display Student")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            roll_no = input("Enter Student Roll No.: ")
            if roll_no in student_index:
                print("Student with Roll No. already exists.")
                continue
            name = input("Enter Student name: ")
            standard = input("Enter Student standard: ")
            marks = input("Enter Student marks: ")
            add_student(roll_no, name, standard, marks)
            student_index.add(roll_no)
        elif choice == "2":
            roll_no = input("Enter Student Roll No.: ")
            if roll_no not in student_index:
                print("Student with Roll No. does not exist.")
                continue
            delete_student(roll_no)
            student_index.remove(roll_no)
        elif choice == "3":
            roll_no = input("Enter Student Roll No.: ")
            if roll_no not in student_index:
                print("Student with Roll No. does not exist.")
                continue
            display_student(roll_no)
        elif choice == "4":
            sys.exit()


if __name__ == "__main__":
    main()
