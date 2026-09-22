# Fundamentals of Cybersecurity and Data Privacy
**Activity:** PSHS Secure Club Registration System

**Name:** Nate Andrei P. Sañarez

**Section:** Dahlia

**Quarter:** 1

## Activity Overview
I analysed cybersecurity threats and how to prevent them

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case
**Case Number:** Case 1
**Case Title:** Fake Login Alert
> A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

### 1. What cybersecurity threat is shown?
Phishing, as in stealing the students personal online information.

### 2. What warning signs make the situation suspicious?
* Requests for login credentials and other private information without valid reasoning

### 3. What may be affected?
Check or describe all that apply:
- [x] Data
- [x] Account
- [ ] Application
- [ ] Device
- [ ] Network
- [ ] Financial information
> **Explanation:** The hacker tries to steal the students data and account to sell to data brokers or for even worse purposes

### 4. What information could be exposed or misused?
Usernames, passwords, private messages and/or information.

### 5. What should the user do to reduce the risk?
Report it to School IT or a teacher

---

# Part B - Data Privacy and Secure Data Capture

| Data Field | Collect / Do Not Collect | Reason |
| :--- | :--- | :--- |
| Student Name | COLLECT | Necessary to identify the student registering. |
| Section | COLLECT | Needed to organize students by class. |
| Club Choice | COLLECT | Core requirement for club assignment. |
| School Email | COLLECT | Needed for official communication and verification. |
| Attendance Status | COLLECT | Needed for tracking student presence. |
| Password | DO NOT COLLECT | Unnecessary and presents a major security risk. |
| OTP | DO NOT COLLECT | Not required for a basic club registration form. |
| Home Address | DO NOT COLLECT | Excessive personal information not required for school clubs. |
| Parent Bank Account | DO NOT COLLECT | Completely irrelevant and introduces severe financial risk. |

## Privacy Question
### Why is it safer to collect only information that the program actually needs?
So that if data is ever stolen, there is nothing but the information already given

---

# Part C - Security-Focused Validation Rules

| Data Captured | Expected Input | Possible Risk | Invalid Input Example | Validation Rule | Error Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Student Name | Non-blank string | Empty submissions | `[blank]` | Must not be empty[cite: 1] | Student name is required. |
| Section | Valid section name[cite: 1] | Incorrect grouping | `Rose` | Must match allowed list | Invalid section. |
| Club Choice | Valid club name[cite: 1] | Invalid registration | `Gaming` | Must match predefined list | Please choose a valid club. |
| School Email | Proper email string[cite: 1] | Invalid contact | `studentpshs.edu.ph` | Must contain `@` and `.` | Invalid email format. |
| Attendance Status | Valid status string | Incorrect record | `Here` | Must be Present/Absent/Late | Invalid attendance status. |

## Secure Data Capture Questions

### 1. What should your program accept?
Inputs that are considered valid based off the instructions.

### 2. What should your program reject?
Blank inputs, invalid club choices, and inputs not correlated to what is asked for.

### 3. How do your validation rules help reduce incorrect or unsafe input?
By verifying inputs before deeming them valid or not

---

# Part D - Secure Program Implementation

## Source Code File
[secure_registration.py](secure_registration.py)

## Final Code
```python
import re

VALID_SECTIONS = ["Dahlia"]
VALID_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
VALID_ATTENDANCE = ["Present", "Absent", "Late"]

try:
    student_name = input("Enter Student Name: ").strip()
    student_section = input("Enter Student Section: ").strip()
    student_club = input("Enter Student Club: ").strip()
    student_email = input("Enter Student Email: ").strip()
    attendance_status = input("Enter Attendance Status: ").strip()

    if not student_name:
        raise ValueError("Student name is required.")

    if student_section not in VALID_SECTIONS:
        raise ValueError(
            f"Invalid section. Allowed sections: {', '.join(VALID_SECTIONS)}"
        )

    if student_club not in VALID_CLUBS:
        raise ValueError("Please choose a valid club.")

    if "@" not in student_email or "." not in student_email:
        raise ValueError("Invalid email format. Must contain '@' and '.'.")

    if attendance_status not in VALID_ATTENDANCE:
        raise ValueError(
            f"Invalid attendance status. Must be one of: {', '.join(VALID_ATTENDANCE)}"
        )

    print("\nREGISTRATION ACCEPTED")
    print(f"Student: {student_name}")
    print(f"Section: {student_section}")
    print(f"Club: {student_club}")
    print(f"Email: {student_email}")
    print(f"Attendance: {attendance_status}")

except ValueError as e:
    print(f"\nREGISTRATION REJECTED: {e}")
