'''
Auther_Eaton Holden
Date 9/15/2025
Bugs doesn't do all titles limited number of titles - comments go above the code - 
sources Mr Campbell, Ms Marciano
'''
import random

def reverse_display(string):
     return string[::-1]
'''
reverses the name prints it backwords 
args: 
    name (str): original name input
returns 
    name backwords
'''

def determine_the_number_of_vowels(name):
    vowels = ['a','i','e','y','o','u','A','I','E','Y','O','U']
    vowel_count = 0

    for letter in name:
        if letter in vowels: 
            vowel_count += 1
    return vowel_count
'''
   determine the number of vowels in the name 
   Args: 
    name (str): original name input
   return: 
    the vowel count 
   '''
def consonant_frequency(name):
    ok = ['a','i','e','y','o','u','A','I','E','Y','O','U']
    cons_count = 0

    for letter in name:
        if letter not in ok:
            cons_count += 1
    return cons_count
'''
determine the number of consonants in the name
args: name (str): original name input  
returns: the number of consonants 
'''
def first_name(name):
    parts = name.split(" ")
    return parts[0]
'''
determines the first name in a persons name
args: name (str): original name input
returns: the first name
'''

def last_name(name):
    parts = name.split(" ")
    return parts[-1]    
'''
determines the last name in a persons name
args: name (str): original name input
returns: the last name
'''
def middle_name(name):
    parts = name.split(" ")
    return ' '.join(parts[1:-1])
'''
determines the middle name in a persons name
args: name (str): original name input
returns: the middle name
'''

def return_last_name_if_contain_hyphen(name):
   '''
   check to see if it contians a hyphen
   args: name (str): original name input
   returns: hyphen in name
   '''
   return '-' in name

def convert_to_lowercase(name):
    new_name = ''

    for letter in name:
        int_value = ord(letter)

        if int_value < 91 and int_value > 64: 
            int_value += 32
            lower_letter = chr(int_value)
            new_name += lower_letter
        else:
            new_name += letter
    
    return new_name

'''
convert uppercase letter to lowercase 
args: name (str): original name input
returns: same name but all in lowercase
'''
    
def convert_to_uppercase(name):
    new_name = ''

    for letter in name:
        int_value = ord(letter)

        if int_value < 123 and int_value > 96: 
            int_value -= 32
            upper_letter = chr(int_value)
            new_name += upper_letter
        else:
            new_name += letter
    return new_name
    
    
'''
    if int_value< 97 and int_value > 122:
            new_int_value = int_value-32
    '''
        
def modify_array_to_create_a_random_name(name):
    name = list(name)
    random.shuffle(name)
    return ''.join(name)
'''
modifies array to create a random name
args: name (str): original name input
returns names to create one long random name
'''

def return_boolean_if_first_name_is_a_palindrome(name):
    '''
    SUGGESTION: CHANGE FUNCTION NAME TO BE SHORTER
    '''
    return convert_to_lowercase(name) == reverse_display(name)

def return_name(name):
    
    order = ''
    real_name = name.replace(' ',' ')
    chars = list(real_name)
    sorted_chars = sorted(chars)
    order = order = sorted_chars
    return (order)

def get_initials(name):
    initials = ''
    names = name.split(' ')

    for n in names:
        initials += n[0]

    return initials

def main():
    while True:
        name = input("what is your name: ")
        while True:
            selection=input('''
                1. reverse and display
                2. determine the number of vowels
                3. consonant frequency 
                4. return first name
                5. return last name
                6. return middle names
                7. return boolean if last name contains a hyphen
                8. function to convert to lowercase 
                9. function to convert to uppercase
                10. modify array to create a random name 
                11. return boolean if first name is a palindrome
                12. get initials
                            ''')
            

            if selection == "1":
                print(reverse_display(name))
            if selection == "2":
             print(determine_the_number_of_vowels(name))
            if selection == "3":
                print(consonant_frequency(name))
            if selection == "4":
                print(first_name(name))
            if selection == "5":
                print(last_name(name))
            if selection == "6":
                print(middle_name(name))
            if selection == "7":
                print(return_last_name_if_contain_hyphen(name))
            if selection == "8":
                print(convert_to_lowercase(name))
            if selection == "9":
                print(convert_to_uppercase(name))
            if selection =="10":
                print(modify_array_to_create_a_random_name(name))
            if selection =="11":
                print(return_boolean_if_first_name_is_a_palindrome(name))
            if selection == "12":
                print(get_initials(name))
            
            

main()