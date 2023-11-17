win='''

                     __________
        /\____;;___|
       | /         /
       `. ())oo() .
        |\(%()*^^()^|
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|

                    '''


swim = """
             ||
       \`._.-' `--.
        ) o o =[#]#]
        ) _o      -3
       /.' `-.,---'   
"""
fire = """
                 (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
"""
forgot="""
   _____
           /     \/_
          //\__(\_|
          |\ ^  ^ |
         .//_O \O_ |
          \_  (_)  /
           \  \_/ /
         __/\    /\__
        /  \ \  / /  |
       /    \/\/\/    |
      /   |    .   |   |
     /    |    .   |    |
"""


print('''
      ***************************************************************
          __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\     
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::'       :: :     ""--.._
                  __..-'          __;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ "---....___                                     __..--"" _)
     "--...  ___""-----......._______......----     --"
                   "       ---.....   ___....----
      ***************************************************************
''')


print("""Welcome to Treasure Island.
      Your mission is to find the treasure""")

a1 = input("go left or right? ")
a1_lower = a1.lower()
if a1_lower =="left":
    a2=input("""
      Do you want to "wait" for a boat or "swim" towards the island? 
      """)
    a2_lower=a2.lower()

    if a2 == "wait":
        print()
        c1 = input("There are three doors. Red, Yellow, Blue. Choose one?")
        
        c1_lower = c1.lower()
        if c1_lower == "red":
            print("Death by Fire")
            print(fire)
        elif c1_lower =="blue":
            print("Huh?You forgot to breathe.")
            print(forgot)

        elif c1_lower=="yellow":
            print("Less goooo. You found the treasure chest. You win!")    
            print(win)    

        else:
            print("Write the correct spellings! Stupid")    
    else:
        print("\n\n\nCongratulations! You died. You forgot that you never knew how to swim.\n How can you forget such a thing? \nIs it because of your greed or are you just stupid?")
        print("\nAny ways your dead body was torn apart by angry fishes. LEARN TO SWIM")
        print(swim)

else:
    print("hahaha! Stupid you died by falling in a hole")
    print('''
          ...
             ;::::;
           ;::::; :;
         ;:::::'   :;
        ;:::::;     ;.
       ,:::::'       ;           OOO\
       ::::::;       ;          OOOOO\
       ;:::::;       ;         OOOOOOOO
      ,;::::::;     ;'         / OOOOOOO
    ;:::::::::`. ,,,;.        /  / DOOOOOO
  .';:::::::::::::::::;,     /  /     DOOOO
 ,::::::;::::::;;;;::::;,   /  /        DOOO
;`::::::`'::::::;;;::::: ,#/  /          DOOO
:`:::::::`;::::::;;::: ;::#  /            DOOO
::`:::::::`;:::::::: ;::::# /              DOO
`:`:::::::`;:::::: ;::::::#/               DOO
 :::`:::::::`;; ;:::::::::##                OO
 ::::`:::::::`;::::::::;:::#                OO
 `:::::`::::::::::::;'`:;::#                O
  `:::::`::::::::;' /  / `:#
   ::::::`:::::;'  /  /   `#

''')

