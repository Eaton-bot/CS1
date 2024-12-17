import random                                                       #random import

name = input("what is your name? ")                                    #asks player 
print('Good luck', name)                                                # print good luck
rounds = 0                                                              # set computer number to random 1-10
correct = 0                                                             # set correct to 0 and rounds to 0 while guesses set to 0
while True:                                                             # forever loop
    guesses = 5                                                         # guesses set to 0 
    comp_number= random.randint(1, 10)                                  # set computer number 1-10                                                  # print comp number 

    while guesses > 0:                                                  #while guesses set to 0 
        while True:                                                      # forever loop 
            guess_number = input('Guess a number 1 - 10')                 # player guesses number that computer chooses 1-10

            try:
                guess_number = int(guess_number)                           # attempts to convert guess to an integer 

                if guess_number >= 1 and guess_number <= 10:                # if player guess is less than 1 or greater than break 10
                    break
                else:
                    print ("enter a # between 1 - 10")                      #print enter a number between 1-10  
            except ValueError:
                print('Please enter a number')                               # print please enter a number                               

        if guess_number == comp_number:                                       # if guess=number
            print ("you got it")                                               # print you got this
            correct += 1                                                        # add 1 correct
            break
        elif guess_number > comp_number:                                         # eliff guess > number 
            print("your number is too high")                                      # print your number is too high 
        else:
            print("your number is too low")                                        # print your number is too high 
        
        guesses -= 1                                                                # guesses -=1 

    if guesses == 0:                                                                # if guesses are 0 
        print('you lost this round')                                                 # print you lost this round 
    rounds += 1                                                                       # add 1 to rounds 

    while True:                                                                        # forever loop 
        play_again = input(f"You have gotten {correct} correct out of {rounds}. Would you like to play again? y/n: ") # asking play again input name says how many you got right and out of rounds would you like to play again y or n 

        if play_again == "n":                                                           # if play again is n
            exit()                                                                      # then you exit 
        elif play_again == "y":                                                          # elif play again y
            break                                                                        # break 
        else:
            print("invalid response")                                                     # PRINT invalid response 
    


    
