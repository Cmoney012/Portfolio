from Library import *


def Start():
    while True:
        print("   >>>Welcome to game!<<<")
        print(">>>Would you like to play?<<<")
        play = input("Y/N: ")
        if play.lower() == "y":
            print(">>>Great!")
            print(
                "***If you ever want to see what options you have at any point, type Help and a list of commands will pop up***")
            player.name = input("What is your name?: ")
            Backstory()
        if play.lower() == "n":
            quit()


def Backstory():
    while True:
        print(
            ">>>As you wake up, your head feels like someone hit it with a hammer and as you look around you realize you're in an unfamiliar space")
        # sleep(2)
        print(">>>Your hand unconsciously goes to you're belt")
        # sleep(2)
        print("What do you find there?")
        print("a. Hammer - Blacksmiths Apprentice")
        print("b. Dagger - Orphan")
        print("c. Bag of Gold - Noble")
        backstory_choice = input("Enter the letter that corresponds with the backstory you'd like: ")
        static_options(backstory_choice)
        if backstory_choice.lower() == "a":
            print(">>>Your fingers find the smooth handle of your trusty hammer and you breathe a sigh of relief")
            print("~~Hammer added~~")
            playerinven.add_item(Hammer)
            setattr(player, "backstory", "Blacksmith")
            LastNight()
        if backstory_choice.lower() == "b":
            print(">>>You find your dagger tucked in your belt, you feel a bit less anxiety")
            print("~~Dagger added~~")
            playerinven.add_item(Dagger)
            setattr(player, "backstory", "Orphan")
            LastNight()
        if backstory_choice.lower() == "c":
            print(">>>The clinking of gold as your fingers brush against your coin purse puts you a little at ease")
            print("~~Coin Purse added~~")
            player.add_gold(10)
            setattr(player, "backstory", "Noble")
            LastNight()


def LastNight():
    while True:
        print(
            ">>>You spend a minute trying to remember what you did last night... You think the memory starts to come back...")
        # sleep(1)
        print("Maybe it was...")
        print("a. Drinking with the boys")
        print("b. Getting into fights")
        print("c. Horse racing at night")
        print("d. Stealing from people")
        last_night = input("Enter answer here: ")
        static_options(last_night)
        if last_night.lower() == "a":
            setattr(player, "last_night", "drinking")
            player.add_max_hp()
            print("-+-Your Max Hp has raised a little-+-")
            # sleep(1)
            print(
                ">>>Its starting to come back now, the loud bar and the smell of ale. The last thing you remember is your\n"
                ">>friend Bulban yelling for help...")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            SelfIndex()
        if last_night.lower() == "b":
            setattr(player, "last_night", "fighting")
            player.add_dam()
            print("-+-Your Damage has raised a little-+-")
            # sleep(1)
            print(
                f">>>Its starting to come back now, yelling and cursing, fist and feet everywhere. Why did you let Bulban\n"
                ">>go out after he'd been drinking?")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            SelfIndex()
        if last_night.lower() == "c":
            setattr(player, "last_night", "racing")
            player.add_spd()
            print("-+-Your Speed has raised a little-+-")
            # sleep(1)
            print(
                f">>>Its starting to come back now, strained muscles, the cold air rushing by you as you speed through the\n "
                ">>night. Bulban calls out from behind you \n'Slow down! We're almost to the bridge!'")
            # sleep(1)
            print(">>>And then suddenly you're falling")
            print(">>>You go to stand up and realize how sore you really are")
            SelfIndex()
        if last_night.lower() == "d":
            # sleep(1)
            setattr(player, "last_night", "stealing")
            playerinven.add_item(SilverRing)
            print(">>>You reach in your pocket and feel the ring you stole last night")
            print("~~Silver Ring added~~")
            # sleep(1)
            print(
                ">>>Of course, the ring. You'd seen lady Nanari with it and decided it would look better on you... her\n"
                ">>husband didn't seem to agree when he caught you trying to sneak in")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            SelfIndex()


def SelfIndex():
    while True:
        print("Would you like to check yourself for damage?")
        check_self = input("Y/N: ")
        static_options(check_self)
        if check_self.lower() == "y":
            if player.last_night == "drinking":
                print(
                    ">>>The bruises across your torso tell you that at some point last night you got into a fight, but\n "
                    ">>for the life of you, you can't remember with who or why")
                player.current_hp()
                SearchRoom()
            if player.last_night == "fighting":
                print(
                    ">>>From the way your jaw feels you'd say you lost a fight to someone last night, you can't remember\n"
                    ">>anything past telling Bulban to sod off after he tried to get you to go to the pub last night, and\n"
                    ">>then going anyway for Bulban's sake")
                player.current_hp()
                SearchRoom()
            if player.last_night == "racing":
                print(
                    ">>>You're pretty sure your shoulder is dislocated, but for the fall you took, you actually feel pretty good")
                player.current_hp()
                SearchRoom()
            if player.last_night == "stealing":
                print(
                    ">>>You can almost see the imprint of Sir Tellin's boots on your ribs as you inspect yourself for injuries.\n"
                    ">>Come to think of it, how do you still have the ring?")
                player.current_hp()
                SearchRoom()
        if check_self.lower() == "n":
            print(">>>Tis but a scratch, you'll deal with it later")
            print("***To check your current hp in the future, type hp into any prompt***")
            SearchRoom()


