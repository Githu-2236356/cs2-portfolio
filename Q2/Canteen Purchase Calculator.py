#Hi this is nate, just a signature comment

try:
  
  quantity = int(input("Please enter the quantity of your items: "))
  price = int(input("Please enter the price of your item: "))
  payment = int(input("Please enter the amount paid: "))
  
  #this function gets the total by multiplying the price with the quantity of items
  def calculate_total(price, quantity):
    return price * quantity

  #this is the variable where the total price is stored to use in the function for calculating change
  total = calculate_total(price, quantity)

  #this function finds the difference between the payment and total price to get the change
  def calculate_change(payment,total):
    return total - payment
  
  print("Total price: PHP", calculate_total(price, quantity))
  print("Change: PHP", calculate_change(payment,total))

#Price is the amount of money neeeded to pay for a single item, while quantity is the amount of items with that price
#Separating change calculatin and total calculation is really helpful, because it can stop mixups, simplify code, and avoid having errors
