import random

def play_game():
    words = ["python", "programming", "code", "miracle"]

    print("Welcome to the Field of Miracles game!")

    num_players = int(input("Enter number of players (2-4): "))

    if num_players < 2 or num_players > 4:
        print("Number of players must be between 2 and 4")
        exit()

    # Select random word
    word = random.choice(words)

    hidden_word = "*" * len(word)

    print(hidden_word)

    current_player = 1
    guessed_letters = []

    while hidden_word != word:
        print(f"\nPlayer {current_player}'s turn:")

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        if guess in word:
            print("Congratulations! Guess another letter.")
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word = hidden_word[:i] + guess + hidden_word[i + 1:]
        else:
            print(f"Sorry, '{guess}' is not in the word. Next player's turn.")
            current_player += 1
            if current_player > num_players:
                current_player = 1

        guessed_letters.append(guess)
        print(hidden_word)
    return print(f"\nPlayer {current_player} wins! The word was {word}.")

while (True):
    play_game()
