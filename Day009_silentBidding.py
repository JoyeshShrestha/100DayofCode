import os

def clear_console():
  os.system('cls')



logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
auction ={}
a= 0 
while a == 0:
    print("Welcome to the secret auction program")
    name = input("What is your name?: ")
    bid = input("What's your bid?: Rs. ")
    auction[name]=bid
    print("Are there any other bidders? Type Y/N ")
    ans = input().lower()
    if ans =="y":
        clear_console()
        

    if ans =="n":
        break
    
final_key = ""
count = 0
for key in auction:
    current = int(auction[key])
    if current >= count:
        count = current
        final_key = key
winner = final_key

clear_console()
print(f"{winner} wins the bidding by Rs.{count}")
