import time

def type(phrase, newline):
    for char in phrase:
        print(char, end = "", flush = True)
        time.sleep(0.02)
    if newline == True:
        print("")
    time.sleep(0.2)
    return None

def num_handling(lower, upper, float_bool):
    number = input("")
    while True: 
        try:
            if float_bool == True:
                num_type = "a float"
                number = float(number)
            else:
                num_type = "an integer"
                number = int(number)
        except:
            type(f"Please type {num_type}!!!: ", False)
            number = input("")
            continue
        else:
            if not lower <= number <= upper:
                type("That's quite an interesting number, and it's not really in the range, now what's the real number???: ", False)
                number = input("")
                continue
        return number

def average(num_list):
    total = 0
    for number in num_list:
        total += number
    return total / len(num_list)

def decision(options):
    response = input("").lower()
    while response not in options:
        type("I'm sorry but that wasn't an option. What's your real answer? ", False)
        response = input("").lower()
    return response

type("Welcome to your very own GPA Calculator!\n", True)

type("How many classes do you have semester 1? [1-10]: ", False)
sem1num = num_handling(1, 10, False)

type("How many classes do you have semester 2? [1-10]: ", False)
sem2num = num_handling(1, 10, False)

sem1 = []
type("\nSemester 1!", True)
for num in range(1, sem1num + 1):
    type(f"What's your grade for class {num} (0.0 - 4.0): ", False)
    sem1.append(num_handling(0.0, 4.0, True))

sem2 = []
type("\nSemester 2!", True)
for num in range(1, sem2num + 1):
    type(f"What's your grade for class {num} (0.0 - 4.0): ", False)
    sem2.append(num_handling(0.0, 4.0, True))

grades = sem1 + sem2
gpa = round(average(grades), 2)
sem1gpa = round(average(sem1), 2)
sem2gpa = round(average(sem2), 2)

type(f"You're total grade point average is {gpa}", True)
type(f"Your gpa for semester 1 is {sem1gpa}", True)
type(f"Your gpa for semester 2 is {sem2gpa}", True)

while True:
    type("Do you want to analyze a certain selection of classes or figure out how to get youre gpa goals [selection/goals] ", False)
    sel_goal = decision(["selection", "goals"])

    match sel_goal:
        case "selection":
            type("Would you like to look at semester 1, semester 2, or the same class between the two semesters? [1, 2, same] ", False)
            answer = decision(["1", "2", "same"])

            if answer == "same":
                class_options = []
                buffer = 1
                if len(sem1) > len(sem2):
                    for value in sem1:
                        class_options.append(buffer)
                        buffer += 1
                else:
                    for value in sem2:
                        class_options.append(buffer)
                        buffer += 1

                type(f"Which class would you like to look at? {class_options}", True)
                type("(Note: If you select a class that you only have one semester, the average will just be that value) ", False)
                same_class = int(decision(str(class_options)))
                if same_class > len(sem1):
                    same_class_avg = sem2[same_class - 1]
                elif same_class > len(sem2):
                    same_class_avg = sem1[same_class - 1]
                else:
                    same_class_avg = round((sem1[same_class - 1] + sem2[same_class - 1])/2, 2)
                type(f"You're average of class number {same_class} is equal to {same_class_avg}", True)

            else:
                type(f"What range of classes would you like to look at in semester {answer}? (Ex: 1-4) ", False)
                classes_range = input("").split("-")
                print(classes_range)

        case "goals":
            print("goober")
