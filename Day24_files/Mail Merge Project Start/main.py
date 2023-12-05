#Todoo: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
 

with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day24_files\\Mail Merge Project Start\\Input\\Names\\invited_names.txt") as name:
    names = name.read()
    name_list = names.split("\n")
    

with open("C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day24_files\\Mail Merge Project Start\\Input\\Letters\\starting_letter.txt") as letter:
    s_letter = letter.read()
        
for name in name_list:
    with open(f"C:\\Users\\lenovo\\Documents\\pawandai\\100daysofpython\\Day24_files\\Mail Merge Project Start\\ReadToSend\\{name}.txt","w") as each_letter:
        new_letter = s_letter.replace("[name]",name)
        each_letter.write(new_letter)
