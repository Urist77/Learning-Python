# zyDE 11.1.1a: Dictionary example: Gradebook.

def main():
    student_grades = {}  # Create an empty dict
    grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
    menu_prompt = ("1. Add/modify student grade\n"
                    "2. Delete student grade\n"
                    "3. Print student grades\n"
                    "4. Quit\n")

    while True:  # Exit when user selects 4 to quit
        command = input(menu_prompt).strip()  # what is not needed on this line? .lower() - working with numbers
        if command == '1':
            name, grade = input(grade_prompt).split() # what is missing here?
            student_grades[name.title()] = grade.strip().upper() # added .title() to name variable and .strip() + .upper() to grade variable
        elif command == '2':
            # pass
            name = input("Delete which student's grade? ").strip().title()
            # del student_grades[name] # if user misspells name program will crash
            print(student_grades.pop(name, 'Student not in gradebook.'))
        elif command == '3':
            # pass
            print(student_grades)
        elif command == '4':
            break
        else:
            print('Unrecognized command.')

main()