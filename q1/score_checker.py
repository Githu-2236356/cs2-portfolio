#imports
import time
import math

#try for valid inputs
try:
    #Score calculations and added loading time for calculating effect
    score = float(input("Please enter your grade: "))
    if score in range(90,101):
        print("Calculating grade...")
        time.sleep(2)
        print("Outstanding")
    
    if score in range(80,90):
        print("Calculating grade...")
        time.sleep(2)
        print("Very Satisfactory")

    if score in range(75,80):
        print("Calculating grade...")
        time.sleep(2)
        print("Satisfactory")

    if score in range(0,75):
        print("Calculating grade...")
        time.sleep(2)
        print("Needs Improvement")

    if score < 0:
        print("Calculating grade...")
        time.sleep(2)
        print("Invalid Score")

    if score > 100:
        print("Calculating grade...")
        time.sleep(2)
        print("Invalid Score")
        
    time.sleep(2)
    print("Shutting down...")
    time.sleep(2)
    print("Calculation complete")

#except ValueError if someone enters an invalid input
except ValueError:
    print("Your input was not valid")
