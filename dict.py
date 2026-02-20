import string
import matplotlib.pyplot as plt
import numpy as np

def add_file(name_of_file):
    try:
        with open (name_of_file, 'r') as file:
            counts = dict()
            
            for line in file:
                line = line.translate(line.maketrans("","", string.punctuation))
                line = line.lower()
                words = line.split()
                
                for word in words:
                    if word not in counts:
                        counts[word] = 1
                    else:
                        counts[word] += 1
                    
        data_sorted = {k: v for k, v in sorted(counts.items(),key=lambda item: item[1], reverse=True)}
        remove_words = ['it','in','to','a','my','the','like','is','you','than','that','of','he','she','they','their','not','his','your','lord','me','for','have','be','i','and','to'] 
        
        for word in remove_words:
            if word in data_sorted:
                del data_sorted[word]
        
        final_dict = dict()
        count = 0
        limit = 15
        
        for key, value in data_sorted.items():
            if count < limit:
                final_dict.update(({key: value}))
                count += 1 
            else:
                break
        

        data = []
        labels = []
        for key, value in final_dict.items():
            labels.append(key)
            data.append(value)
        plt.pie(data,labels = labels)
        plt.title('biggest words in text',)
        plt.show()

    except FileNotFoundError:
        print('file not found')

def main():
    choice = input("Do you want all is well and ends well, or Anthony and cleopatra")
    if choice == '1':
        (add_file("well.txt"))
    elif choice == "2":
        (add_file("ac.txt"))
main()

