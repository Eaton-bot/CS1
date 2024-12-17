import time 
import datetime
    
while True:                                                                                                       #forever loop
    sleeping=str.lower(input("are you sleeping"))                                                                #storage user response in variable snooze and convert to lower case                                                                                                
    if sleeping == "y":                                                                                           # if sleeping yes 
        print("Mom wakes me up")
        current_time=datetime.datetime(2025, 2, 28, 6, 45)                                                         # current time and datetime
        print(current_time.strftime("%H:%M:%S"), end='\r')                                                          # print current time and date 
        break
    elif sleeping == "n":                                                                                         # user response no
        print ("wake up on my own!")                                                                               # print wake up on your own 
        break
    else:
        print("invalid response")                                                                                   # print invalid response 
    
while True:                                                                                                           #forever loop
    weather=str.lower(input("is it hot"))                                                                             #storage user response in variable snooze and convert to lower case 
    if weather == "y":                                                                                                 # if weather == y
        print("put shorts/short sleeves on")                                                                            # print put shorts sleeves on 
        break
    elif weather == "n":                                                                                               #user response no
        print ("put warm clothes on!")                                                                                 # print put warm clothes on  
        break
    else:
        print("invalid response")                                                                                       # else print invalid response 


while True:                                                                                                             # forever loop
    brekafast=str.lower(input("eat brekafast"))                                                                         # input eat breakfast 
    if brekafast == "y":                                                                                                 # if breakfast = y
        print("hurry and make breakfast")                                                                                 # print hurry and make me breakfast
        while True:                                                                                                        # forever loop
            mom=input("does mom make me breakfast y/n")                                                                     # input does mom make me breakfast y or n
            if mom == "yes":                                                                                                # if mom = y
                print("take longer and ask for a yummy breakfast")                                                           # print take longer and ask for yummy breakfast
                break
            elif mom == "n":                                                                                                  # elif mom=n
                print ("make my own simple breakfast!")                                                                        # print make my own simple breakfast
                break
            else:                                                                   
                print("invalid response")                                                                                       # else print invalid response 
        break
    elif brekafast == "n":                                                                                                      # elif breakfast = n
        print ("take longer getting ready")                                                                                     # print take longer to get ready
        break
    else:
        print("invalid response")                                                                                                # else print invalid response 

print ('pack my bag')                                                                                                            # print pack my bag 

while True:                                                                                                                       # forever loop 
    finished_homework = str.lower(input("homework finished?"))                                                                    # finished homework= input homework finished
    if finished_homework == "y":                                                                                                   # if finished homework = y then break
        print("go down stairs and wait for brekafast")                                                                              # print go down staris and wait for breakfast
        break
    elif finished_homework == "n":                                                                                                  # elif finished homework = n
        print ("quickly try and finish my homework!")                                                                               # print quickly try to finish homework break
        break
    else:
        print("invalid response")                                                                                                   # else print invalid response


while True:                                                                                                                         # forever loop
    go_on_phone = str.lower(input("be social"))                                                                                     # input be social 
    if  go_on_phone == "n":                                                                                                          # if go on phone is n
        print("go sit somewhere and chill on phone")                                                                                # print go sit somwhere and chill on phone
        break
    elif  go_on_phone == "y":                                                                                                        # elif go on phone = y
        print ("chill in kitchen and wait for breakfast!")                                                                           # print chill in kitchen and wait for breakfast
        break
    else:
        print("invalid response")                                                                                                   # else print invalid response 

print (' eat brekafast')                                                                                                            # print eat breakfast 
print (' put my shoes on')                                                                                                          # print put on my shoes 
print ('brush my teeth')                                                                                                            # print brush my teeth 
print ('get in the car')                                                                                                            # print get in the car 





        

