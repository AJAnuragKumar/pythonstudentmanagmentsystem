#------------------------------Class 11th Programs---------------------------------


# Program 01: To find the sum of digits upto a given number

num = int(input("Enter a number: "))
sum_digits = 0

var = num
while var >= 0:
    sum_digits+=var
    var-=1
print("Sum of digits of", num, "is:", sum_digits)


# Program 02: To display Fibonacci series up to n terms

n = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b


# Program 03: To check if a number is prime

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number.")
            break
    else:
        print(num, "is a prime number.")
else:
    print("Enter a number greater than 1.")


# Program 04: To count vowels and consonants in a string

text = input("Enter a string: ").lower()
vowels = "aeiou"
v_count = c_count = 0

for ch in text:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1

print("Vowels:", v_count)
print("Consonants:", c_count)

# Program 05: To print the factorial of number

num = int(input("Enter a number: "))
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial of", num, "is:", fact)

# Program 06: To check string is palindrome or not 

text = input("Enter a string: ")
if text == text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# Program 07: To sort with the help of bubble sort 

arr = [64, 25, 12, 22, 11]
n = len(arr)
for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print("Sorted list:", arr)


# Program 08: To search the element with the help of binary search 

arr = [10, 20, 30, 40, 50]
x = int(input("Enter element to search: "))
low, high = 0, len(arr) - 1
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == x:
        print(x, "found at position", mid + 1)
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print(x, "not found in the list.")

# Program 09: For checking armstrong number 

num = int(input("Enter a number: "))
order = len(str(num))
sum_pow = sum(int(digit) ** order for digit in str(num))
if num == sum_pow:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

# Program 10: To search element with the help of linear search 

arr = [12, 45, 23, 67, 89, 10]
x = int(input("Enter element to search: "))
for i in range(len(arr)):
    if arr[i] == x:
        print(x, "found at position", i + 1)
        break
else:
    print(x, "not found in the list.")

# Program 11: To print area and perimeter of circle 

import math

r = float(input("Enter radius of circle: "))
area = math.pi * r ** 2
perimeter = 2 * math.pi * r

print("Area of circle =", round(area, 2))
print("Perimeter of circle =", round(perimeter, 2))

# Program 12: To display a calendar of a given month and year

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print("\n", calendar.month(year, month))

# Program 13: To find the largest and smallest element in a list

numbers = [23, 45, 12, 67, 34, 89, 2]
largest = smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


# Program 14: To find the greatest common divisor (GCD) of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD is:", a)

# Program 15: To count words in a given sentence

sentence = input("Enter a sentence: ")
words = sentence.split()
print("Total words:", len(words))



#------------------------------Class 12th Programs---------------------------------

# Program 01: Stack implementation with all operations (with try-except handling)

stack = []  # empty list to represent stack
MAX_SIZE = 5  # maximum size of the stack

def push():
    try:
        if len(stack) == MAX_SIZE:
            print("⚠️ Stack Overflow! Cannot push more elements.")
        else:
            element = input("Enter element to push: ")
            stack.append(element)
            print(f"✅ '{element}' pushed into stack.")
    except Exception as e:
        print("Error during push operation:", e)

def pop():
    try:
        if not stack:
            print("⚠️ Stack Underflow! Stack is empty.")
        else:
            element = stack.pop()
            print(f"🗑️ Popped element: {element}")
    except Exception as e:
        print("Error during pop operation:", e)

def peek():
    try:
        if not stack:
            print("⚠️ Stack is empty. Nothing to peek.")
        else:
            print("👀 Top element:", stack[-1])
    except Exception as e:
        print("Error while peeking:", e)

def display():
    try:
        if not stack:
            print("📭 Stack is empty.")
        else:
            print("\n📦 Stack elements (top → bottom):")
            for i in range(len(stack)-1, -1, -1):
                print(stack[i])
    except Exception as e:
        print("Error while displaying stack:", e)

