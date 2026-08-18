import time
import math 

#hi this is nate, this is my very first comment lmao oh and the code attached to this comment defines the point
try:
#for inputs
x1 = float(input("Enter x1: ")) 

y1 = float(input("Enter y1: "))

x2 = float(input("Enter x2: "))

y2 = float(input("Enter y2: "))

#loading text cause why not?
print("loading...")
time.sleep(2)

#Epik final answer (Updated to use math.pow and math.sqrt)
confusing_formula = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
epik_final_answer = round(confusing_formula, 2)
print("Euclidean Distance:", epik_final_answer)

except ValueError: 
# If anyone tries to be sneaky by adding a number
print("That isnt a number😡")

#I wanna say that this entire coding process was really really fun to learn like my last coding experiences. But one major issue i have is that i forget a lot of the important things i learn with little of it retaining in my memory. Luckily though that means i just have to keep learning and i'll keep getting better, which seems to be easy seeing how much I love coding.
