'''
Name: Eaton Holden
Date: 5/23/25
Description: password keeper that stores passwords, lets you input more, change them later, and more
Bugs: none
Challenges: Allow the user to retroactively add more usernames and passwords
Allow the user to change usernames and passwords
Store the list of websites with usernames and passwords in an excel spreadsheet
Generate a secure password for the user
Sources none 
'''

import random
import csv


def add_entry(websites, usernames, passwords):
    website = input ("pick a website: ")
    username = input("pick a username: ")
    password = input ("pick a password (press 'g' to generate): ")

    if password.lower() == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)

def get_index(websites):
    while True:
        website = input ("pick a website: ")

        if website in websites:
            return websites.index(website)
        else:
            print ("website is not here")

def print_entry(website, username, password):
    print(f'''
Website: {website}
Username: {username}
Password: {password}''')
    
def change_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites[index] = input('Enter new website: ')
    usernames[index] = input('Enter new username: ')
    passwords[index] = input('Enter new password: ')

def delete_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites.pop(index)
    usernames.pop(index)
    passwords.pop(index)

def export_to_csv(filename, headers, *arrays):
    '''
    Exports parallel arrays to a CSV file.

    Args:import csv
        filename (str): The name of the CSV file to create.
        headers (list): A list of header names for each column.
        *arrays: Variable number of array arguments (lists or tuples).
               All arrays must have the same length.
    '''
    if not arrays:
        raise ValueError("At least one array must be provided.")
    
    num_rows = len(arrays[0])

    for arr in arrays:
        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same length.")
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)

        for i in range(num_rows):
            row = [arr[i] for arr in arrays]
            csvwriter.writerow(row)

def get_password_length():
    '''
    '''
    while True:                                                                             
        
        try:                                                                              
            length = int(input("choose a passowd"))
            return length
        except ValueError:
            print("That's not an integer")
def generate_password():
    '''
    '''
    length = get_password_length()
    return ''.join(random.sample(list('abcABC0123'), length))
def main():
    websites = []
    usernames = []
    passwords = []
    
    add_entry(websites, usernames, passwords)

    while True: 
        option = input('''Which option do you want? Enter "q" to quit
1. Add an entry
2. Print an entry
3. Print all entries
4. Change an entry
5.
6. Check how many characters this password has
                ''').lower()
        
        if option == "q":
            break
        elif option == "1":
            add_entry(websites, usernames, passwords)
        elif option == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif option == "3":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif option == "4":
            change_entry(websites, usernames, passwords)
        elif option == "5":
            filename = input('Choose a filename: ')
            export_to_csv(filename + '.csv', ["Website", "Username", "Password"], websites, usernames, passwords)
            print(f'Export successful! Your file has been saved as {filename}.csv')
        elif option == "6":
            print(get_password_length())
        else:
            print('Invalid!')
main()