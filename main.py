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
                num_type = " float"
                number = float(number)
            else:
                num_type = "n integer"
                number = int(number)
        except:
            type(f"Please type a{num_type}!!!: ", False)
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

type("Welcome to your very own GPA Calculator!\n", True)

type("How many classes do you have semester 1?: ", False)
sem1num = num_handling(1, 10, False)

type("How many classes do you have semester 2?: ", False)
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
gpa = average(grades)
sem1gpa = average(sem1)
sem2gpa = average(sem2)

type(f"You're total grade point average is {gpa}", True)

type("Would you like to know your specific gpa for semester 1 or 2? [1/2] ", False)
answer = input("")
while answer != "1" and answer != "2":
    type("I'm sorry but that wasn't an option. What's your real answer? ", False)
    answer = input("")

match answer:
    case "1":
        type(f"Your gpa for semester 1 is {sem1gpa}", True)
    case "2":
        type(f"Your gpa for semester 2 is {sem2gpa}", True)