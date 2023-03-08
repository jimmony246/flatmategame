import random
import time

# give each flatmates answers to the q's, maybe in dictionary form

flatmates = {
    "Eline": {
        "birthday": "05/10/1997",
        "colour": "green",
        "meal": "pâtes champignons",
        "film": "oss 117",
    },
    "Louise": {
        "birthday": "08/10/1998",
        "colour": "jaune",
        "meal": "les pâtes grillées de mamie Pou",
        "film": "30 ans sinon rien",
    },
    "Amir": {
        "birthday": "15/01/1994",
        "colour": "vert",
        "meal": "couscous",
        "film": "les affranchis",
    },
    "Jonny": {
        "birthday": "27/08/1999",
        "colour": "blue",
        "meal": "sticky chicken",
        "film": "her",
    }
}

# greet player

print('''
                                  _H_              _H_               _H_                  o88o.
          .=|_|===========v==|_|============v==|_|===========.    (8%8898),
         /                |                 |                 \ ,(8888%8688)
        /_________________|_________________|__________________(898%88688HJW)
        |=|_|_|_|  =|_|_|=|X|)^^^(|X|=|/ \|=||_|_|_|=| ||_|_|=|`(86888%8%9b)
        |=|_|_|_|== |_|_|=|X|\___/|X|=||_||=||_____|=|_||_|_|=|___(88%%8888)
        |=_________= ,-. =|""""""""""="""""=|=_________== == =|_______\//`'
        |=|__|__|_| //O\=|X|"""""|X|=//"\=|=|_|_|_|_| .---.=|.=====.||
        |=|__|__|_|=|| ||=|X|_____|X|=|| ||=|=|_______|=||"||=||=====|||
        |___d%8b____||_||_|=_________=||_||_|__d8%o%8b_=|j_j|=|j==o==j|\---
''')
time.sleep(1)
print("""Bienvenue. Each of your flatmates has a gift for you
but you'll need to answer some questions first...""")

# set number of lives to 3

lives = 3



# create functions for each flatmate

# function for Eline
def eline(lives):
    print("You knock on Eline's door.")
    time.sleep(1)
    print("*Elle fait pause a Koh-Lanta*")
    time.sleep(1)
    print("Qu'est-ce qu'il y a ? Ah, tu veux mon cadeau ? Eh bien, réponds à ces questions sur moi : ")
    while lives > 0:
        q1 = input("When is Eline's birthday? (dd/mm/yyyy)\n")
        if q1.lower() == flatmates["Eline"]["birthday"]:
            print("bien joué...on to the next question")
            time.sleep(1)
            q2 = input("What is Eline's favourite colour? Purple, Red, or Green\n")
            # second question
            if q2.lower() == flatmates["Eline"]["colour"]:
                print("Tu me connais mieux que je ne me connais moi-même !")
                #     third question
                time.sleep(1)
                q3 = input("What is Eline's favourite meal? Hint: it is an anagram of\ntsnpiasegâ hconpm\n")
                if q3.lower() == flatmates["Eline"]["meal"]:
                    print("mmmmm delicious very nice and tasty!")
                    #         fourth question
                    time.sleep(1)
                    q4 = input("What is Eline's favourite film? Hint: it contains a number\n")
                    if q4.lower() == flatmates["Eline"]["film"]:
                        print("Félicitations, tu connais bien Eline et elle t'offre une leçon de snowboard!")
                        return True
                    else:
                        lives -= 1
                        print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                        if lives == 0:
                            print("Game over! You ran out of lives.")
                            return False
                        else:
                            print("Réessaye !")
                            continue
                else:
                    lives -= 1
                    print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                    if lives == 0:
                        print("Game over! You ran out of lives.")
                        return False
                    else:
                        print("Réessaye !")
                        continue
            else:
                lives -= 1
                print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                if lives == 0:
                    print("Game over! You ran out of lives.")
                    return False
                else:
                    print("Réessaye !")
                    continue
        else:
            lives -= 1
            print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
            if lives == 0:
                print("Game over! You ran out of lives.")
                return False
            else:
                print("Réessaye !")
                continue
    return lives

# function for Amir

def amir(lives):
    print("You knock on Amir's door.")
    time.sleep(1)
    print("*Les sons de la guitare s'arrêtent*")
    time.sleep(1)
    print("*Amir apparaît, couvert d'œufs*")
    time.sleep(1)
    print("Je m'amusais à mettre des œufs dans ma guitare, que veux-tu ? ")
    while lives > 0:
        q1 = input("When is Amir's birthday? (dd/mm/yyyy)\n")
        if q1.lower() == flatmates["Amir"]["birthday"]:
            print("Chut! J'ai dit aux autres que j'avais 24 ans, alors garde cette date secrète !")
            time.sleep(1)
            q2 = input("What is Amir's favourite colour? No hints here because Amir doesn't like them.\n")
            # second question
            if q2.lower() == flatmates["Amir"]["colour"]:
                print("Trop facile, essaye celui-là !")
                time.sleep(1)
                #     third question
                q3 = input("What is Amir's favourite meal? (a)Tandoori (b)Couscous (c)Potatoes and eggs\n")
                if q3.lower() == flatmates["Amir"]["meal"] or q3.lower() == "b":
                    print("hyuh hyuh hyuh I eat that good baby")
                    time.sleep(1)
                    #         fourth question
                    q4 = input("What is Amir's favourite film? Hint: The English title could literally be 'les bons mecs'...\n")
                    if q4.lower() == flatmates["Amir"]["film"]:
                        print("Bravo ! Tu as gagné la confiance d'Amir et il te récompense en te donnant une leçon de guitare.")
                        return True
                    else:
                        lives -= 1
                        print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                        if lives == 0:
                            print("Game over! You ran out of lives.")
                            return False
                        else:
                            print("Réessaye !")
                            continue
                else:
                    lives -= 1
                    print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                    if lives == 0:
                        print("Game over! You ran out of lives.")
                        return False
                    else:
                        print("Réessaye !")
                        continue
            else:
                lives -= 1
                print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                if lives == 0:
                    print("Game over! You ran out of lives.")
                    return False
                else:
                    print("Réessaye !")
                    continue
        else:
            lives -= 1
            print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
            if lives == 0:
                print("Game over! You ran out of lives.")
                return False
            else:
                print("Réessaye !")
                continue
    return lives

