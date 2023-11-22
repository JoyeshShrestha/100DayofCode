from logo import logo,vs
from data import data
import random
import os

def clear_console():
    os.system('cls')

length = len(data)
previous_num = []


def no_similarities(num1,num2,previous_num):    
    previous = False
    same= False
    if num2 in previous_num:
        previous = True
        
    while previous:
        if num2 not in previous_num:
            previous = False
            num2 = random.randint(0,length)
    if num1 == num2:

        same = True
    
    while same:
        if num1 != num2:
            same = False
            num2 = random.randint(0,length)
    return num2        

score = 0

def compare_followers(followers1,followers2):
    if followers1 > followers2:
        return "A"
    else:
        return "B"


proceed = True
num1 = random.randint(0,length)

# main program starts
while proceed:
    num2 = random.randint(0,length)
    num2 = no_similarities(num1,num2,previous_num)
    print(logo)
    print(f"Compare A: {data[num1]['name']}, {data[num1]['description']}, from {data[num1]['country']}  ")

    print(vs)

    print(f"Against B: {data[num2]['name']}, {data[num2]['description']}, from {data[num2]['country']}  ")
    if score != 0:
        
        print(f"You're right! Current Score : {score}")
    answer = input("Who has more followers? Type 'A' or 'B' ").upper()
    
    result = compare_followers(data[num1]['follower_count'],data[num2]['follower_count'])

    if answer !=result:
        clear_console()
        print(f"Sorry, that's wrong. Final score:{score}")
        break
    elif answer == result:
        clear_console()
        score+=1
        choose = random.randint(1,2)
        if choose== 1:
            previous_num.append(num1)
            previous_num.append(num2)

            num1 = num2
        if choose == 2:
            previous_num.append(num2)    
            num1 = num1
    if length == len(previous_num):
        print(f"Congratulations! You Won the game. Your final score : {score} ")     
        break   