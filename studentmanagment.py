import time

# ------------------- Utility Functions -------------------

def loading_animation(message="Loading"):
    for i in range(3):
        print(f"{message}{'.'*i}", end="\r")
        time.sleep(0.5)
    print(f"{message}... Done!    ")

def pause():
    try:
        input("\nPress Enter to continue...")
    except EOFError:
        pass

def grade_calc(avg):
    if avg >= 90: return "A+"
    elif avg >= 80: return "A"
    elif avg >= 70: return "B+"
    elif avg >= 60: return "B"
    else: return "C"

def print_line():
    print("="*50)

def print_title(title):
    print_line()
    print(title.center(50))
    print_line()

def print_subtitle(subtitle):
    print(f"\n-- {subtitle} --\n")

# ------------------- Menu -------------------

def show_menu():
    print_title("STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student Info")
    print("5. Delete Student")
    print("6. Add Marks")
    print("7. Statistics")
    print("8. Exit")
    print_line()

# ------------------- Core Functions -------------------

def add_student(school):
    print_subtitle("Add New Student")
    while True:
        class_name = input("Enter Class (e.g., 11, 12): ").strip()
        if class_name: break
        print("Class cannot be empty!")
    while True:
        roll_no = input("Enter Roll No: ").strip()
        if roll_no: break
        print("Roll No cannot be blank!")
    while True:
        name = input("Enter Name: ").strip()
        if name: break
        print("Name cannot be blank!")
    while True:
        gender = input("Enter Gender (M/F): ").strip().upper()
        if gender in ["M","F"]: break
        print("Gender must be M or F!")
    while True:
        dob = input("Enter DOB (DD-MM-YYYY): ").strip()
        if dob: break
        print("DOB cannot be blank!")
    marks = {"Math":0,"Physics":0,"Chemistry":0,"English":0,"Biology":0}
    student = [roll_no, name, gender, dob, marks]

    # Add student to class
    for cls in school:
        if cls[0] == class_name:
            cls[1].append(student)
            break
    else:
        school.append([class_name,[student]])

    print(f"\n✅ Student '{name}' added to Class {class_name} successfully!")
    loading_animation("Saving student data")
    pause()

def display_students(school):
    print_subtitle("Displaying All Students")
    if not school:
        print("No students in school yet.")
        pause()
        return
    for cls in school:
        print(f"\nClass {cls[0]}:")
        if not cls[1]:
            print("  No students yet.")
        else:
            for s in cls[1]:
                print(f"  Roll No: {s[0]} | Name: {s[1]} | Gender: {s[2]} | DOB: {s[3]}")
    pause()

# ------------------- Search -------------------

def search_student(school):
    while True:
        roll_no = input("Enter Roll No to search: ").strip()
        if roll_no: break
        print("Roll No cannot be blank!")

    print_subtitle("Searching Student")
    loading_animation("Searching student record")
    found = False
    for cls in school:
        for s in cls[1]:
            if s[0] == roll_no:
                print(f"\n✅ Found Student in Class {cls[0]}:")
                print(f"  Roll No: {s[0]}\n  Name: {s[1]}\n  Gender: {s[2]}\n  DOB: {s[3]}")
                print("  Marks:")
                for subject, mark in s[4].items():
                    print(f"    {subject}: {mark}")
                found = True
                break
        if found: break
    if not found:
        print("❌ Student not found.")
    pause()

# ------------------- Update -------------------

def update_student(school):
    while True:
        roll_no = input("Enter Roll No to update: ").strip()
        if roll_no: break
        print("Roll No cannot be blank!")
    print_subtitle("Updating Student Info")
    found = False
    for cls in school:
        for s in cls[1]:
            if s[0] == roll_no:
                print(f"\nUpdating Student {s[1]} (Class {cls[0]})")
                name_input = input(f"Enter new Name [{s[1]}]: ").strip()
                if name_input: s[1] = name_input
                gender_input = input(f"Enter new Gender [{s[2]}]: ").strip().upper()
                if gender_input in ["M","F"]: s[2] = gender_input
                dob_input = input(f"Enter new DOB [{s[3]}]: ").strip()
                if dob_input: s[3] = dob_input
                print("\n✅ Student info updated successfully!")
                loading_animation("Updating database")
                found = True
                break
        if found: break
    if not found:
        print("❌ Student not found.")
    pause()