while True:
    try:
        print("\n------ STACK OPERATIONS MENU ------")
        print("1. PUSH")
        print("2. POP")
        print("3. PEEK (TOP ELEMENT)")
        print("4. DISPLAY STACK")
        print("5. EXIT")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            peek()
        elif choice == '4':
            display()
        elif choice == '5':
            print("👋 Exiting program... Thank you!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")
    except Exception as e:
        print("Unexpected error:", e)


# Program 02: Student Table Management using File Handling (with Add, Delete, Search, Update)
# File: students.txt

FILENAME = "students.txt"

def add_student():
    try:
        with open(FILENAME, "a") as f:
            roll = input("Enter Roll No: ")
            name = input("Enter Name: ")
            marks = input("Enter Marks: ")
            f.write(f"{roll},{name},{marks}\n")
        print("✅ Student record added successfully!")
    except Exception as e:
        print("Error while adding student:", e)

def display_students():
    try:
        with open(FILENAME, "r") as f:
            data = f.readlines()
            if not data:
                print("📭 No records found!")
                return
            print("\n📘 Student Records:")
            print("Roll No | Name | Marks")
            for line in data:
                roll, name, marks = line.strip().split(",")
                print(f"{roll} | {name} | {marks}")
    except FileNotFoundError:
        print("⚠️ File not found! Add a record first.")
    except Exception as e:
        print("Error while displaying students:", e)

def search_student():
    try:
        roll_search = input("Enter Roll No to search: ")
        found = False
        with open(FILENAME, "r") as f:
            for line in f:
                roll, name, marks = line.strip().split(",")
                if roll == roll_search:
                    print(f"🎯 Record Found: Roll No: {roll}, Name: {name}, Marks: {marks}")
                    found = True
                    break
        if not found:
            print("❌ Record not found.")
    except FileNotFoundError:
        print("⚠️ File not found! Add a record first.")
    except Exception as e:
        print("Error while searching student:", e)

def delete_student():
    try:
        roll_del = input("Enter Roll No to delete: ")
        found = False
        with open(FILENAME, "r") as f:
            lines = f.readlines()
        with open(FILENAME, "w") as f:
            for line in lines:
                roll, name, marks = line.strip().split(",")
                if roll != roll_del:
                    f.write(line)
                else:
                    found = True
        if found:
            print("🗑️ Record deleted successfully!")
        else:
            print("❌ Roll number not found.")
    except FileNotFoundError:
        print("⚠️ File not found! Add a record first.")
    except Exception as e:
        print("Error while deleting student:", e)

def update_student():
    try:
        roll_update = input("Enter Roll No to update marks: ")
        found = False
        with open(FILENAME, "r") as f:
            lines = f.readlines()
        with open(FILENAME, "w") as f:
            for line in lines:
                roll, name, marks = line.strip().split(",")
                if roll == roll_update:
                    new_marks = input("Enter new marks: ")
                    f.write(f"{roll},{name},{new_marks}\n")
                    found = True
                    print("✏️ Record updated successfully!")
                else:
                    f.write(line)
        if not found:
            print("❌ Roll number not found.")
    except FileNotFoundError:
        print("⚠️ File not found! Add a record first.")
    except Exception as e:
        print("Error while updating student:", e)

