import random

# List of predefined words
word_list = ["apple", "banana", "cherry", "orange", "grape"]
# Function to choose a random word from the list
def choose_word():
    return random.choice(word_list)
# Function to initialize the game
def hangman():
    # Select a random word
    word = choose_word()
    # Initialize variables
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word. It could be a fruit!")

    # Main game loop
    while incorrect_guesses < max_attempts:
        # Display current progress (underscores for unguessed letters)
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print(f"Word: {display_word}")

        # Prompt for a guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        # Add the guessed letter to the list
        guessed_letters.append(guess)

        # Check if the guess is correct
        if guess in word:
            print("Correct!")
        else:
            print("Incorrect!")
            incorrect_guesses += 1

        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word '{word}' correctly.")
            break

    # If out of guesses, display the word
    if incorrect_guesses == max_attempts:
        print(f"Sorry, you're out of guesses. The word was '{word}'.")


# Start the game
hangman()
