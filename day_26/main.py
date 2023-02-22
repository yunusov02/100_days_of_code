import pandas

WAY_TO_DATA = "D://100_days_of_code//day_26//nato_phonetic_alphabet.csv"

data = pandas.read_csv(WAY_TO_DATA)

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

def generate():
    word = input("Enter a word: ").upper()
    try:
        output_word = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate()
    else:
        print(*output_word)
    
generate()