# function for Louise
def louise(lives):
    print("You knock on Louise's door.")
    time.sleep(1)
    print("*Elle apparaît, tenant un vaporisateur pour ses plantes.*")
    time.sleep(1)
    print("Je faisais de l'improvisation avec mes plantes ! Maintenant, tu dois improviser des réponses !")
    time.sleep(1)
    while lives > 0:
        q1 = input("When is Louise's birthday? (dd/mm/yyyy)\n")
        if q1.lower() == flatmates["Louise"]["birthday"]:
            print("Bien joué - Impro !")
            time.sleep(1)
            q2 = input("What is Louise's favourite colour? Hint: It's the colour of the Beatles' submarine...\n")
            # second question
            if q2.lower() == flatmates["Louise"]["colour"] or q2.lower == "yellow":
                print("Yellow marshmallow makes me mellow baby! ")
                time.sleep(1)
                #     third question
                q3 = input("What is Louise's favourite meal? (a)les pâtes grillées de mamie Pou \n(b)les pâtes grillées de mamie Fou\n(c)les pâtes grillées de mamie genou")
                if q3.lower() == flatmates["Louise"]["meal"] or q3.lower() == "a":
                    print("Yum yum so scrumptious")
                    time.sleep(1)
                    #         fourth question
                    q4 = input("What is Louise's favourite film? Hint: The age when you can learn to drive in the U.K.\n")
                    if q4.lower() == flatmates["Louise"]["film"]:
                        print("Bravo, Louise est très contente que tu la connaisses bien et elle t'offre des cours d'improvisation théâtrale!")
                        return True
                    else:
                        lives -= 1
                        print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                        if lives == 0:
                            print("Game over! You ran out of lives.")
                            return False
                        else:
                            print("Réessaye !")
                            continue
                else:
                    lives -= 1
                    print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                    if lives == 0:
                        print("Game over! You ran out of lives.")
                        return False
                    else:
                        print("Réessaye !")
                        continue
            else:
                lives -= 1
                print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                if lives == 0:
                    print("Game over! You ran out of lives.")
                    return False
                else:
                    print("Réessaye !")
                    continue
        else:
            lives -= 1
            print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
            if lives == 0:
                print("Game over! You ran out of lives.")
                return False
            else:
                print("Réessaye !")
                continue
    return lives


# function for Jonny
def jonny(lives):
    print("You knock on Jonny's door.")
    time.sleep(1)
    print("*The strange singing sounds stop*")
    time.sleep(1)
    print("Why hello there! I was singing some Louis Armstrong - did you hear? Come on then, answer my questions bruv.")
    time.sleep(1)
    while lives > 0:
        q1 = input("When is Jonny's birthday? (dd/mm/yyyy)\n")
        if q1.lower() == flatmates["Jonny"]["birthday"]:
            print("Pas mal mate pas mal!")
            time.sleep(1)
            q2 = input("What is Jonny's favourite colour? Hint:\nSome say you are this colour\nWhen you're feeling down\nYour eyes might be this colour\nIf they're not green or brown\n")
            # second question
            if q2.lower() == flatmates["Jonny"]["colour"]:
                print("Blue as the ocean darling, that's groovy")
                time.sleep(1)
                #     third question
                q3 = input("What is Jonny's favourite meal? Hint: The english word for bâton will give you a good start\n")
                if q3.lower() == flatmates["Jonny"]["meal"]:
                    print("Sweet sweet sticky chicken all day long baby")
                    time.sleep(1)
                    #         fourth question
                    q4 = input("What is Jonny's favourite film? Hint: A.I.\n")
                    if q4.lower() == flatmates["Jonny"]["film"]:
                        print("Wahey! You bloody legend. Jonny is very pleased and offers you an English lesson!")
                        return True
                    else:
                        lives -= 1
                        print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                        if lives == 0:
                            print("Game over! You ran out of lives.")
                            return False
                        else:
                            print("Réessaye !")
                            continue
                else:
                    lives -= 1
                    print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                    if lives == 0:
                        print("Game over! You ran out of lives.")
                        return False
                    else:
                        print("Réessaye !")
                        continue
            else:
                lives -= 1
                print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
                if lives == 0:
                    print("Game over! You ran out of lives.")
                    return False
                else:
                    print("Réessaye !")
                    continue
        else:
            lives -= 1
            print(f"La honte! Tu connais même pas tes propres colocs ! You have {lives} lives left.")
            if lives == 0:
                print("Game over! You ran out of lives.")
                return False
            else:
                print("Réessaye !")
                continue
    return lives


# ask user which door they want to knock on

while lives > 0:
    door = input("Who's door do you want to knock on? (E)line, (L)ouise, (A)mir, or (J)onny?\n")
    if door.lower() == "e":
        eline(lives)
    elif door.lower() == "a":
        amir(lives)
    elif door.lower() == "l":
        louise(lives)
    elif door.lower() == "j":
        jonny(lives)
    else:
        print("That's not even one of your flatmates dummy")
        continue


