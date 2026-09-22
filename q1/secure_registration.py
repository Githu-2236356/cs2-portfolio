import re

ValidSections = ["Dahlia"]
ValidClubs = ["Robotics", "Science", "Mathematics", "Programming"]
ValidAttendance = ["Present", "Absent", "Late"]

try:
    student_name = input("Enter Student Name: ").strip()
    student_section = input("Enter Student Section: ").strip()
    student_club = input("Enter Student Club: ").strip()
    student_email = input("Enter Student Email: ").strip()
    attendance_status = input("Enter Attendance Status: ").strip()

    if not student_name:
        raise ValueError("Student name is required.")

    if student_section not in ValidSections:
        raise ValueError(
            f"Invalid section. Allowed sections: {', '.join(ValidSections)}"
        )

    if student_club not in ValidClubs:
        raise ValueError("Please choose a valid club.")

    if "@" not in student_email or "." not in student_email:
        raise ValueError("Invalid email format. Must contain '@' and '.'.")

    if attendance_status not in ValidAttendance:
        raise ValueError(
            f"Invalid attendance status. Must be one of: {', '.join(ValidAttendance)}"
        )

    print("\nREGISTRATION ACCEPTED")
    print(f"Student: {student_name}")
    print(f"Section: {student_section}")
    print(f"Club: {student_club}")
    print(f"Email: {student_email}")
    print(f"Attendance: {attendance_status}")

except ValueError as e:
    print(f"\nREGISTRATION REJECTED: {e}")
