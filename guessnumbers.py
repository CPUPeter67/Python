import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score. It's your chance to set one!")
    else: 
        print("The current high score is {} attempts.".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 50))
    print("Hey there! Welcome to the Guess The Number game!")
    player_name = input ("Please enter your name.")
    wanna_play = input("Hi, {}, would you like to play? (Yes/No) ".format(player_name))
    ## Where the show_score function used to be
    Attempts = 0
    show_score()
    while wanna_play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 50")
            if int(guess) < 1 or int(guess) > 50:
                raise ValueError("The number must be between 1 and 50.")
            if int(guess) == random_number:
                print("Congrats! You guessed the number right!")
                attempts += 1
                attempts_lists.append(attempts)
                print("You guessed the number in {} attempts.".format(attempts))
                play_again = input("Would you like to play again? (Yes/No)")

                attempts = 0
                show_score()
                random_number = int(ranfom.randit(1, 50))
                if play_again.lower() == "no":
                    print("That's cool, {}. Have a nice day!")
                    break
            elif int(guess) < random_number:
                print("Too low!")
                attempts += 1
            elif int(guess) > random_number:
                print("Too high!")
                attempts += 1
        except ValueError as err:
            print("Oops! That is not a valid value. Try again.")
            print("({})".format(err))
    else:
        print("That's cool, {}. Have a nice day!")
if __name__ == "__main__":
    start_game()                
                         
