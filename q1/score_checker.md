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

# PseudoCode
  ```text
START
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
```
  
END

# Clean Code Implementation

### Source Code:
Click here for the [`Source Code`](./score_checker.py)

# Testing

| Test | Input | Purpose | Expected Output | Actual Output | Result |
|---|---|---|---|---|---|
| 1 | -1 | Below minimum | Invalid score. | Invalid score. | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid score. | Invalid score. | PASS |

# Testing Reflection

### Why is it important to test the values 0 and 100?
So that we know which range the number given is, and then we give them their grade/output.

### Why did you also test -1 and 101?
To ensure that the input given is valid and is within the range needed.

### Which test helped you understand boundary conditions the most?
Testing for number ranges was a real pain in my side, but it was fun to learn and made me gain a deeper understanding.

### Did any of your tests initially fail? If yes, what did you change in your program?
Yes, initially a few bugs came in, the syntax was wrong a few times and i used the wrong functions. But i managed to do research, changed it to the correct syntax, and even learned a few extra things to add to the program.

# Reflection

### How did selection structures make the program more useful?
Selection structures let the program become more open to new inputs.

### How did proper comments and readable formatting improve your program?
Proper readable and proper formatting will help other people understand the programs code easier and quicker, making it more efficient and organized.

### Why is it useful to plan the program using a flowchart and pseudocode before writing the code?
Planning a program with flowcharts and pseudocode before writing the actual code allows you to gain a deeper insight and understanding of what your planning to build. Which could help you become more efficient in your coding experience.