while True:
    try:
        print("\n------ STUDENT MANAGEMENT SYSTEM ------")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Roll No")
        print("4. Delete Student")
        print("5. Update Student Marks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            update_student()
        elif choice == '6':
            print("👋 Exiting program... Have a great day!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 6.")
    except Exception as e:
        print("Unexpected error:", e)

#Program 03: To Store employee details and calculate yearly salary automatically.
import pickle

f = open("employee.dat", "wb")
n = int(input("Enter number of employees: "))
data = []
for i in range(n):
    eid = int(input("Emp ID: "))
    name = input("Name: ")
    salary = float(input("Monthly Salary: "))
    data.append([eid, name, salary, salary * 12])
pickle.dump(data, f)
f.close()

with open("employee.dat", "rb") as f:
    emp = pickle.load(f)
    for e in emp:
        print(f"ID:{e[0]}, Name:{e[1]}, Yearly Salary:{e[3]}")

# Program 04: Password Storage System using CSV File

import csv

FILENAME = "users.csv"

def add_user():
    try:
        with open(FILENAME, "a", newline='') as f:
            writer = csv.writer(f)
            username = input("Enter username: ")
            password = input("Enter password: ")
            writer.writerow([username, password])
        print("✅ User added successfully!")
    except Exception as e:
        print("Error while adding user:", e)

def view_users():
    try:
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            print("\n🧾 Stored Users:")
            for row in reader:
                print(f"Username: {row[0]}, Password: {row[1]}")
    except FileNotFoundError:
        print("⚠️ No user data found!")
    except Exception as e:
        print("Error while reading file:", e)

def login():
    try:
        uname = input("Enter username: ")
        pwd = input("Enter password: ")
        with open(FILENAME, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == uname and row[1] == pwd:
                    print("🔓 Login successful!")
                    return
            print("❌ Invalid username or password.")
    except FileNotFoundError:
        print("⚠️ User database not found!")
    except Exception as e:
        print("Error during login:", e)

while True:
    print("\n--- PASSWORD STORAGE SYSTEM ---")
    print("1. Add User")
    print("2. View All Users")
    print("3. Login")
    print("4. Exit")

    choice = input("Enter choice (1-4): ")
    if choice == '1':
        add_user()
    elif choice == '2':
        view_users()
    elif choice == '3':
        login()
    elif choice == '4':
        print("👋 Exiting... Have a secure day!")
        break
    else:
        print("❌ Invalid choice! Try again.")

# Program 05: To-Do List 

FILENAME = "tasks.txt"

def add_task():
    with open(FILENAME, "a") as f:
        f.write(input("Enter task: ") + "\n")
    print("✅ Task added successfully!")

def view_tasks():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()
            if not tasks:
                print("📭 No tasks found!")
                return
            print("\n📋 Your Tasks:")
            for i, t in enumerate(tasks, 1):
                print(f"{i}. {t.strip()}")
    except FileNotFoundError:
        print("⚠️ No tasks file found!")

def delete_task():
    try:
        with open(FILENAME, "r") as f:
            tasks = f.readlines()
        view_tasks()
        num = int(input("\nEnter task number to delete: "))
        if 1 <= num <= len(tasks):
            del tasks[num - 1]
            with open(FILENAME, "w") as f:
                f.writelines(tasks)
            print("🗑️ Task deleted!")
        else:
            print("❌ Invalid task number.")
    except FileNotFoundError:
        print("⚠️ No tasks file found!")

while True:
    print("\n--- TO-DO LIST WITH DELETE ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    ch = input("Enter choice: ")
    if ch == '1':
        add_task()
    elif ch == '2':
        view_tasks()
    elif ch == '3':
        delete_task()
    elif ch == '4':
        print("👋 Goodbye! Stay productive!")
        break
    else:
        print("❌ Invalid choice! Try again.")


# Program 06: Bank Management System using a binary file

import pickle

def add_account():
    acc = {"acc_no": input("Account No: "), "name": input("Name: "), "bal": float(input("Balance: "))}
    with open("bank.dat", "ab") as f:
        pickle.dump(acc, f)
    print("✅ Account added!\n")

def view_accounts():
    try:
        with open("bank.dat", "rb") as f:
            while True:
                print(pickle.load(f))
    except EOFError:
        pass
    except FileNotFoundError:
        print("❌ No records found!")

def search_account():
    n = input("Enter account no: ")
    found = False
    try:
        with open("bank.dat", "rb") as f:
            while True:
                acc = pickle.load(f)
                if acc["acc_no"] == n:
                    print("🔍 Found:", acc); found = True
    except EOFError:
        if not found: print("❌ Account not found!")
    except FileNotFoundError:
        print("❌ No records file found!")

while True:
    ch = input("\n1.Add 2.View 3.Search 4.Exit: ")
    if ch == "1": add_account()
    elif ch == "2": view_accounts()
    elif ch == "3": search_account()
    else: 
        break
