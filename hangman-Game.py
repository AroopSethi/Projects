import random
## Hangman
words = ["python", "java", "jenkins", "swift", "stack"]

choose_word = random.choice(words)
word = ["_" for _ in choose_word]
attemps = 8

print("Welcome to Hangman")

while attemps > 0 and "_" in word:
    print("\n" + " ".join(word))
    guess = input("Guess a letter: ").lower()
    if guess in choose_word:
        for index, letter in enumerate(choose_word):
            if letter == guess:
                word[index] = guess
    else:
        print("Wrong selection of word, idiot!!")
        attemps -=1

if "_" not in word:
    print("you guessed the word")
    print(" ".join(word))
else:
    print(f"you ran out of attempts, the word was {choose_word}")
    print("you lost")
