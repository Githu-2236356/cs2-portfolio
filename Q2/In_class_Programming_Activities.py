import time

try: 
   input("Press enter to begin Programming Activity 1")
   failed_count = 0
   answer = 7
   
   while True:
     guess = int(input("Guess a number: "))
  
     if guess == answer:
       print("Correct!")
       break
     else:
       failed_count += 1
       print(f"Wrong password. Failed attempts: {failed_count}")
     

   print()
   input("Press enter to begin Programming Activity 2")
   question = input("YES or NO? ")
   while question != "YES":
     print("No, enter YES")
     question = input("YES or NO? ")
   print("Correct!")

   print()
   input("Press enter to begin Programming Activity 3")
   def PA():
     for i in range(3, 33, 3):
       time.sleep(0.4)
       print(i)
  
   PA()

   print()
   input("Press enter to begin Programming Activity 4")
   def Mot():
     msg = input("Enter a motivational message: ")
     amount = int(input("Enter the amount of times it will be repeated:"))
     for i in range(amount):
       time.sleep(0.4)
       print(msg)

   Mot()
except ValueError:
 print("Invalid input")
