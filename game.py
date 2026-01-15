from game_logic import check_name

print("🎮 Welcome to the Guess My Name Game!")
print("Hint: My name has 6 letters")

guess = input("Enter your guess: ")

if check_name(guess):
    print("🎉 Correct! You guessed my name.")
else:
    print("❌ Wrong guess! Try again.")
