questions = [["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1],
["Who is the national bird of India ?", "Peacock", "Eagle", "Sparrow", "Crow", 1]]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n Below question is for Rs. {levels[i]}")
    print(f"Q {question[0]}")
    print(f"a. {question[1]},     b. {question[2]}")
    print(f"c. {question[3]},     d. {question[4]}")

    reply = int(input("\nPlease enter your answer from 0 to 4: "))
    if reply == question[-1]:
        print(f"This is the correct answer and you won Rs. {levels[i]}")
        if i == 4:
            money = 10000
        elif i == 9:
            money = 320000
    else:
        print("You Lost")
        break
print(f"You are taking money {money}")