def SearchRoom():
    while True:
        print("You look around the room some more. You see: ")
        print("a. Window")
        print("b. Door")
        print("c. Bookshelf")
        checkroom = input("Which do you check?: ")
        static_options(checkroom)
        if checkroom.lower() == "a" and player.backstory == "Orphan":
            SearchWindowOrphan()
            ###Potentially unneeded redundancy, test later
        if checkroom.lower() == "a" and player.backstory != "Orphan":
            SearchWindow()
        if checkroom.lower() == "b":
            SearchDoor()
        if checkroom.lower() == "c":
            SearchBookshelf()


def SearchWindow():
    while True:
        if Window1.misc == 0:
            print(
                ">>>You step towards the window, from the sun you can tell it's early in the morning. It takes you a moment to realize... ")
            # sleep(1)

            print(
                ">>>You look down on an unfamiliar town. From the third story of the building you're in, you can see\n"
                "that the city is quite large, roughly the same size of Trostenwald by your estimation")
            Window1.change_misc()
        else:
            print("What would you like to do?")
            print("a. Keep looking through the window for awhile")
            print("b. Search something else")
            if player.backstory == "Blacksmith":
                print("c. Try smashing the window")
            window_choice = input("Enter choice here: ")
            static_options(window_choice)
            if window_choice.lower() == "a" and Window1.misc == 0:
                print(">>>You spend a minute or so looking through the window before you see someone coming down\n"
                      ">>the street. You're thinking about calling out to them before you notice something strange")
                # sleep(1)
                print(">>>The figure seems much taller than a normal person, but more than that you notice\n"
                      ">>the purplish hue to their skin that you've never seen before")
                # sleep(1)
                print(">>>As you look closer you realize their hair is also a strange light blue")
                print(">>You spend another minute looking but no one else comes into view")
                # sleep(1)
                Window1.change_misc(1)
                SearchWindow()
            if window_choice.lower() == "a" and Window1.misc == 1:
                print(
                    ">>>You can't resist taking another look through the window. You spend another minute waiting before\n"
                    ">>someone else comes into view. This time it's a pair of what appears to be two women. Their skin\n"
                    ">>looks a pale pink. They walk by without appearing to notice you. 'What is going on' you think to yourself")
                Window1.change_misc(1)
                # sleep(3)
                SearchWindow()
            if window_choice.lower() == "a" and Window1.misc == 2:
                print(">>>You spend a few more minutes looking through the window but no one else appears, strange.")
                SearchWindow()
            if window_choice.lower() == "b":
                print(">>>You feel like you've got bigger things to attend to")
                SearchRoom()

            if window_choice.lower() == "c" and player.backstory == "Blacksmith" and Window1.intact:
                Window1.smash()
                print(
                    ">>>You pull your hammer back and smash the window. You flinch at how loud the crash is but there's\n"
                    ">>no turning back now")
                # sleep(1)
                print(
                    ">>>You take a deep breath and begin to pull yourself through the window. Right as you begin\n"
                    ">>to pull yourself through the window you hear a woman call out from beyond the door")
                # sleep(2)
                print(f">>>'{player.name}?' and you freeze. How does she know your name?")
                # sleep(1)
                print("What do you do?")
                print("a. Continue climbing out of the window?")
                print("b. Wait for her to say something else")
                print("c. Reply to her")
                smith_escape = input("Enter choice here: ")
                static_options(smith_escape)
                if smith_escape.lower == "a":
                    print(
                        ">>>You keep climbing out of the window. As you pull yourself onto the roof, you hear the click\n"
                        ">>of a tumbler being turned. Startled, you begin to fall")
                    # sleep(1)
                    print(
                        ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                    player.hurt(3)
                    player.current_hp()
                    Street()
                    # Work on details of this way out later

                if smith_escape.lower() == "b":
                    print(
                        ">>>You freeze as the voice hits your ears. You take a second to wait and see if she says\n"
                        ">>something else")
                    # sleep(1)
                    print(
                        ">>>After a moment you hear a knock at the door followed by the same voice saying\n"
                        ">>'Listen, I know you're probably confused. If you allow me I'll explain what I know")
                    # sleep(1)
                    print("You can either\n"
                          "a. Respond\n"
                          "b. Escape out of window\n"
                          "c. Wait some more")
                    x = input("Enter choice here: ")
                    static_options(x)
                    if x.lower() == "a":
                        print(">>>The offer of clarification is too tempting for you to deny. You call out to her\n"
                              ">>'Who are you, and how do you know my name?")
                        # sleep(2)
                        print(">>>She responds, 'My name is Shae-Orra and I know your name because my brother told\n"
                              ">>me you'd be here. If you want more answers you'll have to talk to him")
                        # sleep(2)
                        print(">>>'Now', she continues, 'If you'd be so kind as to open the door I can take you to him")
                        print("Do you open the door?")
                        y = input("Y/N: ")
                        static_options(y)
                        if y.lower() == "y" and DoorKey1 in playerinven:
                            print(">>>You approach the door and turn the key. It opens to reveal a... she looks like\n"
                                  ">>a human woman except for the color of her skin which is a light pink and her hair\n"
                                  ">>is a deep blue")
                            # sleep(3)
                            print(">>>'That's better', she says, seemingly not surprised at your complexion, 'Now'\n"
                                  ">>she continues, 'Lets go see my brother")
                            # sleep(1)
                            print(">>>She leads you down a hallway. You can't help but notice how big this house is")
                            print(">>>After a minute she stops outside a door and turns to look at you, 'This is it',\n"
                                  ">>she says gesturing towards the door")
                            MeetBro()

                        if y.lower() == "y" and DoorKey1 not in playerinven:
                            print(
                                ">>>You say, 'I don't have a key'. After a moment you hear a key hit the lock from outside")
                            # sleep(1)
                            print(">>>The door opens to reveal a... she looks like a human woman except for the color\n"
                                  ">>of her skin which is a light pink and her hair is a deep blue")
                            # sleep(1)
                            print(">>>'There', she says, 'Now, if you'd be so kinds as to follow me'")
                            print(">>>She leads you down a hallway. You can't help but notice how big this house is")
                            # sleep(1)
                            print(">>>After a minute she stops outside a door and turns to look at you, 'This is it',\n"
                                  ">>she says gesturing towards the door")
                            MeetBro()

                        if y.lower() == "n":
                            print(">>>You decide you don't trust her")
                            print("Do you keep climbing out of the window?")
                            r = input("Y/N: ")
                            static_options(r)
                            if r.lower() == "y":
                                print(
                                    ">>>You keep climbing out of the window. As you pull yourself onto the roof you hear\n"
                                    ">>the doorknob begin to turn behind you and you lose your balance")
                                # sleep(1)
                                print(
                                    ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                                player.hurt(3)
                                player.current_hp()
                                Street()

                            if r.lower() == "n":
                                print(">>>You decide to look around some more before risking that fall")
                                # sleep(1)
                                print(">>>As you begin to back away from the window you hear the tumbler in the door\n"
                                      ">>click and the door opens")
                                # sleep(1)
                                print(
                                    ">>>You see what looks like a woman, except her hair is a deep blue and her skin\n"
                                    ">>is a shade of light pink you don't recall ever seeing before")
                                # sleep(1)
                                print(
                                    ">>>She looks from you to the broken window and sighs. 'I don't suppose you know\n"
                                    ">>who did that', she asks in a joking manner")
                                print(
                                    ">>>'Now', she continues, 'I understand that you must be confused but you have to\n"
                                    ">>believe me, the only person who can help you is my brother. Will you come with\n"
                                    ">>me to meet him?', after a moment she sheepishly adds 'Please?'")
                                print("Do you\n"
                                      "a. Go with her\n"
                                      "b. Break for the window")
                                t = input("Enter choice here: ")
                                static_options(t)
                                if t.lower() == "a":
                                    print(
                                        ">>>You just nod your head and she smiles at you before turning around and saying\n"
                                        ">>'Come on then, it's this way'")
                                    print(
                                        ">>>She leads you down a hallway. You can't help but notice how big this house is")
                                    # sleep(1)
                                    print(
                                        ">>>After a minute she stops outside a door and turns to look at you, 'This is it',\n"
                                        ">>she says gesturing towards the door")
                                    MeetBro()

                                    if t.lower() == "b":
                                        print(
                                            ">>>Before she can react you rush headlong out of the broken window. You do your best\n"
                                            ">>to keep your balance but in your haste your foot slips")
                                        # sleep(1)
                                        print(
                                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                                        player.hurt(3)
                                        player.current_hp()
                                        Street()
                                        # Work on details of this way out later

                    if x.lower() == "b":
                        print(">>>You're unconvinced. You decide to continue escaping out of the window")
                        # sleep(1)
                        print(
                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                        player.hurt(3)
                        player.current_hp()
                        Street()

                    if x.lower() == "c":
                        print(
                            ">>>You stay silent for another few seconds, unsure of what to do. After a brief lull you hear\n"
                            ">>the lock in the door knob turn over and the door opens")
                        # sleep(1)
                        print(">>>When the door opens you see a woman with pink skin and hair colored a deep blue")
                        # sleep(1)
                        print(
                            ">>>She looks from you to the broken window. 'Surely that isn't a good idea now is it?' she says cracking a grin")
                        # sleep(1)
                        print(">>>After a second of shock wears off you realize your hand is still on the window sill")
                        print("Do you jump out?")
                        o = input("Y/N: ")
                        static_options(o)
                        if o.lower() == "y":
                            print(
                                ">>>This is too weird, you have to get out of here. You pull yourself through the window and\n"
                                ">>onto the roof. As soon as your other foot hits the sharp angle of the shingles you lose your balance")
                            # sleep(1)
                            print(
                                ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                            player.hurt(3)
                            player.current_hp()
                            Street()

                        if o.lower() == "n":
                            print(">>>You step away from the window sill")
                            # sleep(1)
                            print(
                                ">>>'That's better', she says. She looks at the broken window and smiles, 'I never liked\n"
                                "that window anyway. Name's Shae-Orra', she says with a smile")
                            # sleep(1)
                            print(
                                "'Now if you'd be so kind as to follow me, my brother is anxious to meet you. After nodding\n"
                                "your agreement she turns and begins walking")
                            print(">>>She leads you down a hallway. You can't help but notice how big this house is")
                            # sleep(1)
                            print(">>>After a minute she stops outside a door and turns to look at you, 'This is it',\n"
                                  ">>she says gesturing towards the door")
                            MeetBro()

                if smith_escape.lower() == "c":
                    print(">>>The woman's words seem sincere to you and you stop trying to climb out of the window.")
                    # sleep(1)
                    print(">>>You call out, 'How do you know my name?'")
                    # sleep(1)
                    print(">>>After a moment she replies, 'My brother can explain everything, if you'll let him'")
                    print("Do you\n"
                          "a. Go with her\n"
                          "b. Jump out of window")
                    z = input("Enter choice here: ")
                    static_options(z)
                    if z.lower() == "a":
                        print(">>>You take a second to consider before saying, 'Fine, take me to your brother then'")
                        # sleep(1)
                        print(
                            ">>>'Wonderful' you hear from the other side of the door. You can't quite tell but you think\n"
                            ">>you may detect a hint of sarcasm in her tone.")
                        # sleep(1)
                        print(
                            ">>>After a moment you hear the sound of a key unlocking a door and before you stands a woman\n"
                            ">>Well, almost. Aside from her light pink skin and deep blue hair she looks completely normal")
                        # sleep(1)
                        print(
                            ">>>Noticing the expression on your face, she lets out a small laugh. 'Yes, I'm pink', a moment later\n"
                            ">>she notices the broken window and laughs again. 'I don't suppose you saw who did that did you?")
                        # sleep(1)
                        print(">>>'Anyway, the answers you seek are this way', and she turns around and begins walking")
                        print(">>>She leads you down a hallway. You can't help but notice how big this house is")
                        # sleep(1)
                        print(">>>After a minute she stops outside a door and turns to look at you, 'This is it',\n"
                              ">>she says gesturing towards the door")
                        MeetBro()
                    if z.lower() == "b":
                        print(
                            ">>>You don't like her answer. You quickly mantle the window sill and in your haste lose your balance")
                        # sleep(1)
                        print(
                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                        player.hurt(3)
                        player.current_hp()
                        Street()


def SearchWindowOrphan():
    if not Window1.locked:
        print("The window is open, would you like to go through it?")
        leave = input("Y/N:  ")
        static_options(leave)
        if leave == "y":
            print(">>>You leap through the window and make your way down to the street without issue")
            Street()
        if leave == "n":
            print(">>>You decide to look around a little more")
            SearchWindow()
    if player.backstory == "Orphan" and Window1.locked:
        print(
            ">>>You look through the window and immediately realize that this is not Trostenwald. Strangely though, having\n"
            ">>spent almost your entire life navigating the many roads and alleyways of Trostenwald, you recognize a sort\n"
            ">>of similarity. Almost like someone rebuilt Trostenwald from memory...")
        # sleep(2)
        print(
            ">>>Saving that strange bit of information for later, you examine the window itself. Being somewhat of an\n"
            ">>expert on them you guess you could get this one open if you wanted. You can tell getting down from here\n"
            ">>is going to be difficult, but you could probably do it")
        print("Do you try to open the window?")
        OrphanWindow = input("Y/N: ")
        static_options(OrphanWindow)
        if OrphanWindow.lower() == "y":
            Window1.unlock()
            print(">>>You try to slide your knife between the sill and the glass.")
            # sleep(2)
            print(">>>After a few moments you manage to slide the blade of your knife under the window and pop it open")
            # sleep(1)
            print("Would you like to climb through? ")
            leave = input("Y/N: ")
            static_options(leave)
            if leave.lower() == "y":
                print(">>>Carefully you pull yourself through the open window. You don't see anyone on the street below\n"
                      "that could potentially blow your cover, for now. From the roof you can see that the buildings\n"
                      "here are close enough together that you should be able to jump from one to another. Or you could\n"
                      "just drop down to the street and go from there")
                print("Would you like to:\n"
                      "a. Stay on the roofs\n"
                      "b. Drop down to the street\n"
                      "c. Go back inside")
                orph_esc = input("Enter choice here: ")
                static_options(orph_esc)
                if orph_esc.lower() == "a":
                    print(">>>You decide it's safer for now to stay up high")
                    # Rooftops()
                if orph_esc.lower() == "b":
                    print(">>>You expect you might draw far too much attention on the roofs, not to mention the constant\n"
                          ">>danger of falling")
                    # sleep(1)
                    print(">>>You deftly scale down the face of the building you're on and after a few moments, your boots\n"
                          ">>hit solid ground.")
                    Street()
                if orph_esc.lower() == "c":
                    print(">>>You decide it might be a good idea to look around some more before you decide to take off.\n"
                          ">>Without trouble you slide back through the window")
                    SearchRoom()
            if leave.lower() == "n":
                SearchWindow()
        if OrphanWindow.lower() == "n":
            print(
                ">>>You decide it's probably better to look for a way out that doesn't risk a thirty foot fall, better try something else")
            SearchWindow()


def SearchDoor():
    while True:
        # Figure out the best way to get approach message to trigger once
        print(">>>You approach the door")
        if not Door1.locked or not Door1.intact:
            print("Would you like to leave the room?")
            opendoor = input("Y/N: ")
            static_options(opendoor)
            if opendoor.lower() == "y":
                print(">>>You slowly pull open the door to reveal a long hallway")
                if Door1.intact:
                    Hallway()
                if not Door1.intact:
                    HallwaySmash()
            if opendoor.lower() == "n":
                print(">>>You decide you may not be done in here yet")
                SearchRoom()
        if DoorKey1 in playerinven.content:
            print("Would you like to try the key on the door?")
            key_use = input("Y/N: ")
            static_options(key_use)
            if key_use.lower() == "y":
                print(
                    ">>> You put the key in the doorknob and turn with baited breath. As the key turns a quite click echos\n"
                    ">>off the walls of the room and you breathe a sigh of relief. The key does seem to be stuck though")
                print("Key removed from inventory")
                playerinven.remove(DoorKey1)
                Door1.unlock()
                SearchDoor()
            if key_use.lower() == "n":
                print(">>>You're not sure if you're done here yet")
                SearchDoor()
        if player.backstory == "Blacksmith" and Door1.locked and Door1.intact:
            print(">>>You don't like the look of that door knob, maybe you should just smash it?")
            print("Smash the door?")
            smash_door = input("Y/N: ")
            static_options(smash_door)
            if smash_door.lower() == "y":
                Door1.smash()
                SearchDoor()
            if smash_door.lower() == "n":
                print(">>>You think that may be a little hasty. Maybe just wiggle the handle to see if it's unlocked?")
                print("Wiggle handle?")
                door_choice = input("Y/N: ")
                static_options(door_choice)
                if door_choice.lower() == "y" and Door1.trap:
                    player.hurt(1)
                    player.current_hp()
                    print(">>>Oww!")
                    print(
                        ">>>As you twist the doorknob you hear a small snap as a trap that was attached to the doorknob activates.\n"
                        ">>You don't think it'll happen again but the door is locked. Better try something else")
                    # sleep(2)
                    Door1.disarm()
                    SearchDoor()
                if door_choice.lower() == "y" and not Door1.trap:
                    print(">>>The trap only works once but the door is still locked")
                if door_choice.lower() == "n":
                    print(">>>You decide to leave the door for later")
                    SearchRoom()
        if Door1.locked:
            print(">>>The handle has a keyhole in it.")
            print("Do you try to twist the doorknob?")
            door_choice = input("Y/N: ")
            static_options(door_choice)
            if door_choice.lower() == "y":
                if Door1.trap:
                    print(
                        ">>>As you twist the doorknob you hear a small snap as the trap that was attached to the doorknob activates")
                    print(">>>Oww!")
                    player.hurt(1)
                    player.current_hp()
                    Door1.disarm()
                    print(">>>You don't think it'll happen again but the door is locked. Better try something else")
                    SearchRoom()
                if not Door1.trap:
                    print(">>>The trap only works once but the door is still locked")
                    SearchRoom()
            if door_choice.lower() == "n":
                print(
                    ">>>As you take a second to examine the door knob, you notice a strange button on the backside of the knob,\n"
                    ">>better be careful with that")
                SearchRoom()


def SearchBookshelf():
    while True:
        print(">>>You look over the bookshelf for a moment. A couple books stand out to you")
        print("a. A smaller book on the side looks like a journal to you")
        print("b. What looks like a bundle of maps tucked in the top shelf")
        if HistoryBook not in playerinven.content:
            print("c. A very large leather bound tome ornate in design that lays flat on its shelf")
        print("d. Do something else")
        if player.backstory == "Noble" and FaerieTales not in playerinven.content:
            print("e. A book that reminds you of a book of Faerie tales your mother used to read you")
        print("Which would you like to examine more closely? ")
        which_book = input("Enter choice here: ")
        static_options(which_book)
        if which_book.lower() == "a":
            if player.last_night == "drinking":
                print(
                    ">>>You open the book, confirming it's a journal. You flip to the latest entry and start reading.")
                # sleep(1)
                print(
                    ">>>The more you read the more worried you become. You realize this is a dream journal, and the entry\n"
                    ">>you're reading describes a dream about a night out with friends that is eerily similar to your memory of last night")
                # sleep(2)
                print(
                    ">>>It goes on to describe the walk home with his friend, Bolbis, when suddenly they were both attacked.")
            elif player.last_night == "fighting":
                print(
                    ">>>You open the book, confirming it's a journal. You flip to the latest entry and start reading.")
                # sleep(1)
                print(
                    ">>>The more you read the more worried you become. You realize this is a dream journal, and the entry\n"
                    ">>you're reading describes a dream about the mans drunk friend, Bolbis, instigating several brawls\n"
                    ">>before being kicked out of the pub. It seems like it's the same as your night")
                # sleep(3)
                print(">>>It goes on to describe the walk home with his friend when suddenly they were both attacked.")
            elif player.last_night == "racing":
                print(
                    ">>>You open the book, confirming it's a journal. You flip to the latest entry and start reading.")
                # sleep(1)
                print(
                    ">>>The more you read the more worried you become. You realize this is a dream journal, and the entry\n"
                    ">>you're reading describes a dream about a night out racing with his friend, Bolbis. You realize this\n"
                    ">>is exactly what you remember from last night")
                # sleep(3)
                print(
                    ">>>As you read on evey detail is the same, down to the end when he falls off a cliff, except in his\n"
                    ">>dream he describes falling for what felt like days")
            if player.last_night == "stealing":
                print(
                    ">>>You open the book, confirming it's a journal. You flip to the latest entry and start reading.")
                # sleep(1)
                print(
                    ">>>The more you read the more worried you become. You realize this is a dream journal, and the entry\n"
                    ">>you're reading describes a dream about a night out attempting to break into the home of one of the\n"
                    ">>wealthiest families in town. You're struck by the similarity to your previous night.")
                # sleep(3)
                print(
                    ">>>The entry goes on to describe getting caught by the Fren of the house, whatever that means, and getting\n"
                    ">>beaten badly. It goes on a little further though to describe a bright flash of light and the sensation\n"
                    ">>of falling before waking up")
        if which_book.lower() == "b" and BigMap in playerinven.content:
            print(">>>You already took the map, better try something else")
            SearchBookshelf()
        if which_book.lower() == "b":
            print(">>>You reach up to the top of the bookshelf and grab what looks like a bundle of maps.")
            print(
                ">>>You open one and upon further inspection it is indeed a map, but it's a map of a town called Yhiddenhaal.\n"
                ">>You don't recognize the name.")
            # sleep(1)
            print("Keep looking at maps?")
            keep_looking_maps = input("Y/N:  ")
            static_options(keep_looking_maps)
            if keep_looking_maps.lower() == "y":
                print(
                    f">>>You open the next scroll. It's a larger scale map of what looks like a desert on one side and coastline\n"
                    ">>on the other. After a moment of searching you find Yhiddenhaal on the map. In an area named\n"
                    ">>The Cullver Lands a few hundred miles from both the coast and desert. Everything about these maps\n"
                    ">>seems familiar.")
                print("Would you like to take the map with you?")
                take_map = input("Y/N: ")
                static_options(take_map)
                if take_map.lower() == "y":
                    playerinven.add_item(BigMap)
                    print(">>>You hold onto the map just in case")
                    print("~~Map added~~")
                    SearchBookshelf()
                if take_map.lower() == "n":
                    print("You don't see the point in taking the map with you")
                    SearchBookshelf()
            if keep_looking_maps.lower() == "n":
                print(">>>You decide to move on to something else")
                SearchBookshelf()
        if which_book.lower() == "c" and HistoryBook in playerinven.content:
            print(">>>You already took that")
            SearchBookshelf()
        if which_book.lower() == "c" and DoorKey1 not in playerinven.content and Door1.locked:
            print(">>>You pull the book out and after a quick flip through a key falls out!")
            playerinven.add_item(DoorKey1)
            print("~~Door Key Added~~")
            SearchBookshelf()
        if which_book.lower() == "c" and DoorKey1 in playerinven.content:
            print(">>>You were so excited about the key you forgot to read the book that held it.")
            print("what would you like to do with the booK?")
            print("a. Read it now")
            print("b. Take it for later")
            print("c. Go back to searching bookshelf")
            aai = input("Enter choice here: ")
            static_options(aai)
            if aai.lower() == "a":
                print(">>>Story go brrrr. probably a creation story that resembles player characters own")
                SearchBookshelf()
            if aai.lower() == "b":
                print(">>>You stash the book for later and go back to what you were doing")
                playerinven.add_item(HistoryBook)
                print("~~Book added~~")
                SearchBookshelf()
            if aai.lower == "c":
                print(">>>You've got more important things to worry about right now")
                SearchBookshelf()
        if which_book.lower() == "d":
            print(">>>You decide to try something else")
            SearchRoom()
        if which_book.lower() == "e" and FaerieTales not in playerinven.content and player.backstory == "Noble":
            print(
                ">>>As you pick the book up you realize it's not exactly the book you thought it was. Though similar, the\n"
                ">>opening pages are much like the stories you remember, except they're about humans stealing faerie children.")
            # sleep(2)
            print(
                ">>>Strange indeed. As you flip a few more pages though you come across a story about a faerie who wakes\n"
                ">>up in a strange land that reminds you of a similar tale in the book you remember.")
            # sleep(2)
            print("a. Read the story")
            print("b. Put the book in your pocket to read later and keep searching bookshelf")
            print("c. Stop reading and put the book back where you got it from")
            noble_bookshelf_1 = input("Enter choice here: ")
            static_options(noble_bookshelf_1)
            if noble_bookshelf_1.lower() == "a":
                print(FaerieTales.text)
            if noble_bookshelf_1.lower() == "b":
                playerinven.add_item(FaerieTales)
                print(">>>You slide the book in your pocket and continue searching")
                print("~~Faerie Tales added~~")
                SearchBookshelf()
            if noble_bookshelf_1.lower() == "c":
                print(">>>No sense wasting time on faerie tales anyway")
                SearchBookshelf()
        if which_book.lower() == "e" and FaerieTales in playerinven.content and player.backstory == "Noble":
            print(">>>You already took the book. Check your inventory")
            SearchBookshelf()


# ####~~~~Everything works up to here perfectly~~~~####

def Hallway():
    print("You're in a hallway!")


def HallwaySmash():
    while True:
        if not Door1.intact:
            print(
                ">>>As you step into the hallway, you check both directions for someone coming to check on the noise you just made")
            # sleep(1)
            print(
                ">>>After a second you start to hear footsteps from the right. You look towards the noise and see a corner \n"
                ">>that the footsteps are headed towards.")
            # ##############Rewrite to fit with standard formatting, i.e. a,b,c,d for multiple choice
            print("You have to make a decision quickly do you:\n"
                  "a. Ambush\n"
                  "b. Hide\n"
                  "c. Surrender")
            smash_hallway = input("Enter choice here: ")
            static_options(smash_hallway)
            if smash_hallway.lower() == "a":
                print(
                    ">>>You move towards the corner and prepare yourself to strike. Not but a few seconds later you see them.")
                # sleep(1)
                print(
                    ">>>What comes around the corner takes you by surprise, as a human-like, but definitely not human creature\n"
                    ">>strides into sight.")
                # sleep(1)
                print(
                    ">>>Though appearing feminine, she stands a head taller than you. Her form is extremely lithe and her skin\n"
                    ">>is the light pink of a sunset. She has hair the color of the sea and you think you see some jewelry\n"
                    ">>around her neck and wrists.")
                # sleep(2)
                print(
                    ">>>You don't have time to be taken aback though and you instantly grab the creature and wrestle it to the ground\n"
                    ">>She hits the ground with a dull thud and a small squeak escapes her. You cover her mouth with your hand immediately.")
                # sleep(2)
                print("Would you like to: ")
                print("a. Ask her some questions")
                print("b. Pull her into the room you just came out of")
                print("c. Steal her stuff and run")
                print("d. Knock her out")
                option1 = input("Enter choice here: ")
                static_options(option1)
                if option1.lower() == "a":
                    print(
                        ">>>In hushed tones you say 'I'm not going to hurt you, I just need some information. Blink twice if\n"
                        ">>you understand.' Slowly you see the fear in her eyes fade a little and she blinks twice.")
                    # sleep(1)
                    print(
                        ">>>'Good' you say as you remove your hand. 'Look my name is {player.name} and I have no idea where\n"
                        ">>I am or how I got here and I've never seen anyone like you.'")
                    # sleep(2)
                    print(
                        ">>>'So' you say as you help her to her feet 'First things first, what's your name and have you ever\n"
                        ">>met anyone like me?'")
                    # sleep(2)
                    print(
                        ">>>Now that you've had a second to look at her, you realize there are a lot of similarities between\n"
                        ">>whatever she is and humans. Correct number of fingers and everything. It's really just her frame\n"
                        ">>and skin tone that sets her apart.")
                    # sleep(2)
                    if player.spd > 10:
                        print(
                            ">>>As she gets to her feet, she brushes herself off and turns to address you. Suddenly you see\n"
                            ">>her eyes flash with fury so quickly you barely have time to react as she attempts to slap you")
                        # sleep(1)
                        print(">>>Her fingers graze your cheek and she looks over you for a moment before saying\n"
                              ">>'Hmm, not quite as slow as you look huh?'")
                    else:
                        print(
                            ">>>As she gets to her feet, she brushes herself off and turns to address you. Suddenly you see\n"
                            ">>her eyes flash with fury so quickly you don't have time to react as her hand whips across your cheek")
                        player.hurt(1)
                        player.current_hp()
                        print(">>>She looks down at you with an odd mix of bewilderment and annoyance before speaking\n"
                              ">>'My brother said you would be here. He did not however tell me, you would be such a brute'")
                        # sleep(2)
                        print(
                            ">>>Her accent catches you so off guard you it takes you a minute to realize what she said\n"
                            ">>'I'm sorry ma'am, did you say your brother knew I would be here?' you say in disbelief")
                        # sleep(1)
                        print(">>>She simply nods her head and indicates that you should follow her")
                        # have branch meet back up with other options in current tree and non-smash door hallway tree
                if option1.lower() == "b":
                    print(
                        ">>>You look around quickly for a place to hide. The only place that seems reasonable is back\n"
                        ">>inside the room you just escaped")
                    # sleep(2)
                    print(">>>The only problem is the obvious lack of a doorknob on the door but you don't have much\n"
                          ">>of a choice right now.")
                    # sleep(1)
                    print(">>>Almost as soon as you pull the door closed you hear the footsteps round the corner")
                    print(">>>The footsteps stop for a second before someone calls out\n"
                          ">>'I know you're here. Just come out and I'll explain'")
                    print("What do you do?")
                    print("a. Come out peacefully")
                    print("b. Stay where you are")
                    print("c. Talk through the door")
                    found = input("Enter choice here: ")
                    static_options(found)
                    if found.lower == "a":
                        print(
                            ">>>You realize there's no where to go and you open the door to reveal what looks like a woman\n"
                            ">>except her skin is a light-ish pink color and her hair is blue")
                        # sleep(2)
                        print(
                            ">>>For a moment you can't help but be taken aback. She catches the look in your eye and\n"
                            ">>just smiles at you. Somehow her smile puts you at ease and you relax a little")
                        # (sleep(1)
                        print(">>>'Now then', she says, 'If you'll just follow me we can go see my brother, he's been\n"
                              ">>expecting you.'")
                        # (sleep(1)
                        print(">>>She starts walking down the same hallway she came down without so much as checking\n"
                              ">>if you're following")
                        # sleep(2)
                        print(
                            ">>>You spend a moment considering before following her. She's the only lead you have at the moment")
                        print(
                            ">>>After walking for short time you arrive in front of a door and she gestures towards it\n"
                            ">>'He's in here', she says, 'Make sure to mind your manners'")
                        MeetBro()  # Make sure this makes sense later
                    if found.lower == "b":
                        print(
                            ">>>You're heart is nearly beating out of your chest and you decide to stay right where you are")
                        # sleep(1)
                        print(
                            ">>>After a few more moments you hear a key in the door and before you can react there's a\n"
                            ">>woman in the door way")
                        # sleep(2)
                        print(
                            ">>>Immediately you notice that her skin is a light shade of pink. Not only that, her hair\n"
                            ">>is also the deep blue of the sea.")
                        # sleep(2)
                        print(
                            "She notices you staring and just laughs before saying, 'Trust me, you look pretty weird too,\n"
                            "but I'm here to help you.'")
                    if found.lower == "c":
                        print(">>>You take one deep breath before calling out through the door\n"
                              ">>'Why would I trust you?'")


def MeetBro():
    print("You meet the brother")


def Street():
    print("You're on the street")


Start()
