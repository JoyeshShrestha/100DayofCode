# names =["Joyesh","Sau","Bishale","Deshne","RijuBhai"]
# import random
# student_scores = {student:random.randint(1,100) for student in names}
# print(student_scores)

# passed_students = {student for student,marks in student_scores.items() if marks>60}

# print(f"Passed Student: {passed_students}")

#NO. 2 
# sentence = input().split(" ")

# all_letters = {word:len(word) for word in sentence}
# print(all_letters)
# # count = {letter:sum(letter) for letter in all_letters if letter in letter}


#NO.3

weather_c = eval(input())

weather_f = {day:(temparature*9/5)+32 for day,temparature in weather_c.items()}
print(weather_f)