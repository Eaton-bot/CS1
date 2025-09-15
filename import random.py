import random
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
                12. return full-name as a sorted array of charicters
                13. build a menu 
                14 make initials from name
                15 return boolean if namecontains a title/distinction  ''')
            

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
                print(return_bolean_if_last_name_contains_a_hyphen(name))
            if selection == "8":
                print(convert_to_lowercase(name))
            if selection == "9":
                print(convert_to_lowercase(name))
            
            
def reverse_display(string):
     return string[::-1]
    

def determine_the_number_of_vowels(name):
   vowels = list['a','i','e','y','o','u','A','I','E','Y','O','U']
   vowel_count = 0
   for letter in name:
        if letter in vowels: 
            vowel_count +=1
        return vowel_count

    
def consonant_frequency(name):
    cons_count = 0
    ok = ['a','i','e','y','o','u','A','I','E','Y','O','U']
    for letter in name:
        if letter not in ok:
            cons_count +=1

    
    return cons_count
def first_name(name):
    parts = name.split(" ")

    name_1 = parts[0]

    return(name_1)

def last_name(name):
    parts = name.split("")

    name_2 = parts[2]

    return(name_2)
    
    
def middle_name(name):
    parts = name.split("")

    name_3 = parts[3]

    return(name_3)
def return_bolean_if_last_name_contains_a_hyphen(name):
   ''' 
   checks to see if name contaisn a hyphen 
   '''
   return '-' in name

def convert_to_lowercase(name):
    list_name = list (name)
    new_list_name = []
    for letter in list_name:
        int_value = ord(letter)
        if int_value< 90 and int_value > 64:
            new_int_value = int_value+32
            lower_letter = chr(new_int_value)
            new_list_name.append(lower_letter)
        else:
            already_lower_letter = chr(int_value)
            new_list_name.append(already_lower_letter)
        return("".join(new_list_name))
    
def cpnvert_to_uppercase(name):
    list_name = list (name)
    new_list_name = []
    for letter in list_name:
        int_value = ord(letter)
        if int_value< 97 and int_value > 122:
            new_int_value = int_value-32
            upper_letter = chr(new_int_value)
            upper_name = upper_name+upper_letter
        else:
           upper_name+upper_letter
    


main()