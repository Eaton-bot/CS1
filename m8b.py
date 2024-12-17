import random
print("hello human I am the Magic 8 ball")                                      # print hello human I am the Magic 8 Ball
responses = ["yes", "no", "maybe", "ask again later"]                           # create a list called responses yes no maybe ask again later 
question_words =  ["am", "will", "is", "are", "how", "where", "who" "what" "whom" "whose" "which" "when"]            # create a list of question words 

while True:                                                                      # forever loop 
    question = input("ask any question: ")                                        # set question to user input ask any question enter stop to end
    first_word = question.split()[0]                                              # set first word to the first word of question

    if question == "stop":                                                         # if question == stop break 
        break 
    elif "?" in question and first_word in question_words:                         # else in question and first word is in question words
	display: a random response from responses

        print(random.choice(responses))                                            # generate a random elemenent from a list
    else:
        print("That is not a question")                                             # else that is not a question 
