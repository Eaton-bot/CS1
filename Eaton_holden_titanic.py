def display_10(file):
    count=0
    for line in file:
            if count > 10:
                break
            else:
                print(line)
                count = count + 1
        
def t_passangers(file):
    count = 0
    for line in file:
        count = count+1
    print(count)
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
    
    male = 0
    female = 0
    male_s = 0
    female_s = 0
    for line in file:
        row = line.strip().split(',')
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
    print (f"male survival rate {msr*100}%")
    print (f"female survival rate {fsr*100}%")
     
def average_age(file):
    file.seek(1)
    with open('titanic.csv', 'r') as file:
        totalppl = 0
        totalage = 0
        for line in file:
            row = line.strip().split(',')
            try:
                totalppl = totalppl + 1
                totalage = totalage + int(row[6])
            except ValueError:
                pass
    print(totalage/totalppl)
            

def youngest_age(file):
    youngest_age = 200

    with open('titanic.csv','r') as file:
        youngest_age = 100
        for line in file:
            row = line.strip().split(',')
            try:
                age = int(row [6])
                if age < youngest_age:
                    youngest_age = age
            except ValueError:
                pass
    print(youngest_age)

def oldest_age(file):
    oldest_age = 0
    with open('titanic.csv','r') as file:
        oldest_age = 0
        for line in file:
            row = line.strip().split(',')
            try:
                age = int(row[6])
                if age > oldest_age:
                    oldest_age = age
            except ValueError:
                pass
    print(oldest_age)

def average_age_of_survivors_v_nonsurvivors(file):
    s = 0
    s_age = 0
    ns = 0
    ns_age = 0

    file.seek(1)

    for line in file:
        row = line.strip().split(',')
        try:
            if row[1] == "1":
                s=+1
                s_age += int(row[6])
            elif row[1] == "0":
                ns += 1
                ns_age += int(row[6])
        except ValueError:
            pass
    av_age_s = s_age/s
    av_age_ns = ns_age/ns
    print (f"survivor survival age{av_age_s}")
    print (f"nonsurvivor survival age{av_age_ns}")


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
    first_class_fare = 0
    second_class_fare = 0
    third_class_fare = 0
    with open ('titanic.csv','r') as file:
        
        for line in file:
            try:
                row = line.strip().split(',')
                pclass = row[2]
                if pclass == "1":
                    first_class += 1
                    first_class_fare += float(row[10])
                    if row[1] == "1":
                        first_class_survived += 1
                elif pclass == "2":  
                    second_class += 2
                    second_class_fare += float(row[10])
                    if row[1] == "1":
                        second_class_surviced += 1
                elif pclass == "3":
                    third_class += 3
                    third_class_fare += float(row[10])
                    if row[1] == "1":
                        third_class_survived += 1
            except ValueError:
                pass
        
        fcsr = first_class_survived/first_class
        scsr = second_class_surviced/second_class
        tcsr = third_class_survived/third_class
        fcf = first_class_fare/first_class
        scf = second_class_fare/second_class
        tcf = third_class_fare/third_class
        print (f"first class survival rate{fcsr*100}")
        print (f"second class survival rate{scsr*100}")
        print (f"third class survival rate{tcsr*100}")
        print(f"first class average fare: {fcf}")
        print (f"second class average fare: {scf}")
        print (f"third class average fare: {tcf}")


def average_fare(file):
    people = 0
    fare = 0
    with open ('titanic.csv','r') as file:
        
        for line in file:
            try:
                row = line.strip().split(',')
                people += 1
                fare += float(row[10])
            except ValueError:
                pass
    average_fare = fare/people
    print (f"average fare{average_fare}")


    


def main():
    with open('titanic.csv', 'r') as file:
        options = input("""what do you want this to do
         1 survival rate      
         2 youngest passenger
         3 gender survival rate
         4 average age
         5 oldest age
         6 average age of survivors vs non surviviors
         7 age statistics
         8 display file
         9 total passangers
         10 youngest age
         11 class analysis
         12 average fare
        """)
        
        if options == '1':
             survival_rate(file)
        elif options == '2':
            youngest_age()
        elif options == '3':
            gender_survival_rate(file)
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
        elif options == '8':
            display_10(file)
        elif options == '9':
            t_passangers(file)
        elif options == '10':
            youngest_age(file)
        elif options == '11':
            class_analysis(file)
        elif options == '12':
            average_fare(file)

        
main()
             



    