# ------------------- Delete -------------------

def delete_student(school):
    while True:
        roll_no = input("Enter Roll No to delete: ").strip()
        if roll_no: break
        print("Roll No cannot be blank!")
    print_subtitle("Deleting Student")
    found = False
    for cls in school:
        for i, s in enumerate(cls[1]):
            if s[0] == roll_no:
                removed = cls[1].pop(i)
                print(f"\n❌ Student '{removed[1]}' deleted successfully!")
                loading_animation("Updating database")
                found = True
                break
        if found: break
    if not found:
        print("❌ Student not found.")
    pause()

# ------------------- Add Marks -------------------

def add_marks(school):
    while True:
        roll_no = input("Enter Roll No to add/update marks: ").strip()
        if roll_no: break
        print("Roll No cannot be blank!")
    found = False
    print_subtitle("Add/Update Marks")
    for cls in school:
        for s in cls[1]:
            if s[0] == roll_no:
                print(f"\nAdding/Updating marks for {s[1]} (Class {cls[0]})")
                for subject in s[4]:
                    while True:
                        try:
                            mark_input = input(f"Enter marks for {subject} [{s[4][subject]}]: ").strip()
                            if mark_input == "":
                                break
                            marks = int(mark_input)
                            if 0 <= marks <= 100:
                                s[4][subject] = marks
                                break
                            else:
                                print("Marks must be between 0 and 100")
                        except ValueError:
                            print("Invalid input! Enter an integer")
                print("\n✅ Marks updated successfully!")
                loading_animation("Saving marks")
                found = True
                break
        if found: break
    if not found:
        print("❌ Student not found.")
    pause()

# ------------------- Statistics -------------------

def statistics(school):
    if not school:
        print("No data available.")
        pause()
        return
    print_subtitle("Statistics")
    loading_animation("Calculating statistics")
    for cls in school:
        print(f"\nClass {cls[0]}:")
        print(f"  Total Students: {len(cls[1])}")
        if cls[1]:
            total_avg = 0
            max_avg = -1
            topper = None
            for s in cls[1]:
                avg = sum(s[4].values())/len(s[4])
                total_avg += avg
                if avg > max_avg:
                    max_avg = avg
                    topper = s
            print(f"  Topper: {topper[1]} with Average {max_avg:.2f}")
            print(f"  Class Average: {total_avg/len(cls[1]):.2f}")
    pause()

# ------------------- Handle Choice -------------------

def handle_choice(choice, school):
    if choice == 1: add_student(school)
    elif choice == 2: display_students(school)
    elif choice == 3: search_student(school)
    elif choice == 4: update_student(school)
    elif choice == 5: delete_student(school)
    elif choice == 6: add_marks(school)
    elif choice == 7: statistics(school)
    elif choice == 8:
        print("\nExiting Program...")
        loading_animation("Exiting")
        return "exit"
    else:
        print("Invalid choice! Enter 1-8.")
        pause()

# ------------------- Main Loop -------------------

def main():
    school = []
    while True:
        show_menu()
        try:
            choice_input = input("Enter your choice (1-8): ").strip()
            if choice_input == "":
                raise ValueError("Choice cannot be blank")
            choice = int(choice_input)
            if choice not in range(1,9):
                raise ValueError("Choice must be 1-8")
            result = handle_choice(choice, school)
            if result == "exit":
                break
        except ValueError as ve:
            print(f"❌ Invalid input: {ve}")
            pause()
        except Exception as e:
            print(f"❌ Unexpected error: {e}")
            pause()

# ------------------- Run Program -------------------

if __name__ == "__main__":
    main()
