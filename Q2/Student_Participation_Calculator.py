#Code by nate and shiery
try:
  day1 = float(input("Enter Day 1 participation (In hours): "))
  Score1 = float(input("Enter Day 1 quiz score: "))
  day2 = float(input("Enter Day 2 participation (In hours): "))
  Score2 = float(input("Enter Day 2 quiz score: "))
  day3 = float(input("Enter Day 3 participation (In hours): "))
  Score3 = float(input("Enter Day 3 quiz score: "))

  def calculate_total_hours(day1, day2, day3):
   total_hours = day1 + day2 + day3
   return print("Total hours:", total_hours)

  total_hours = day1 + day2 + day3

  def get_participation_level(total_hours):
    if 8 <= total_hours:
      print("highly active")
    elif 5 <= total_hours < 8:
      print("active")
    elif 5 > total_hours:
      print("Needs improvement")

  def calculate_quiz_score(Score1, Score2, Score3):
    quiz_score = Score1 + Score2 + Score3
    return quiz_score

  quiz_score = Score1 + Score2 + Score3

  def is_certificate_eligible(total_hours, quiz_score):
    if quiz_score == 30 and 8 <= total_hours:
     print("Is eligible: True")
    else:
     print("Is eligible: False")
    return
   

  calculate_total_hours(day1, day2, day3)
  get_participation_level(total_hours)
  is_certificate_eligible(total_hours, quiz_score)
 
except ValueError:
  print("Invalid Input! This message is shown if you left an input blank or put a letter instead of a number.")
