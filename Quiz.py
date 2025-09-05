import time

print("\n********************\n")
print("Welcome to the Quiz!")
print("\n********************\n")

score = 0
start_time = time.time()        # Record start time
time_limit = 120             # 2 minutes in seconds

def check_time():
    """End quiz if 2 minutes have passed."""
    if time.time() - start_time > time_limit:
        print("\nTime's up! Quiz ended.")
        print("Your score is:", score, "/ 10")
        exit()

# Question 1
check_time()
q1 = input("1. Who created Python?\nA) James Gosling\nB) Guido van Rossum\nC) Md Ratul Hasan Abid\nD) Showmick Roy Chowdhury\n\nThe answer is: ")
if q1.upper() == "B":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is Guido van Rossum.\n")

# Question 2
check_time()
q2 = input("2. Abstraction in computational thinking is used to:\nA) Focus only on the important details of a problem\nB) Break the problem into steps\nC) Remember all details of the problem\nD) Write pseudocode\n\nThe answer is: ")
if q2.upper() == "A":
    print("Correct.\n")
    score += 1
else:
    print("Your answer is wrong.\nThe correct answer is Focus only on the important details of a problem\n")
 
# Question 3
check_time()
q3 = input("3. What is the output of print(type([]))?\nA) <class 'tuple'>\nB) <class 'set'>\nC) <class 'dict'>\nD) <class 'list'>\n\nThe answer is: ")
if q3.upper() == "D":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is <class 'list'>\n")
 
# Question 4
check_time()
q4 = input("4. Which keyword is used to create a function in Python?\nA) func\nB) function\nC) def\nD) lambda\n\nThe answer is: ")
if q4.upper() == "C":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is def\n")
 
# Question 5
check_time()
q5 = input("5. Decomposition in computational thinking means:\nA) Making a problem bigger\nB) Breaking down a complex problem into smaller parts\nC) Ignoring unnecessary details\nD) Writing the final solution directly\n\nThe answer is: ")
if q5.upper() == "B":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is Breaking down a complex problem into smaller parts\n")
 
# Question 6
check_time()
q6 = input("6. Which operator is used for floor division?\nA) //\nB) /\nC) %\nD) **\n\nThe answer is: ")
if q6.upper() == "A":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is //\n")
 
# Question 7
check_time()
q7 = input("7. A company uses computational thinking to analyze customer behavior. If they group customers into categories based on repeated purchase patterns, they are applying:\nA) Abstraction\nB) Decomposition\nC) Pattern recognition\nD) Algorithm design\n\nThe answer is: ")
if q7.upper() == "C":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is Pattern recognition\n")
 
# Question 8
check_time()
q8 = input("8. Which keyword is used to exit a loop prematurely in Python?\nA) stop\nB) exit\nC) end\nD) break\n\nThe answer is: ")
if q8.upper() == "D":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is break\n")
 
# Question 9
check_time()
q9 = input("9. Which of the following loop(s) always executes at least once in Python?\nA) for loop\nB) while loop\nC) Both A and B\nD) None of these\n\nThe answer is: ")
if q9.upper() == "D":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is None of these\n")

# Question 10
check_time()
q10 = input("10. Which keyword is used to skip the current iteration in a loop?\nA) continue\nB) skip\nC) pass\nD) jump\n\nThe answer is: ")
if q10.upper() == "A":
    print("Correct.\n")
    score += 1
else:
    print("\nYour answer is wrong.\nThe correct answer is continue\n")

# Final Score
print("\n********************\n")
print("Your score is:", score ,"/ 10")
print("\n********************\n")