import random

# List of words and optional clues
words = {
    "python": "A programming language",
    "apple": "A fruit",
    "java": "Popular backend language",
    "coding": "What programmers do",
    "hangman": "This game itself"
}

# Choose a random word
word = random.choice(list(words.keys()))
clue = words[word]  # optional clue

# Initialize variables
guessed_letters = []
attempts = 6
display_word = ["_"] * len(word)

print("Welcome to Hangman!")
print("You have", attempts, "incorrect guesses allowed.")
print("Clue:", clue)  # optional, you can comment this line if you don't want clues

# Game loop
while attempts > 0 and "_" in display_word:
    print("\nWord:", " ".join(display_word))
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
        # Reveal all occurrences of guessed letter
        for i, letter in enumerate(word):
            if letter == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts remaining:", attempts)

# Check game result
if "_" not in display_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)
