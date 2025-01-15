import random

import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
  display += "_"

lifeline = 6

end_of_game = False

print(f"{hangman_art.logo}\n")

print(display)

while not end_of_game:
  guess = input("Guess the word: ").lower()
  if guess in display:
    print(f"you have already guessed {guess}.")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  print(display)
  if guess not in chosen_word:
    print(f"you have chosen wrong input {guess}.")
    lifeline -= 1
    if lifeline == 0:
      end_of_game = True
      print("You loose.You Die.")

  print(f"{' '.join(display)}")

  if "_" not in display:
    end_of_game = True
    print("You win.")
  print(hangman_art.stages[lifeline])
