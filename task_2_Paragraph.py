import re

paragraph = input("Enter paragraph: ")

print("Do you want to edit or update any word in the paragraph")

x = input("Proceed (y/n)? ")

if x == "y" or x == "Y":
    word = input("Enter the word you want to replace: ")
    new_word = input("Enter the word you want to replace it with or keep it empty if you want to delete the word: ")
    if new_word == "":
       
        new_para = re.sub(word, "\b", paragraph, flags=re.IGNORECASE)
    else:
       
        new_para = re.sub(word, new_word, paragraph, flags=re.IGNORECASE)

    print(new_para)





