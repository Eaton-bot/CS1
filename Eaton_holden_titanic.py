def display_10(file):
    line_count=0
           
        #header = file.readline().strip().split(',')  # Read the header row
        #name_index = header.index('Name')  # Find the index of 'Name' column
       
    for line in file:
        row = line.strip().split(',')
        print(row)
    #print(row[name_index])
    # except FileNotFoundError:

def survival_rate(file):
    survivors = 0
    total_people = 0 
    for line in file:
            row = line.strip().split(',')
            total_people += 1
            if row [1] == '1':
                survivors += 1
    survival_percent = survivors/total_people
    print (f"survival percent: {survival_percent*100}%")

def gender_survival_rate(file):
    file.seek(1)
    for line in file:
        row = line.strip().split(',')
        male = 0
        female = 0
        male_s = 0
        female_s = 0
        if row [5] == "male":
            male += 1
            if row[1] == "1":
                male_s += 1
        elif row[5] == "female":
            female += 1
            if row[1] == "1":
                female_s+= 1
        msr = male_s/male
        fsr = female_s/female
        print (f"male survival rate{msr*100}")
        print (f"female survival rate{fsr*100}")
     
def average_age(file):
    file.seek(1)
    with open('titanic.csv', 'r') as file:
        totalppl = 0
        totalage = 0
        for line in file:
            row = line.strip().split(',')
            totalppl += 1
            totalage += len(row[6])
            

def youngest_age():
    youngest_age = 200

    with open('titanic.csv','r') as file:
        youngest_age = 100
        for line in file:
            row = line.strip().split(',')
            try:
                age = float(row [6])
                if age < youngest_age:
                    youngest_age = age
            except ValueError:
                pass
    print(youngest_age)

def oldest_age(file):
    oldest_age = 0
    with open ('oldest_person.csv','w') as oldest_person_file:
        oldest_age = 100
        for line in file:
            row = line.strip().split(',')
            try:
                age = int(row [6])
                if age < oldest_age:
                    oldest_age = age
            except ValueError:
                pass
            
            oldest_person_file.write('Youngest Age:,')
            oldest_person_file.write(f'{youngest_age}')

def average_age_of_survivors_v_nonsurvivors(file):
    male_s = 0
    male = 0
    female_s = 0
    female = 0

    file.seek(1)

    for line in file:
        row = line.strip().split(',')
        total_age = 0
        if row[1] == "1":
            total_age += float(row[6])
        if row[1] == "0":
            survi+= 1
        msr = male_s/male
        fsr = female_s/female
        print (f"male survival rate{msr*100}")
        print (f"female survival rate{fsr*100}")


def age_statistics(data):
    header = data(0)
    age_index = header.index("age")
    survival_index = header.index("survival")
    ages = []
    survival_ages = []
    not_survived_ages = []

    for row in data[1]:
        age = row[age_index]


    if age == "" or age.lower() == "nan":
        age = float(age)
        ages.append(age)

    if row[survival_index] == "1":
        survival_ages.append(age)
    else:
        not_survived_ages.append(age)
        
   
    overall_avg = sum(ages) / len(ages) if ages else 0
    survived_avg = sum(ages) / len(ages) if ages else 0 

    print(overall_avg)
    print(survived_avg)



def read_csv_manual(file):
    data = []
    filename = 0
    with open(filename, 'r') as file:
        for line in file:
            row = []
            current = ""
            inside_quotes = False

        for ch in line.strip():
            if ch == '"':
                inside_quotes = not inside_quotes
            elif ch == ',' and not inside_quotes:
                row.append(current)
            current = ""
        else:
            current += ch
        row.append(current)
        row.append(row)


def class_analysis(file):
    file.seek(1)
    first_class = 0
    second_class = 0
    third_class = 0
    first_class_survived = 0
    second_class_surviced = 0
    third_class_survived = 0




    


def main():
    with open('titanic.csv', 'r') as file:
        options = input("""what do you want this to do
         1 survival rate      
         2 youngest passenger
        """)
        
        if options == '1':
             survival_rate(file)
        elif options == '2':
            youngest_age()
        elif options == '3':
            gender_survival_rate
        elif options == '4':
            average_age(file)
        elif options == '5':
            oldest_age(file)
        elif options == '6':
            average_age_of_survivors_v_nonsurvivors(file)
        elif options == '6':
            read_csv_manual(file)
        elif options == '7':
            age_statistics(file)

        
main()
             



    