import time

def quiz_game():
    score = 0

    questions = [
        {
            "question": "What is the capital of Bangladesh?",
            "options": ["A. Chittagong", "B. Dhaka", "C. Khulna", "D. Rajshahi"],
            "answer": "B"
        },
        {
            "question": "Which language is used for web development?",
            "options": ["A. Python", "B. HTML", "C. Java", "D. All of these"],
            "answer": "D"
        },
        {
            "question": "What is 5 + 3?",
            "options": ["A. 5", "B. 8", "C. 10", "D. 15"],
            "answer": "B"
        }
    ]

    while True:
        print("\n=== Quiz Menu ===")
        print("1. Play Quiz")
        print("2. Add Question")
        print("3. Remove Question")
        print("4. Show Questions")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            # ---------- Play Quiz ----------
            score = 0
            total_time = 30  # total quiz time in seconds
            start_time = time.time()

            for q in questions:
                elapsed = int(time.time() - start_time)
                remaining_time = total_time - elapsed

                if remaining_time <= 0:
                    print("\nTime's up!")
                    break

                print(f"\nTime Remaining: {remaining_time} seconds")
                print(q["question"])
                for option in q["options"]:
                    print(option)

                user_answer = input("Your answer (A/B/C/D): ").upper()
                if user_answer == q["answer"]:
                    print("Correct!")
                    score += 1
                else:
                    print(f"Wrong! Correct answer is {q['answer']}")

            print(f"\nQuiz Finished! Your Score: {score}/{len(questions)}")

        elif choice == "2":
            # ---------- Add Question ----------
            question = input("Enter the question: ")
            options = []
            options.append("A. " + input("Option A: "))
            options.append("B. " + input("Option B: "))
            options.append("C. " + input("Option C: "))
            options.append("D. " + input("Option D: "))
            answer = input("Correct answer (A/B/C/D): ").upper()

            questions.append({
                "question": question,
                "options": options,
                "answer": answer
            })
            print("Question added successfully!")

        elif choice == "3":
            # ---------- Remove Question ----------
            if not questions:
                print("No questions to remove!")
                continue

            print("\nCurrent Questions:")
            for i, q in enumerate(questions):
                print(f"{i + 1}. {q['question']}")

            index = int(input("Enter question number to remove: ")) - 1
            if 0 <= index < len(questions):
                removed = questions.pop(index)
                print(f"Removed question: {removed['question']}")
            else:
                print("Invalid number!")

        elif choice == "4":
            # ---------- Show Questions ----------
            if not questions:
                print("No questions available!")
            else:
                print("\nAll Questions:")
                for i, q in enumerate(questions):
                    print(f"{i + 1}. {q['question']} (Answer: {q['answer']})")

        elif choice == "5":
            print("Exiting Quiz. Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1-5.")


quiz_game()
