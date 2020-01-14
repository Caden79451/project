yes_no = ["yes", "no"]
directions = ["A", "B"]
 
# Introduction
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
 
# First part
response = ""
while response not in directions:
    print("you go to the tree and decypher the mark which tells you a warning telling travelers to stay away")
    print("What do you do.")
    response = input("?\n a) You get worried and head to the next village. / b) You ignore the tree's warning and head to the village.\n")
    if response == "a":
        print("You get worried and head to the next village. Farewell, " + name + ".")
        quit()
    elif response == "b":
        print("You ignore the tree's warning and head to the village.\n")
    else:
        print("I didn't understand that.\n")

# Second part
    print("You arrive and a villager recognizes you and says, Hey do I know you?")
    print("What do you do?")
    response = input("?\n a) You tell him to leave you alone not knowing who he was. / b) Tell him he may speak with you later when you're not trying to rinse the taste of bad pottage out of your mouth.")
    if response == "a":
        print("You ignore the villager and go on your own way. Farewell, " + name + ".")
        quit()
    elif response == "b":
        print  ("You go and sit down and are later in the evening interrupted while eating by the same man with a request saying, “Sorry for not telling you who I was earlier but my name is not important, but my need is.”He then softly tells you that he has a proposition for you, and knows who you are.")
    else:
        print("I didn't understand that.\n")

# Third part
