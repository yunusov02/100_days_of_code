#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



# INPUTS

# To add  letter text
with open("D://100_days_of_code//day_24//mail_merge_project//Input//Letters//starting_letter.txt") as letter:
    letter_text = letter.read()

first_index = letter_text.index("[")
second_index = letter_text.index("]")

# To add names
with open("D://100_days_of_code//day_24//mail_merge_project//Input//Names//invited_names.txt") as name:
    names = name.read().split()


#  OUTPUTS
for n in names:
    with open(f"D://100_days_of_code//day_24//mail_merge_project//Ouput//ReadyToSend//{n}.txt", mode="w") as ouput:
        ouput.write(letter_text[:first_index]+n+letter_text[second_index+1:])
    
