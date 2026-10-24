# The nate signature unnecesary comment

try:
    Score1 = input("Enter Score 1: ")
    Score2 = input("Enter Score 2: ")
    Score3 = input("Enter Score 3: ")

    task1 = Score1 != ""
    task2 = Score2 != ""
    task3 = Score3 != ""

    s1 = float(Score1) if task1 else 0.0
    s2 = float(Score2) if task2 else 0.0
    s3 = float(Score3) if task2 else 0.0

    completed_tasks = int(task1) + int(task2) + int(task3)
    print(f"Completed Tasks: {completed_tasks}")

    def calculate_average(score1, score2, score3, tasks_count):
        total_score = (score1 if task1 else 0) + (score2 if task2 else 0) + (score3 if task3 else 0)
        average = total_score / tasks_count if tasks_count > 0 else 0.0
        print(f"Average: {average:.2f}")
        return average

    def get_performance(score1, score2, score3, tasks_count, avg_score):
        mastery = (tasks_count == 3) and (85 <= score1 <= 100) and (85 <= score2 <= 100) and (85 <= score3 <= 100)
        excellent = (tasks_count < 3) and (avg_score > 85)
        needs_review = (score1 < 70 and task1) or (score2 < 70 and task2) or (score3 < 70 and task3)
        developing = not mastery and not excellent and not needs_review

        if mastery:
            return "Mastery"
        elif excellent:
            return "Excellent"
        elif developing:
            return "Developing"
        elif needs_review:
            return "Needs Review"

    def is_eligible(score1, score2, score3, tasks_count):
        mastery = (tasks_count == 3) and (85 <= score1 <= 100) and (85 <= score2 <= 100) and (85 <= score3 <= 100)
        return mastery

    if completed_tasks > 0:
        calculated_avg = calculate_average(s1, s2, s3, completed_tasks)
        
        performance_status = get_performance(s1, s2, s3, completed_tasks, calculated_avg)
        print(f"Performance: {performance_status}")
        
        eligible = is_eligible(s1, s2, s3, completed_tasks)
        print(f"Eligible: {eligible}")
    else:
        print("Invalid Input")

except ValueError:
    print("Invalid Input")

#calculate_average returns a number in the "float" sense. get_performance is the function that returns/displays a text string. is_eligible was a pain to make but uses true or false booleans like the instructions said.
#the average is calculate in calculate_average, then used to put students grades in a criteria using the function get_performance
#when a student has a high average or an average above 85 but didnt complete the 3 tasks, i put "Excellent" instead to ensure them that they did a good job but arent exactly a master.
#Because "return" helps put back the values for later use.
