import os
import sys

class Employee:
    def __init__(self, id, name, designation, salary):
        self.id = id
        self.name = name
        self.designation = designation
        self.salary = salary

    def __repr__(self):
        return "Employee(id=%s, name=%s, designation=%s, salary=%s)" % (self.id, self.name, self.designation, self.salary)

def add_employee(id, name, designation, salary):
    with open("employees.txt", "a") as f:
        f.write("%s\n" % id)

    with open("employee_details.txt", "a") as f:
        f.write("%s %s %s %s\n" % (id, name, designation, salary))

def delete_employee(id):
    with open("employees.txt", "r") as f:
        lines = f.readlines()

    with open("employees.txt", "w") as f:
        for line in lines:
            if line.strip() != id:
                f.write(line)

    with open("employee_details.txt", "r") as f:
        lines = f.readlines()

    with open("employee_details.txt", "w") as f:
        for line in lines:
            if line.split()[0] != id:
                f.write(line)

def display_employee(id):
    with open("employee_details.txt", "r") as f:
        for line in f:
            if line.split()[0] == id:
                print(line)

def main():
    while True:
        print("1. Add employee")
        print("2. Delete employee")
        print("3. Display employee")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            designation = input("Enter employee designation: ")
            salary = input("Enter employee salary: ")
            add_employee(id, name, designation, salary)
        elif choice == "2":
            id = input("Enter employee ID: ")
            delete_employee(id)
        elif choice == "3":
            id = input("Enter employee ID: ")
            display_employee(id)
        elif choice == "4":
            sys.exit()

if __name__ == "__main__":
    main()
