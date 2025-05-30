import random                                                  
def chorus():
    '''
    sings a song
    Args:
        none
    returns:
        the entire song sung
    '''                                                
    print('''                                                    
Pour some sugar on me
Ooh, in the name of love
Pour some sugar on me
C'mon, fire me up
Pour your sugar on me
I can't get enough
    ''')                                                        
def sing_song():
    '''
    use chorus function to sing entire song
    Args: 
        none
    returns:
        print: entire song
    '''
    print('''
Step inside
Walk this way
You and me babe
Hey hey
Love is like a bomb, baby, c'mon get it on
Livin' like a lover with a radar phone
Lookin' like a tramp, like a video vamp
Demolition woman, can I be your man? (your man)
Razzle 'n' a dazzle 'n' a flash a little light
Television lover, baby, go all night
Sometime, anytime, sugar me sweet
Little miss innocent sugar me, yeah, yeah
Now c'mon, take a bottle, shake it up
Break the bubble, break it up
    ''')                                                            
    chorus()
    print('''
          I'm hot, sticky sweet
From my head to my feet, yeah
Listen, red light, yellow light, green-a-light go
Crazy little woman in a one man show
Mirror queen, mannequine, rhythm of love
Sweet dream, saccharine, loosen up (loosen up)
Loosen up
You gotta squeeze a little, squeeze a little
Tease a little more
Easy operator come a knockin' on my door
Sometime, anytime, sugar me sweet
Little miss innocent sugar me, yeah, yeah
Give a little more
Take a bottle, shake it up
Break the bubble, break it up
          ''')                                                        
    chorus()
    print('''
       I'm hot, sticky sweet
From my head to my feet, yeah
You got the peaches, I got the cream
Sweet to taste, saccharine
'Cause I'm hot (hot), say what, sticky sweet
From my head (head), my head, to my feet
Do you take sugar? One lump or two?
Take a bottle (take a bottle), shake it up (shake it up)
Break the bubble (break it up), break it up   
          ''')                                                         
    chorus()                                                          
    chorus()                                                           
def add(a, b):
    '''
    takes two numbers and adds them together
    Args:
        a = (int): first number
        b = (int): second number
    '''                                                  
    print(a + b)                                                      
def print_list(array):  
    '''
    takes a list and prints every element in that list indivdually (vertically)
    Args: 
        array = the list printed
    returns:
        print: list vertically
    '''                                              
    for element in array:                                             
        print(element)                                                 
def in_list(array, element):
    '''
    takes a list and element and returns a boolean based on if the element is in the list
    Args:
        array = the list checked
        element = the individual number in the list
    returns:
        boolean value based on if it is the list
    '''                                       
    return element in array                                            
def is_integer(number):
    '''
    Takes any parameter and returns a boolean based on if it is an integer
    Args:
        number = number that is checked to be an integer
    returns:
        boolean value based on if it is an integer
    '''                                               
    try:                                                               
        int(number)                                                    
        return True                                                    
    except ValueError:                                                 
        return False
def get_integers():
    '''
    asks the user for two numbers, uses is_integer to check input, returns the two integers
    Args:
        none
    '''
    while True:
        number_1 = input("give me one integer")
        number_2 = input ("give me anouther integer")

        if is_integer(number_1) and is_integer(number_2):
            return int(number_1), int(number_2)
def get_random():
    number_1, number_2 = get_integers()
    print(random.randint(number_1, number_2))
def count_vowels(string):
    count = 0 
    for character in string:
        if character in ['a','b','c']:
            count += 1
    return count 
def reverse_string(string):
    return string[::-1]
def main():
    while True:
        option = input('What would you like to do? 1. Sing a song, 2. Add two numbers, 3. Print a list, 4. Check if something in list...')
        
        if option == '1':
            sing_song()
        elif option == '2':
            a, b = get_integers()
            add(a, b)
        elif option == '3':
            user_list = input('Enter a list of items, separate items by spaces: ').split(' ')
            print_list(user_list)
        elif option == '4':
            user_list = input('Enter a list of items, separate items by spaces: ').split(' ')
            check = input('What would you like to check for? ')
            print(in_list(user_list, check))
        elif option == '5':
            get_random()
        elif option == '6':
            word = input('Enter word: ')
            print(count_vowels(word))
main()
