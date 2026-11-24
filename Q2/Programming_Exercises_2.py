# nate signature unnecesary comment
import math
import time

try:
  input("Press enter to begin Exercise 1 ")
  print()
  school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]
  time.sleep(0.4)
  print(school_items[0])
  time.sleep(0.4)
  print(school_items[1])
  time.sleep(0.4)
  print(school_items[2])
  time.sleep(0.4)
  print(school_items[3])
  time.sleep(0.4)
  print(school_items[4])
  time.sleep(0.4)
  print("First item:", school_items[0])
  time.sleep(0.4)
  print("Last item:", school_items[4])
  print()
  input("Press enter to begin Exercise 2 ")
  print()
  destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]
  time.sleep(0.4)
  print("All Destinations:")
  print(*destinations, sep=", ")
  time.sleep(0.4)
  print("\nCurrent Destinations:")
  time.sleep(0.4)
  print(*destinations[1:4], sep=", ")
  time.sleep(0.4)
  search_query = input("\nEnter a destination to search for: ")
  time.sleep(0.4)
  if search_query in destinations:
      print(f"{search_query} exists in the list.")
  else:
      print(f"{search_query} does not exist in the list.")
  time.sleep(0.4)
  destinations[2] = "Iloilo"
  print("\nUpdated Destinations:")
  time.sleep(0.4)
  print(*destinations, sep=", ")
  
except ValueError:
  print("Invalid Input")
