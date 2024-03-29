questions = [
{
"prompt" : "what is the Capital of India?",
"options" : ["A. Delhi", "B. Lucknow", "C. Bangalore", "D. Varanasi"],
"answer" : "A"
},
{
"prompt" : "How many bones does a human body has?",
"options" : ["A. 106", "B. 206", "C. 306", "D. 406"],
"answer" : "B"
},
{
"prompt" : "Who is the Prime Minister of India?",
"options" : ["A. Shri Yogi", "B. Dr Manmohan Singh", "C. Shri Modi", "D. Shri Chandra Shekhar"],
"answer" : "C"
},
{
"prompt" : "How many states are there in India?",
"options" : ["A. 27", "B. 28", "C. 29", "D. 30"],
"answer" : "B"
}
]

def quiz_game(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        ans = input("Please provide your answer amoung (A, B, C, D): ").upper()
        if ans == question["answer"]:
            score += 5
            print(f"You gave the correct answer and your score is {score}\n")
        else:
            print(f"You lost and your final score is {score}")
            break
    


ans = quiz_game(questions)
print(ans)