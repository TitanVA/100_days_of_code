# Create a letter using starting_letter.docx
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"
names_list = []
with open("Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip("\n")
        names_list.append(name)


def change_name(l_names):
    for n in l_names:
        with open(f"./Output/ReadyToSend/letter_for_{n}.docx", "w"):
            pass
        with open("Input/Letters/starting_letter.docx") as starting_letter:
            letter = starting_letter.read()
            new_letter = letter.replace(PLACEHOLDER, n)
            with open(f"./Output/ReadyToSend/letter_for_{n}.docx", "a") as out_letter:
                out_letter.write(new_letter)


change_name(names_list)