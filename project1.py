import random
word_list = ["apple", "train", "house", "light", "mouse"]
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts_left > 0 and "_" in display_word:
    print("Word: " + " ".join(display_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

 
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
        print("Good guess!\n")
    else:
        attempts_left -= 1
        print("Wrong guess.\n")


if "_" not in display_word:
    print("Congratulations! You guessed the word:", secret_word)
else:
    print("Sorry, you've run out of attempts. The word was:", secret_word)