import random
user_score=0
comp_score=0
print ("welcome to the rock paper scissors challenge")
RPS = ["rock", "paper", "scissors"]
 # generate a random element from thislist 
while True:
    comp_weopon = random.choice(RPS)
# computer picks rock paper or scissors
    user_weopon = input("choose Rock, Paper, Scissors")
# user picks rock paper scissors
    print(comp_weopon,user_weopon)
#
    if comp_weopon == user_weopon:
        print ("tie")
# if they are the same it is a tie
    elif comp_weopon == 'rock' and user_weopon == 'paper':
#user wins the round 
        print ("user wins")
        user_score +=1
#users score is plus one
        print(''' 
  _    _                __          ___           
 | |  | |               \ \        / (_)          
 | |  | |___  ___ _ __   \ \  /\  / / _ _ __  ___ 
 | |  | / __|/ _ \ '__|   \ \/  \/ / | | '_ \/ __|
 | |__| \__ \  __/ |       \  /\  /  | | | | \__ \
  \____/|___/\___|_|        \/  \/   |_|_| |_|___/
                                                  
                                                  
    ''')
    elif comp_weopon == 'rock' and user_weopon == 'scissors':
#if they come up computer wins 
        print ("computer wins")
        comp_score +=1
# computer adds 1 to their score
                                                   
        print ('''                                     
   ___ ___  _ __ ___  _ __   __      ___ _ __  ]
  / __/ _ \| '_ ` _ \| '_ \  \ \ /\ / / | '_ \ 
 | (_| (_) | | | | | | |_) |  \ V  V /| | | | |
  \___\___/|_| |_| |_| .__/    \_/\_/ |_|_| |_|
                     | |                       
                     |_|                       
      ''') 
    elif comp_weopon == 'scissors' and user_weopon == 'paper':
#computer chooses scissors and user chooses paper
        print ("computer wins")
        comp_score +=1
#computer wins and add one to their score 
                                                   
        print ('''                                     
   ___ ___  _ __ ___  _ __   __      ___ _ __  
  / __/ _ \| '_ ` _ \| '_ \  \ \ /\ / / | '_ \ 
 | (_| (_) | | | | | | |_) |  \ V  V /| | | | |
  \___\___/|_| |_| |_| .__/    \_/\_/ |_|_| |_|
                     | |                       
                     |_|                       
      ''') 
    elif comp_weopon == 'scissors' and user_weopon == 'rock':
#computer chooses scissors and user chooses rock    
        print ("user wins")
        user_score +=1
#user wins and adds one to their 
        print(''' 
  _    _                __          ___           
 | |  | |               \ \        / (_)          
 | |  | |___  ___ _ __   \ \  /\  / / _ _ __  ___ 
 | |  | / __|/ _ \ '__|   \ \/  \/ / | | '_ \/ __|
 | |__| \__ \  __/ |       \  /\  /  | | | | \__ \
  \____/|___/\___|_|        \/  \/   |_|_| |_|___/
                                                  
                                                  
    ''')
    elif comp_weopon == 'paper' and user_weopon == 'scissors':
#computer chooses paper and user chooses scissors
        print ("computer wins")
        comp_score +=1
# computer wins and adds one to their score
                                                   
        print ('''                                     
   ___ ___  _ __ ___  _ __   __      ___ _ __  
  / __/ _ \| '_ ` _ \| '_ \  \ \ /\ / / | '_ \ 
 | (_| (_) | | | | | | |_) |  \ V  V /| | | | |
  \___\___/|_| |_| |_| .__/    \_/\_/ |_|_| |_|
                     | |                       
                     |_|                       
      ''') 
    elif comp_weopon == 'paper' and user_weopon == 'rock':
#computer chooses paper and user chooses rock 
        print ("user wins")
        user_score +=1
#user wins and adds one to their score
        print(''' 
  _    _                __          ___           
 | |  | |               \ \        / (_)          
 | |  | |___  ___ _ __   \ \  /\  / / _ _ __  ___ 
 | |  | / __|/ _ \ '__|   \ \/  \/ / | | '_ \/ __|
 | |__| \__ \  __/ |       \  /\  /  | | | | \__ \
  \____/|___/\___|_|        \/  \/   |_|_| |_|___/
                                                  
                                                  
    ''')
    else:
        print("invalid response")
    print (user_score,comp_score)
# prints the score of the game 



                                              
    print ('''                                     
   ___ ___  _ __ ___  _ __   __      ___ _ __  
  / __/ _ \| '_ ` _ \| '_ \  \ \ /\ / / | '_ \ 
 | (_| (_) | | | | | | |_) |  \ V  V /| | | | |
  \___\___/|_| |_| |_| .__/    \_/\_/ |_|_| |_|
                     | |                       
                     |_|                       
      ''') 

  
