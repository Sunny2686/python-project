import json
import difflib

data = json.load(open("data.json"))

def translate(word):
    
    word = word.lower()
    if word in data:
        print('Available definations: ' + '\n' )
        for i,line in enumerate(data[word], start=1):
            print('{}.{}'.format(i, line))
        return
    elif len(difflib.get_close_matches(word, data.keys(), cutoff=0.85)) > 0:
        print(difflib.get_close_matches(word, data.keys(), cutoff=0.85))
        yes_no_input = input(f'Did you mean "{difflib.get_close_matches(word, data.keys(), cutoff=0.85)[0]}" "yes/y" or "no/n"? ')
        if yes_no_input.lower() in ['yes', 'y','ye']:
            #Calling function recursively
            translate("{}".format(difflib.get_close_matches(word, data.keys(), cutoff=0.85)[0]))
        elif yes_no_input.lower() in ['no', 'n'] :  
            print('Please double check your entery.')
            return
        else:
            print(f'Dictonary does not understand the word "{word}"') 
            
    else:
        if int(word) or float(word):
            print('Please enter the correct word.')
        else:
            print(f'Word "{word}" not found in dictonary.')


user_search = input('Enter the word to search = ')
translate(user_search)