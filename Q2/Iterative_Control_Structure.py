# The nate signature unnecesary comment
# this is a redo, my old code got accidentally deleted and im not happy about it because i spent a lot of time on it.

try:
 #imports below
 import time
 import math

 #made each exercise a function since i did not want to make them separate
 def exercise_1():
        for num in range(2, 21, 2):
         #delay to make each number appear one at a time and not make your eyes hurt as much
         time.sleep(0.4)
         print(num)
        return
         
 input("Press enter to begin exercise 1") #made you control pace to make it nice
 exercise_1() #calls function
 print() #empty print to make a nice space between exercises
 input("Press enter to begin exercise 2")

 def exercise_2():
        count = 10 #starts at 10
        while count >= 1: # checks if the count is above or equal to 1
          time.sleep(0.4)
          print(count) #shows count
          count -= 1 #reduces count by 1 every print
        time.sleep(0.4)
        print("Time is up!") #prints after 1 > count
        return
         
 exercise_2()
 print()
 input("Press enter to begin exercise 3")

 def exercise_3():
  for num in range(1, 16):
    if num % 3 == 0:
        continue
    time.sleep(0.4)
    print(num) 

 exercise_3()
 print()
 input("Press enter to begin exercise 4")

 def exercise_4():
         def show_table(number):
           for i in range(1, 11):
              time.sleep(0.4)
              print(f"{number} x {i} = {number * i}")

         user_number = int(input("Enter a number: "))
         show_table(user_number)
 
 exercise_4()
 
except ValueError:
        print("Invalid input") 

        
