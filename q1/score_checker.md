# Logic Analysis:

### Input: 
The grade of the student using it

### Boundary: 
The minimum valid score is 0

### Boundary: 
The maximum valid score is 100

### Possible outputs: 
Outstanding, Very Satisfactory, Satisfactory, Needs improvement, Invalid Score

### Selection Pattern: the minimum valid score is zero, the code is down below
    if score < 0:
        print("Calculating grade...")
        time.sleep(2)
        print("Invalid Score")
        
### Selection Pattern: the maximum valid score is 100, the code is down below
    if score > 100:
        print("Calculating grade...")
        time.sleep(2)
        print("Invalid Score")

### Boundary Condition, What condition will you use to determine whether the score is valid?
What condition will you use to determine whether the score is valid?
score < 0 or score > 100

### Multiple Decision Paths, Explain how the program decides which classification should be displayed.
The program checks if the grade given is between a range of numbers, as shown in the selection patterns, and gives an output which is listed in the "Possible outputs"

# Flowchart
<img width="882" height="627" alt="chart" src="https://github.com/user-attachments/assets/93a8b963-f62e-4c44-b307-228bc50858b7" />

# PseudoCodeSTART
  
INPUT score
  IF score < 0 OR score > 100 THEN
    DISPLAY "Invalid score."
  ELSE IF score >= 90 THEN
    DISPLAY "Outstanding"
  ELSE IF score >= 80 THEN
    DISPLAY "Very Satisfactory"
  ELSE IF score >= 75 THEN
    DISPLAY "Satisfactory"
  ELSE
    DISPLAY "Needs Improvement"
  END IF
END

# Clean Code Implementation

### Source Code
The Python source code file is located at [`./q1/score_checker.py`](./score_checker.py)[cite: 1].
