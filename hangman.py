import random
def hangaman(turns):
    list_of_word=["sai","sukanya","umarani","riya","monalisha","arifa","nafiza","brasha","nibedita",
    "sujata","rudra","raja","sridhara","siba","sonam","jaani","navgurukul","jajpur",]
    word=random.choice(list_of_word)
    guess_made=""
    valid_entery=set("abcdefghijklmnopqrstuvwxyz")
    while len(word)>0:
        mainword=""
        for letter in word:
            mainword = mainword+letter if letter in guess_made else f"{mainword}_ "
        if mainword==word:
            print(mainword)
            print("Congrats!! 🥳 Your Guess is correct.. You won 🥳!!")
            break
        print("Guess the word",mainword)
        user_guess=input()
        if user_guess in valid_entery:
            guess_made=guess_made+user_guess
        else:
            print("Enter Valid Character")
            user_guess=input()
        if user_guess not in word:
            turns=turns-1
            if turns == 0:
                print("You loss")
                print("You let a good man die")
                print("_ _ _ _ _ _ _ _ _ _")
                print("         |        |")
                print("        |       |")
                print("         |        |")
                print("         O        |")
                print("        /|\       |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
                break
            elif turns == 1:
                print("2 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("         |        |")
                print("        |       |")
                print("         |        |")
                print("        \O/       |")
                print("         |        |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 2:
                print("2 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("         |        |")
                print("        |       |")
                print("        \O/       |")
                print("         |        |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 3:
                print("3 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("         |        |")
                print("        \O/       |")
                print("         |        |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 4:
                print("4 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("        \O        |")
                print("         |        |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 5:
                print("5 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("         O        |")
                print("         |        |")
                print("        / \       |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 6:
                print("6 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("         O        |")
                print("         |        |")
                print("        /         |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 7:
                print("7 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("         O        |")
                print("         |        |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 8:
                print("8 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("         O        |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("==================|")
            elif turns == 9:
                print("9 turns left!!")
                print("_ _ _ _ _ _ _ _ _ _")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("                  |")
                print("==================|")      
user_name=input("ENTER YOUR NAME:-----")
print("Welcome",user_name)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Try to guess the word in less than 10 attempts")
hangaman(10)
chance=input("DO YOU WANT TO PLAT AGAIN(Y/N):--")
if chance in ["y", "Y"]:
    hangaman(10)
else:
    print(" 😊 Thanks for Playing the game 😊")
#Hangaman project