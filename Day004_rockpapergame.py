import random

paper = """
            ___..__
  __..--.... ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          ....----'    
"""

scissor = """
 .-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
"""

rock = """"
       ,--.--._
------" _, \___)
        / _/____)
        \//(____)
------\     (__)
       `-----"
"""

ans = int(input("Type 0 for paper, 1 for rock and 2 for scissor. ANS = "))

computer_ans = random.randint(0,2)

game = [paper,rock,scissor]

print(game[ans])
print(game[computer_ans])




if ans == computer_ans:
    print("Draw")
elif ans == 0 and computer_ans == 1:
    print("You win")
elif ans == 0 and computer_ans == 2:
    print("You lose")
elif computer_ans == 0 and ans == 1:
    print("You lose")
elif computer_ans == 0 and ans == 2:
    print("You win")
else:
    print("what did you type huh?")                


