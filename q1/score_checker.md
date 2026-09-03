#Logic Analysis:
Input: The program needs the grade of the student using it
Boundary: The minimum valid score is 0
Boundary: The maximum valid score is 100
Possible outputs: Outstanding, Very Satisfactory, Satisfactory, Needs improvement, Your input was not invalid, Invalid Score
Selection Pattern:
    if score > 100:
        print("Calculating grade...")
        time.sleep(2)
        print("Invalid Score")
Selection Pattern:
