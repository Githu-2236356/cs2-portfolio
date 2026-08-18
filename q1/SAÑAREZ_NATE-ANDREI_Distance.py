import time
import math

try:
    #for inputs
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))

    #loading text cus cool
    print("Loading...")
    time.sleep(2)

    confusing_formula = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    epik_final_answer = round(confusing_formula, 2)
    print("The distance between the two points is: ", epik_final_answer)
    time.sleep(5)

except ValueError:
    #if someone tries to be sneaky and put a letter or word
    print("That isnt a number😡")
    time.sleep(5)
    #I wanna say that this entire coding process was really really fun to learn like my last coding experiences. But one major issue i have is that i forget a lot of the important things i learn with little of it retaining in my memory. Luckily though that means i just have to keep learning and i'll keep getting better, which seems to be easy seeing how much I love coding.
