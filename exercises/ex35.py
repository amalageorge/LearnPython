from sys import exit
def gold_room():
    print "This room is full of gold.How much do you take?"

    next = raw_input("> ")

    if "0" in next or "1" in next:
        how_much = int(next)

    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "you are  not greedy"

    else:
        dead ("You are greedy")

def bear_room():
    print "There is a bear"
    print "The bear has a bunch of honey"
    print "The fat bear is in front of another door"
    print "How are u going to move the bear"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at u and slaps ur face of")

        elif next == "taunt bear" and not bear_moved:
            dead("The bear has moved. You can go through it now.")
            bear_moved = True

        elif next == "taunt bear" and bear_moved:
            dead("The bear will chew ur leg")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I have got no idea what that means"

def panda_room():
    print "Here u see the Panda"
    print "You go insane when u see it"
    print "Do u flee for ur life or eat ur head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("That was tasty")
    else:
        panda_room()

def dead(why):
    print why, "Good job"
    exit(0)

def start():
    print "U r in a dark room"
    print "There is a door to ur right and left"
    print "Which one do u take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        panda_room()
    else:
        dead("You stumble around the room till u starve")


start()






