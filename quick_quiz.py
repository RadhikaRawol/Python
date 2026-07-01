def quick_quiz():
    score = 0
    print("Welcome to the Quick Quiz!")
    print("Question 1: What is the capital of France?")
    print("A) London")
    print("B) Berlin")
    print("C) Paris")
    print("D) Madrid")
    answer1 = input("Your answer (A/B/C/D): ")
    if answer1 == "C":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    print("Question 2: What is the largest planet in our solar system?")
    print("A) Earth")
    print("B) Jupiter")
    print("C) Saturn")
    print("D) Uranus")
    answer2 = input("Your answer (A/B/C/D): ")
    if answer2 == "B":
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")

    print(f"Your final score is: {score}/2")