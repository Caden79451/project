yes_no = ["yes", "no"]
a_b = ["a", "b"]
 
# Introduction to game
name = input("What is your name, adventurer?\n")
print("Greetings, " + name + ". Let us go on a adventure!")
print("You stumble upon a small village and decide to find out if there is a pub.")
print("Along the way you notice a tree with a mark on it.")
 
# Start of game
response = ""
while response not in yes_no:
    response = input("Do you review the mark?\nyes/no\n")
    if response == "yes":
        print("Look upon the tree and review the mark..\n")
    elif response == "no":
        print("You are not ready for this quest. Goodbye, " + name + ".")
        quit()
    else: 
        print("I didn't understand that.\n")
 
# First part of game
response = ""
while response not in a_b:
    print("you go to the tree and decypher the mark which tells you a warning telling travelers to stay away")
    print("What do you do.")
    response = input("?\n a) Head to the next village. / b) Head to the village.\n")
    if response == "a":
        print("You get worried and head to the next village. Farewell, " + name + ".")
        quit()
    elif response == "b":
        print("You ignore the tree's warning and head to the village.\n")
    else:
        print("I didn't understand that.\n")

# Second part of game
response = ""
while response not in a_b:
    print("You arrive and a villager recognizes you and says, Hey do I know you?")
    print("What do you do?")
    response = input("?\n a) You tell him to leave you alone not knowing who he was. / b) Tell him he may speak with you later.")
    if response == "a":
        print("You ignore the villager and go on your own way. Farewell, " + name + ".")
        quit()
    elif response == "b":
        print  ("You go and sit down and are later in the evening interrupted while eating by the same man with a request saying,")
        print("Sorry for not telling you who I was earlier but my name is not important, but my need is.")
        print("He then softly tells you that he has a proposition for you, and knows who you are.")
    else:
        print("I didn't understand that.\n")

# Third part of game
response = ""
while response not in a_b:
    print("He spends some time telling you that he is in need of you to reacquire an item of his of which he values dearly.")
    print("What do you say to his request?")
    response = input("?\n a) Go find another man to help you with your silly fetch quest” (Then throw your beer in his face). / b) I will do it only if the coin is good enough, so you better not cheat me. You know the consequences.")
    if response == "a":
        print("You then leave and head to the next village. Farewell, " + name + ".")
        quit()
    elif response == "b":
        print("After telling the man your response he smiles with a sinister look and then very gleefully says to you,")
        print("“Great...great, well i’m so glad this conversation has been so pleasant and friendly, only the man watching in the sky would have known what to do if you said no.”")
    else:
        print("I didn't understand that.\n")

#Fourth part of game
response = ""
while response not in a_b:
    print("What is your response to his words?")
    response = input("?\n a) Well just glad I could help you. / b) Well we can cheer about it later but for now let me get the job done. ")
    if response == "a":
        print("Then after you went on your way to the location he told you about something did not feel right.")
    elif response == "b":
        print("Then after you went on your way to the location he told you about something did not feel right.")
    else:
        print("I didn't understand that.\n")

#Fifth part of game
response = ""
while response not in a_b:
    print("What do you do?")
    response = input("?\n a) Go into the building and investigate. / b) You decide you are not prepared for this quest and leave the area.")
    if response == "a":
        print("You go into the building.)
    elif response == "b":
        print("Leave the area and tell the man that he was not getting your help. Goodbye, " + name + ".")
        quit()
    else:
        print("I didn't understand that.\n")
#Last part of game
response = ""
while response not in a_b:
    print(" Once you enter you feel a aura that creates a feeling of anxiety that comes over you.")
    print("But in a glimpse you see a shadow run past you towards your right.")
    print("what do you do?")