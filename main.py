Students = []

# definintion of variables of Register 
# add the new students   
def add_students():
    
    id = int(input("Enter the id of student: "))
    name = input(" Enter the name of student: ")
    edad = (input(" Enter the age of student: "))
    curso = input(" Enter the grade of student: ")
    state = input(" Enter the state of student: ")
    
    student= {
        
        "id": id,
        "name": name,
        "edad": edad,
        "curso": curso,
        "state": state
        
    }
    
    Students.append(Students)
    print("student added.\n")
    
def show_student_list(Students):
    """Displays all studets_list"""
    if not Students:
        print("Studen_list is empty.\n")
        return
    for p in Students:
        print(f"{p['id']} | {p['name']} | {p['edad']} {p['curso']} | {p['state']}")
    print()


def search_student(Students):
    """Searches a student by name. Returns dict or None."""
    name = input("name: ").strip().lower()
    for p in Students:
        if p["name"].lower() == name:
            print(f"Found: {p}\n")
    print("student  not found.\n")
    return None



def delete_students(Students):
    """Removes a student from the list by name."""
    name = input("student name to delete: ").strip().lower()
    for p in Students:
        if p["name"].lower() == name:
            Students.remove(p)
            print("Deleted.\n")
            return
    print("Student no found.\n")


# Show the menu
option = ""

while option != "5":
    print("\n1. add_students")
    print("2. Show_student_list")
    print("3. search_student")
    print("4. delete_student")
    print("5. thank you for using the sistem")

    option = input("\n----Choose an option----: ")

    if option == "1":
        add_students()
    elif option == "2":
        show_student_list()
    elif option == "3":
        search_student()
    elif option == "4":
        delete_students()
    elif option == "5":
        print("thank you for using the sistem:)")
    else:
        print("\n----Invalid option----")
        
