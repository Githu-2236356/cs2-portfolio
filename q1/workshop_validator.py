import time
import re
import random
import string

denial_reason = None

Student_Name = input("Please put in your student name: ")
if not Student_Name.strip():
    print("Error: Student name is required.")
    denial_reason = "Student name is required but was left blank."

if denial_reason is None:
    print("Please Wait...")
    time.sleep(1)
    try:
        Student_Age = int(input("Please enter your student age: "))
        if Student_Age > 18 or Student_Age < 11:
            print("Error: Invalid Age. Must be between 11 and 18.")
            denial_reason = f"Age ({Student_Age}) is outside the required range of 11 to 18."
    except ValueError:
        print("Error: Invalid Age. Please enter a number.")
        denial_reason = "Age must be a valid number."

if denial_reason is None:
    print("Please Wait...")
    time.sleep(1)
    try:
        Student_Grade = int(input("Please enter your student grade level: "))
        if Student_Grade < 7 or Student_Grade > 12:
            print("Error: Invalid Grade Level. Must be 7 to 12.")
            denial_reason = f"Grade level ({Student_Grade}) is outside the required range of 7 to 12."
    except ValueError:
        print("Error: Invalid Grade Level. Please enter a number.")
        denial_reason = "Grade level must be a valid number."

if denial_reason is None:
    print("Please Wait...")
    time.sleep(1)
    
    registration_pattern = r"^[A-Za-z]\d{5}$" 
    
    while True:
        try:
            Student_Code = input("Enter your 6-digit registration code: ").strip() 
            if not re.match(registration_pattern, Student_Code):
                raise ValueError("Format must be 1 letter followed by 5 numbers (e.g., B72839).")
            print(f"Success! '{Student_Code}' is a valid registration code.")
            break
            
        except ValueError as error:
            print(f"Invalid Input: {error}")
            print("Please try again.\n")

print("\nProcessing final registration...")
time.sleep(1)

if denial_reason is None:
    print("============================")
    print("    🎉  Registration Accepted!  🎉    ")
    print("============================") 
else:
    print("===========================")
    print("      ❌  Registration Denied  ❌     ")
    print("===========================")
    print(f"Reason: {denial_reason}\n")
