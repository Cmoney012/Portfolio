####~~~~Imports~~~~####
from time import sleep
from dataclasses import dataclass


#                                   ####~~~~Functions Used In Classes~~~~####


def total_weight(a):
    x = [b.weight for b in a.content]
    sum(x)
    return x


def let_user_pick(a):
    while True:
        for idx, element in enumerate(a):
            print("{}) {}".format(idx + 1, element))

        g = input("Enter number that corresponds with your selection: ")
        try:
            if 0 < int(g) <= len(a):
                return int(g) - 1
        except ValueError:
            print("Input not recognized, please try again")
            continue


#                                           ####~~~~Classes~~~~####
# Would be potentially helpful to have a subclass of locations named Rooms. i.e. location name would be like Shae-Orra's
# house, and subclass would be named Guest bedroom (where player starts). This might help allow more interactions between
# rooms that are in the same location. for instance, I could add a static option called explore and based on your location
# it could give you the rooms within that location. I could also use my existing exits class to prevent player from going
# places they can't yet
# upon trying I ran ito the issue that say I made a subclass tree like this:
# World --> Country(World) --> Town(Country) --> Street(Town) --> Building(Street) --> Room(Building)
# The parent class would have to be the lowest


@dataclass
class Exits:
    location: str
    locked: bool
    intact: bool
    trap: bool
    misc: int

    def unlock(self):
        self.locked = False

    def smash(self):
        self.intact = False

    def disarm(self):
        self.trap = False

    def change_misc(self, a=1):
        self.misc += a


@dataclass
class Rooms:
    id: int
    name: str
    npcs: []
    items: []
    exits: []


@dataclass
class Buildings(Rooms):
    rooms: []


@dataclass
class Items:
    key: int
    name: str
    val: int
    amount: int
    description: str
    weight: int

    def __repr__(self):
        return self.name

    def read_description(self):
        print(self.description)


@dataclass
class Weapons(Items):
    dam: int
    eq: bool

    def __repr__(self):
        return self.name


@dataclass
class Books(Items):
    text: str

    def __repr__(self):
        return self.name

    def read_book(self):
        print(self.text)


@dataclass
class Inventory:
    content: []
    max_weight: int
    total_weight: int

    def total_weight(self):
        total_weight(self)

    def add_item(self, a):
        while True:
            if self.total_weight + a.weight > self.max_weight:
                print("That item weighs too much")
                print("Would you like to drop something?")
                g = input("Y/N: ")
                if g.lower() == "y":
                    self.drop_item()
                if g.lower() == "n":
                    break
            else:
                self.content.append(a)
                print(f"~~~{a.name} added to inventory~~~")
                self.total_weight += a.weight
                return self.total_weight

    def check_weight(self):
        self.total_weight = 0
        for b in self.content:
            self.total_weight += b.weight
        print(f"The total weight of your inventory is {self.total_weight}/{self.max_weight}")

    def check_inventory(self):
        for a in self.content:
            print(a.name)
        print(f"You have {player.equipped.name} equipped")
        print(f"You have {player.gold} gold")
        self.check_weight()

    def read_book(self):
        book_list = [c for c in self.content if isinstance(c, Books)]
        print("The books in your inventory are: ")
        print(book_list[let_user_pick(book_list)].text)

    def check_description(self):
        items_list = [a.description for a in self.content]
        print("Which item would you like the description of?")
        print(items_list[let_user_pick(self.content)])

    def drop_item(self):
        # make so if equipped weapon is dropped, it is unequipped
        print("Which item would you like to drop?")
        while True:
            for idx, element in enumerate(self.content):
                print("{}) {}".format(idx + 1, element))

            g = input("Enter number that corresponds with your selection: ")
            try:
                if 0 < int(g) <= len(self.content):
                    if self.content[(int(g) - 1)] == player.equipped:
                        print("Are you sure you want to drop your equipped weapon?")
                        tu = input("Y/N: ")
                        if tu.lower() == "y":
                            print(f"{player.equipped.name} unequipped and dropped")
                            player.equipped = NONE
                            player.location.items.append(self.content[(int(g) - 1)])
                            self.content.pop(int(g) - 1)
                            break
                        if tu.lower() == "n":
                            print("You decide it's better to keep that for now")
                            break
                    else:
                        h = input(f"You'd like to drop {self.content[(int(g) - 1)]}?\n"
                                  f"Y/N: ")
                        if h.lower() == "y":
                            player.location.items.append(self.content[(int(g) - 1)])
                            self.content.pop(int(g) - 1)
                            break
                        if h.lower() == "n":
                            c = input("Would you like to drop something else?\n"
                                      "Y/N: ")
                            if c.lower() == "y":
                                self.drop_item()
                            if c.lower() == "n":
                                break
            except ValueError:
                print("Input not recognized, please try again")
                continue

    def remove(self, a):
        self.content.remove(a)


@dataclass
class Characters:
    id: int
    name: str
    max_hp: int
    hp: int
    dam: int
    spd: int
    gold: int
    equipped: Weapons
    inventory: Inventory
    location: Rooms

    def total_dam(self):
        total_dam = self.equipped.dam + self.dam
        return total_dam

    def check_attr(self):
        print(f"Name: {self.name}\n"
              f"Hp: {self.hp}/{self.max_hp}\n"
              f"Strength: {self.dam}\n"
              f"Speed: {self.spd}\n"
              f"Equipped: {self.equipped.name}\n"
              f"Damage: {self.dam + self.equipped.dam}\n"
              f"Location: {self.location.name}")

    def current_hp(self):
        if self.hp < 1:
            print(f"%%%##{self.name} is dead##%%%")
        else:
            print(f"***{self.name} has {self.hp}/{self.max_hp} hp remaining***")

    def add_gold(self, a):
        self.gold += a
        print(f"You now have {self.gold} gold")

    def add_max_hp(self, a=1):
        self.max_hp += a
        print(f"Your max hit points is now {self.max_hp}")

    # Could do heal and hurt in one method but prefer this for now. probably change later
    def heal(self, a=1):
        self.hp += a
        self.current_hp()

    def hurt(self, a=1):
        self.hp -= a
        self.current_hp()

    def add_dam(self, a=1):
        self.dam += a

    def add_spd(self, a=1):
        self.spd += a

    def equip(self):
        weps = [v for v in self.inventory.content if isinstance(v, Weapons)]
        print(f"You currently have {player.equipped.name} equipped")
        print("The weapons in your inventory are:")
        player.equipped = weps[let_user_pick(weps)]
        print(f"{player.equipped.name} equipped")

    def unequip(self):
        if self.equipped != NONE:
            self.equipped = NONE
            return self.equipped
        else:
            print("You're already unarmed")

    def die(self):
        if self.hp < 1:
            start()

    def look(self):
        print("You look around a bit and see:")
        if len(self.location.items) > 0:
            while True:
                print("0) None")
                for idx, element in enumerate(self.location.items):
                    print(f"{idx+1}) {element}")

                g = input("Which item would you like to pick up?: ")
                if g == str(0):
                    print("You decide to leave it for now")
                    break
                try:
                    if -1 < int(g) <= len(self.location.items):
                        if self.inventory.total_weight + self.location.items[
                            (int(g) - 1)].weight > self.inventory.max_weight:
                            print("That item weighs too much")
                            print("Would you like to drop something?")
                            g = input("Y/N: ")
                            if g.lower() == "y":
                                self.inventory.drop_item()
                            if g.lower() == "n":
                                print("It's not worth it")
                                break
                        else:
                            player.inventory.add_item(self.location.items[(int(g) - 1)])
                            self.location.items.pop(int(g) - 1)
                            break

                except ValueError:
                    print("Input not recognized, please try again")
                    continue
        else:
            print("You don't see anything")


@dataclass
class Player(Characters):
    backstory: str
    last_night: str


#                              ######################~~~~Exits~~~~######################

Door_Guest_Shae = Exits("Room One", True, True, True, 0)
Window_Guest_Shae = Exits("Room One", True, True, True, 0)

#                              ######################~~~~Items~~~~######################

NONE = Weapons(0, "Nothing", 0, 0, "You have nothing equipped", 0, 0, False)
Torch = Weapons(4, "Torch", 1, 1, "Lets user see in the dark for awhile", 1, 1, False)
Hammer = Weapons(5, "Hammer", 5, 1, "Forging hammer you always have on you for some reason", 3, 3, False)
Dagger = Weapons(6, "Dagger", 5, 1, "Stabby boi go brrrr", 2, 3, False)
SilverRing = Items(7, "Silver Ring", 10, 1, "A nice ring, might be worth something", 0)
DoorKey1 = Items(200, "Key", 0, 1, "Looks like it might fit in the door", 0)
HouseKey1 = Items(201, "Key", 0, 1, "A very fancy key", 0)
FaerieTales = Books(100, "'Faerie' Tales", 0, 1, "A children's book that seems strange", 0, "story go brr")
BigMap = Books(101, "'Map of Varnuul'", 0, 1, "Is map", 0, "Do later")
HistoryBook = Books(102, "'Origin of Varnuul and the Griisaari'", 10, 1, "History according to whoever wrote it", 0,
                    "Do Later")

#                            ######################~~~~Locations~~~~######################

bedroom_guest = Rooms(1, "Guest Bedroom", [], [], [Door_Guest_Shae, Window_Guest_Shae])
hallway_shaeorra = Rooms(2, "Hallway", [], [], [])
bedroom_humvir = Rooms(3, "Humvir's Bedroom", [], [], [])
bedroom_shaeorra = Rooms(4, "Shae-Orra's Bedroom", [], [], [])
house_shaeorra = Buildings(500, "Shae-Orra's House", [], [], [],
                           [bedroom_guest, hallway_shaeorra, bedroom_humvir, bedroom_shaeorra])

#                             ######################~~~~Player~~~~######################

playerinven = Inventory([], 15, 0)
playerinven.add_item(Torch)
for i in playerinven.content:
    i.weight += i.weight
#            id, name, maxhp, hp, dam, spd, gold, eq, inv, backstory, last_night
player = Player(1, "", 30, 20, 5, 10, 0, NONE, playerinven, bedroom_guest, "", "")

#                             ######################~~~~NPC'S~~~~######################

Shae_Orra_Inv = Inventory([DoorKey1, HouseKey1], 15, 0)
Shae_Orra_Inv.add_item(Dagger)
Shae_Orra = Characters(10, "Shae-Orra", 17, 17, 3, 10, 30, NONE, Shae_Orra_Inv, bedroom_guest)

#                           ######################~~~~Sequences~~~~######################

AllCharacters = [player, Shae_Orra]
AllItems = [SilverRing, DoorKey1, HouseKey1]
AllBooks = [FaerieTales, BigMap, HistoryBook]
AllWeapons = [Torch, Hammer, Dagger]
AllLists = [AllCharacters, AllItems, AllWeapons, AllBooks]


#                        ######################~~~~PlayerCommands~~~~######################


def static_options(a):
    if a.lower() == "hp":
        player.current_hp()
    if a.lower() == "inv":
        playerinven.check_inventory()
    if a.lower() == "eq":
        player.equip()
    if a.lower() == "read":
        playerinven.read_book()
    if a.lower() == "describe":
        playerinven.check_description()
    if a.lower() == "drop":
        playerinven.drop_item()
    if a.lower() == "look":
        player.look()
    if a.lower() == "stats":
        player.check_attr()
    if a.lower() == "help":
        print("hp = check your current health\n"
              "inv = check your inventory\n"
              "eq = change your equipped weapon\n"
              "read = choose book to read\n"
              "describe = check items description\n"
              "drop = drop item\n"
              "look = check around for items\n"
              "help = check the commands")


#                   ######################~~~~Functions That Use Classes~~~~######################


def Fight(a, b):
    while True:
        a.current_hp()
        print(f"    ***{a.name}'s speed is {a.spd}***")
        b.current_hp()
        print(f"    ***{b.name}'s speed is {b.spd}***")
        print("Do you want to keep fighting?")
        keep_fighting = input("Y/N: ")
        if keep_fighting.lower() == "y":
            pass
        if keep_fighting.lower() == "n":
            break
        if a.spd > b.spd:
            b.hp -= a.total_dam()
            if b.hp < 1:
                print(f"You successfully defeat {b.name}.")
                b.location.items.extend(b.inventory.content)
                break
            a.hp -= b.total_dam()
            if a.hp < 1:
                print("You lost the fight")
                a.die()
        if b.spd > a.spd:
            a.hp -= b.total_dam()
            if a.hp < 1:
                print("You lost the fight")
                a.die()
            b.hp -= a.total_dam()
            if b.hp < 1:
                print(f"You successfully defeat {b.name}.")
                b.location.items.extend(b.inventory.content)
                break
        if a.spd is b.spd:
            b.hp -= a.total_dam()
            if b.hp < 1:
                print(f"You successfully defeat {b.name}.")
                b.location.items.extend(b.inventory.content)
                break
            a.hp -= b.total_dam()
            if a.hp < 1:
                print("You lost the fight")
                a.die()


seper = "------------------------------------------------------------------------------------------------------------------\n"

#                            ######################~~~~Events~~~~######################


def start():
    while True:
        print("   >>>Welcome to 'Tales of the Griisaari'!<<<")
        print("         >>>Would you like to play?<<<")
        play = input("Y/N: ")
        if play.lower() == "y":
            print(">>>Great!")
            print(
                f"{seper}***If you ever want to see what options you have at any point, type Help and a list of commands will pop up***")
            player.name = input("What is your name?: ")
            print(
                f"{seper}>>>Welcome, {player.name}, to 'Tales of the Griisaari. You are from a town in the Hidden Vale known\n"
                f">>as Trostenwald.")
            # sleep(2)
            print(f"{seper}>>>You live a normal life, with little out of the ordinary occurring around you. That is\n"
                  ">>until a few days after your twenty-fourth name day, when after a wild night, your adventure begins!")
            backstory()
        if play.lower() == "n":
            print("Maybe next time eh?")
            quit()


def backstory():
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
            playerinven.add_item(Hammer)
            setattr(player, "backstory", "Blacksmith")
            last_night()
        if backstory_choice.lower() == "b":
            print(">>>You find your dagger tucked in your belt, you feel a bit less anxiety")
            playerinven.add_item(Dagger)
            setattr(player, "backstory", "Orphan")
            last_night()
        if backstory_choice.lower() == "c":
            print(">>>The clinking of gold as your fingers brush against your coin purse puts you a little at ease")
            player.add_gold(10)
            setattr(player, "backstory", "Noble")
            last_night()


def last_night():
    while True:
        print(
            ">>>You spend a minute trying to remember what you did last night... You think the memory starts to come back...")
        # sleep(1)
        print("Maybe it was...")
        print("a. Drinking with the boys")
        print("b. Getting into fights")
        print("c. Horse racing at night")
        print("d. Stealing from people")
        last_night_ = input("Enter answer here: ")
        static_options(last_night_)
        if last_night_.lower() == "a":
            setattr(player, "last_night", "drinking")
            player.add_max_hp()
            print("-+-Your Max Hp has raised a little-+-")
            # sleep(1)
            print(
                ">>>Its starting to come back now, the loud bar and the smell of ale. The last thing you remember is your\n"
                ">>friend Bulban yelling for help...")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            self_index()
        if last_night_.lower() == "b":
            setattr(player, "last_night", "fighting")
            player.add_dam()
            print("-+-Your Damage has raised a little-+-")
            # sleep(1)
            print(
                ">>>Its starting to come back now, yelling and cursing, fist and feet everywhere. Why did you let Bulban\n"
                ">>go out after he'd been drinking?")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            self_index()
        if last_night_.lower() == "c":
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
            self_index()
        if last_night_.lower() == "d":
            # sleep(1)
            setattr(player, "last_night", "stealing")
            playerinven.add_item(SilverRing)
            print(">>>You reach in your pocket and feel the ring you stole last night")
            # sleep(1)
            print(
                ">>>Of course, the ring. You'd seen lady Nanari with it and decided it would look better on you... her\n"
                ">>husband didn't seem to agree when he caught you trying to sneak in")
            # sleep(1)
            print(">>>You go to stand up and realize how sore you really are")
            self_index()


def self_index():
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
                search_room()
            if player.last_night == "fighting":
                print(
                    ">>>From the way your jaw feels you'd say you lost a fight to someone last night, you can't remember\n"
                    ">>anything past telling Bulban to sod off after he tried to get you to go to the pub last night, and\n"
                    ">>then going anyway for Bulban's sake")
                player.current_hp()
                search_room()
            if player.last_night == "racing":
                print(
                    ">>>You're pretty sure your shoulder is dislocated, but for the fall you took, you actually feel pretty good")
                player.current_hp()
                search_room()
            if player.last_night == "stealing":
                print(
                    ">>>You can almost see the imprint of Sir Tellin's boots on your ribs as you inspect yourself for injuries.\n"
                    ">>Come to think of it, how do you still have the ring?")
                player.current_hp()
                search_room()
        if check_self.lower() == "n":
            print(">>>Tis but a scratch, you'll deal with it later")
            print("***To check your current hp in the future, type hp into any prompt***")
            search_room()


def search_room():
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
            search_window()
        if checkroom.lower() == "b":
            search_door()
        if checkroom.lower() == "c":
            search_bookshelf()


def search_window():
    while True:
        if Window_Guest_Shae.misc == 0:
            print(
                ">>>You step towards the window, from the sun you can tell it's early in the morning. It takes you a moment to realize... ")
            # sleep(1)

            print(
                ">>>You look down on an unfamiliar town. From the third story of the building you're in, you can see\n"
                ">>that the city is quite large, roughly the same size of Trostenwald from what you can see")
            Window_Guest_Shae.change_misc()
        else:
            print("What would you like to do?")
            print("a. Keep looking through the window for awhile")
            print("b. Search something else")
            if player.backstory == "Blacksmith":
                print("c. Try smashing the window")
            window_choice = input("Enter choice here: ")
            static_options(window_choice)
            if window_choice.lower() == "a" and Window_Guest_Shae.misc == 0:
                print(">>>You spend a minute or so looking through the window before you see someone coming down\n"
                      ">>the street. You're thinking about calling out to them before you notice something strange")
                # sleep(1)
                print(">>>The figure seems much taller than a normal person, but more than that you notice their\n"
                      ">>skin looks blue...")
                # sleep(1)
                print(">>>As you look closer you realize their hair is also light pink. You rub your eyes and look\n"
                      ">>again but nothing changes. You stare until he rounds a corner")
                # sleep(1)
                Window_Guest_Shae.change_misc(1)
                search_window()
            if window_choice.lower() == "a" and Window_Guest_Shae.misc == 1:
                print(">>>You can't resist taking another look through the window")
                # sleep(1)
                print(">>>You spend another minute waiting before someone else comes into view. This time it's a pair of\n"
                      ">>women. Their skin appears to be a pale pink. They walk by without appearing to notice you. 'What is going on?'")
                Window_Guest_Shae.change_misc(1)
                # sleep(3)
                search_window()
            if window_choice.lower() == "a" and Window_Guest_Shae.misc == 2:
                # Potentially add more stuff here
                print(">>>You spend a few more minutes looking through the window but no one else appears, strange.")
                search_window()
            if window_choice.lower() == "b":
                print(">>>You feel like you've got bigger things to attend to")
                search_room()

            if window_choice.lower() == "c" and player.backstory == "Blacksmith" and Window_Guest_Shae.intact:
                Window_Guest_Shae.smash()
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
                    street()
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
                            meet_rem_caught()

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
                            meet_rem_caught()

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
                                street()

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
                                    meet_rem_caught()

                                    if t.lower() == "b":
                                        print(
                                            ">>>Before she can react you rush headlong out of the broken window. You do your best\n"
                                            ">>to keep your balance but in your haste your foot slips")
                                        # sleep(1)
                                        print(
                                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                                        player.hurt(3)
                                        street()
                                        # Work on details of this way out later

                    if x.lower() == "b":
                        print(">>>You're unconvinced. You decide to continue escaping out of the window")
                        # sleep(1)
                        print(
                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                        player.hurt(3)
                        street()

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
                            street()

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
                            meet_rem_caught()

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
                        meet_rem_caught()
                    if z.lower() == "b":
                        print(
                            ">>>You don't like her answer. You quickly mantle the window sill and in your haste lose your balance")
                        # sleep(1)
                        print(
                            ">>>You fall for what seems like ages until the hard cobblestones meet you with bone crunching force")
                        player.hurt(3)
                        street()


def SearchWindowOrphan():
    if not Window_Guest_Shae.locked:
        print("The window is open, would you like to go through it?")
        leave = input("Y/N:  ")
        static_options(leave)
        if leave == "y":
            print(">>>You leap through the window and make your way down to the street without issue")
            street()
        if leave == "n":
            print(">>>You decide to look around a little more")
            search_window()
    else:
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
            Window_Guest_Shae.unlock()
            print(">>>You try to slide your knife between the sill and the glass.")
            # sleep(2)
            print(">>>After a few moments you manage to slide the blade of your knife under the window and pop it open")
            # sleep(1)
            print("Would you like to climb through? ")
            leave = input("Y/N: ")
            static_options(leave)
            if leave.lower() == "y":
                print(
                    ">>>Carefully you pull yourself through the open window. You don't see anyone on the street below\n"
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
                    rooftops()
                if orph_esc.lower() == "b":
                    print(
                        ">>>You expect you might draw far too much attention on the roofs, not to mention the constant\n"
                        ">>danger of falling")
                    # sleep(1)
                    print(
                        ">>>You deftly scale down the face of the building you're on and after a few moments, your boots\n"
                        ">>hit solid ground.")
                    street()
                if orph_esc.lower() == "c":
                    print(
                        ">>>You decide it might be a good idea to look around some more before you decide to take off.\n"
                        ">>Without trouble you slide back through the window")
                    search_room()
            if leave.lower() == "n":
                search_window()
        if OrphanWindow.lower() == "n":
            print(
                ">>>You decide it's probably better to look for a way out that doesn't risk a thirty foot fall")
            search_window()


def search_door():
    while True:
        # Figure out the best way to get approach message to trigger once
        print(">>>You approach the door")
        if not Door_Guest_Shae.locked or not Door_Guest_Shae.intact:
            print("Would you like to leave the room?")
            opendoor = input("Y/N: ")
            static_options(opendoor)
            if opendoor.lower() == "y":
                print(">>>You slowly open the door to reveal a long hallway")
                if Door_Guest_Shae.intact:
                    hallway_shae()
                if not Door_Guest_Shae.intact:
                    hallway_smash_shae()
            if opendoor.lower() == "n":
                print(">>>You decide you may not be done in here yet")
                search_room()
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
                Door_Guest_Shae.unlock()
                search_door()
            if key_use.lower() == "n":
                print(">>>You're not sure if you're done here yet")
                search_door()
        if player.backstory == "Blacksmith" and Door_Guest_Shae.locked and Door_Guest_Shae.intact:
            print(">>>You don't like the look of that door knob, maybe you should just smash it?")
            print("Smash the door?")
            smash_door = input("Y/N: ")
            static_options(smash_door)
            if smash_door.lower() == "y":
                Door_Guest_Shae.smash()
                search_door()
            if smash_door.lower() == "n":
                print(">>>You think that may be a little hasty. Maybe just wiggle the handle to see if it's unlocked?")
                print("Wiggle handle?")
                door_choice = input("Y/N: ")
                static_options(door_choice)
                if door_choice.lower() == "y" and Door_Guest_Shae.trap:
                    player.hurt(1)
                    print(">>>Oww!")
                    print(
                        ">>>As you twist the doorknob you hear a small snap as a trap that was attached to the doorknob activates.\n"
                        ">>You don't think it'll happen again but the door is locked. Better try something else")
                    # sleep(2)
                    Door_Guest_Shae.disarm()
                    search_door()
                if door_choice.lower() == "y" and not Door_Guest_Shae.trap:
                    print(">>>The trap only works once but the door is still locked")
                if door_choice.lower() == "n":
                    print(">>>You decide to leave the door for later")
                    search_room()
        if Door_Guest_Shae.locked:
            print(">>>The handle has a keyhole in it.")
            print("Do you try to twist the doorknob?")
            door_choice = input("Y/N: ")
            static_options(door_choice)
            if door_choice.lower() == "y":
                if Door_Guest_Shae.trap:
                    print(
                        ">>>As you twist the doorknob you hear a small snap as the trap that was attached to the doorknob activates")
                    print(">>>Oww!")
                    player.hurt(1)
                    Door_Guest_Shae.disarm()
                    print(">>>You don't think it'll happen again but the door is locked. Better try something else")
                    search_room()
                if not Door_Guest_Shae.trap:
                    print(">>>The trap only works once but the door is still locked")
                    search_room()
            if door_choice.lower() == "n":
                print(
                    ">>>As you take a second to examine the door knob, you notice a strange button on the backside of the knob,\n"
                    ">>better be careful with that")
                search_room()


def search_bookshelf():
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
            search_bookshelf()
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
                    ">>>You open the next scroll. It's a larger scale map of what looks like a desert on one side and coastline\n"
                    ">>on the other. After a moment of searching you find Yhiddenhaal on the map. In an area named\n"
                    ">>The Cullver Lands a few hundred miles from both the coast and desert. Everything about these maps\n"
                    ">>seems familiar.")
                print("Would you like to take the map with you?")
                take_map = input("Y/N: ")
                static_options(take_map)
                if take_map.lower() == "y":
                    playerinven.add_item(BigMap)
                    print(">>>You hold onto the map just in case")
                    search_bookshelf()
                if take_map.lower() == "n":
                    print("You don't see the point in taking the map with you")
                    search_bookshelf()
            if keep_looking_maps.lower() == "n":
                print(">>>You decide to move on to something else")
                search_bookshelf()
        if which_book.lower() == "c" and HistoryBook in playerinven.content:
            print(">>>You already took that")
            search_bookshelf()
        if which_book.lower() == "c" and DoorKey1 not in playerinven.content and Door_Guest_Shae.locked:
            print(">>>You pull the book out and after a quick flip through a key falls out!")
            playerinven.add_item(DoorKey1)
            search_bookshelf()
        if which_book.lower() == "c" and DoorKey1 in playerinven.content:
            print(">>>You were so excited about the key you forgot to read the book that held it.")
            print("what would you like to do with the booK?")
            print("a. Read it now")
            print("b. Take it for later")
            print("c. Go back to searching bookshelf")
            aai = input("Enter choice here: ")
            static_options(aai)
            if aai.lower() == "a":
                HistoryBook.read_book()
                search_bookshelf()
            if aai.lower() == "b":
                print(">>>You stash the book for later and go back to what you were doing")
                playerinven.add_item(HistoryBook)
                search_bookshelf()
            if aai.lower == "c":
                print(">>>You've got more important things to worry about right now")
                search_bookshelf()
        if which_book.lower() == "d":
            print(">>>You decide to try something else")
            search_room()
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
                search_bookshelf()
            if noble_bookshelf_1.lower() == "c":
                print(">>>No sense wasting time on faerie tales anyway")
                search_bookshelf()
        if which_book.lower() == "e" and FaerieTales in playerinven.content and player.backstory == "Noble":
            print(">>>You already took the book. Check your inventory")
            search_bookshelf()


# ####~~~~Everything works up to here perfectly~~~~####

def hallway_shae():
    setattr(player, "location", hallway_shaeorra)
    print(
        ">>>You look both ways down the hallway, careful to not be seen. From what you can tell, the hallway seems empty")
    # sleep(1)
    print(">>>It seems as though the hallway extends both directions away from you\n"
          "Which way would you like to go?")
    z = input("a. Left\n"
              "b. Right")
    if z.lower() == "a":
        print(">>>You decide to head right first")
        # sleep(1)
        print(
            ">>>As you quietly sneak down the hallway, you listen closely for any sounds that might indicate someone\n"
            ">>is coming. Fortunately, it seems that no one is up and about this early in the morning.")
        # sleep(1)
        print(
            ">>>You pass some doors, which upon inspection appear to be locked. After a little while longer you come\n"
            ">>to a corner. To the left you see more doors, but to the right you see a staircase, heading down.")
        za = input("Do you:\n"
                   "a. Go left down the hallway\n"
                   "b. Go right down the stairs")
        if za.lower() == "a":
            print(
                ">>>You decide to leave the staircase for a bit and head left. After a few steps down the hallway you\n"
                ">>start to hear what sounds like voices. Muffled at first but you can try to get closer and hear what\n"
                ">>they're saying")
            # sleep(1)
            zaa = input("Get closer?\n"
                        "Y/N: ")
            if zaa.lower() == "y":
                print(">>>You decide to try and get a better position to hear what's being said.")
                # sleep(1)
                print(
                    ">>>You slowly creep along the hallway towards the voices. After a moment the muffled sounds become\n"
                    ">>understandable.")
                # sleep(1)
                print(">>>'I can't explain it Shae', you hear a male voice say, 'All I know is these dreams are not normal'")
                # sleep(1)
                print(">>>You hear a woman's voice reply, 'Of course I trust you Ren, but this is so strange', after a \n"
                      ">>brief pause she continues, 'I mean, it's just a children's book'")
                # sleep(1)
                print(">>>The male voice replies, 'I know Shae, I know, but we are beyond coincidence at this point.")
                zaay = input("Do you:\n"
                             "a. Keep listening\n"
                             "b. Knock on the door\n"
                             "c. Back away")
                if zaay.lower() == "a":
                    print(">>>After a tense moment you hear a sigh before the man continues, 'Look, just give it a few more\n"
                          ">>days, if nothing happens before then, I'll let it go'")
                    # sleep(1)
                    print(">>>'Fine, three more days Ren. After that we're leaving. You know how important our mission is'")
                    # sleep(1)
                    print(">>>'Of course, how could I forget'")
                    print(">>>You hear footsteps. You attempt to hide around the corner before you're seen but before you\n"
                          ">>can get to safety, the door opens behind you and you hear a voice call out")
                    # sleep(2)
                    print(f"'{player.name}? Is that you?'\n"
                          "Hearing your name catches you off guard")
                    zaaya = input("Do you:\n"
                                  "a. Keep running\n"
                                  "b. Turn around\n")
                    if zaaya.lower() == "a":
                        print(">>>You keep running for the corner. You've almost made it when you're body suddenly feels heavy.\n"
                              ">>Almost like you're trying to run through molasses. After another moment you're completely stuck\n"
                              ">>mid stride. You wildly struggle against the unseen force but nothing you do seems to have any effect")
                        # sleep(2)
                        print(">>>From behind you hear a woman say, 'Ren, is this the spiritling you're looking for?' As she\n"
                              ">>speaks you're body begins to spin around towards the voices")
                        # sleep(1)
                        if Window_Guest_Shae.misc == 0:
                            print(">>>As she comes into view you're shocked again. Though her general features appear to be human,\n"
                                  ">>her skin looks like she painted herself light pink and her hair is a deep blue")
                            # sleep(1)
                            print(">>>Before you have a chance to process that information, a taller figure joins her.\n"
                                  ">>The figure seems male but his skin seems to match his sisters hair. A moment later you\n"
                                  ">>notice his hair is also the same color as his sisters skin")
                        if Window_Guest_Shae.misc == 1:
                            print(">>>The woman who rounds the corner catches you off guard. Her skin is the same light pink\n"
                                  ">>of the hair of the person you saw out the window earlier.")
                            # sleep(1)
                            print(">>>Before you have time to process what you're seeing, another figure joins the woman.\n"
                                  ">>This one seems male and he matches the man you saw.")
                        if Window_Guest_Shae.misc == 2:
                            print(">>>The woman who comes around the corner has the same skin color as the ladies you saw\n"
                                  ">>out the window earlier, and the man who comes around the corner also has the same complexion\n"
                                  ">>as the man you saw")

                        print(">>>You see the man's face light up as he says, 'Yes! Yes that's him!', he looks at the woman\n"
                              ">>'I know I said he'd be here, but even I was starting to doubt.' as he looks back to you, you see\n"
                              ">>his expression darken before he asks 'Shae, are you holding the man?'")
                        # sleep(1)
                        print(">>>The woman almost sounds bored when she says, 'Well, was I supposed to let him go running\n"
                              ">>through the city? I think we both know how well that would end'")
                        # sleep(1)
                        print(">>>'No,' he replies, 'I suppose not. You're not hurting him are you?'\n"
                              ">>'Do you think you're talking to a novice Rem? I can hold a fly in place without breaking\n"
                              ">>its wing'")
                        # sleep(1)
                        print(">>>You think you see Rem roll his eye's before he turns his attention back to you. 'If she\n"
                              ">>lets you go will you at least listen to what I have to say?'")
                        # sleep(1)
                        zaayaa = input("a. Nod your head in agreement\n"
                                       "b. Tell him to go milk a goat\n"
                                       "c. Stay silent").lower()
                        if zaayaa == "a":
                            print(">>>Realizing there's not many options here you nod your head in agreement.\n"
                                  ">>Rem looks at his sister and you feel the magical energy around you dissipate")
                            # sleep(1)
                            print(">>>You instinctively rub your wrist as Rem continues, 'Now, how about we continue this\n"
                                  ">>conversation in my study.' He turns and walks back through the door he came out of")
                            rems_story()
                        if zaayaa == "b":
                            print(">>>This day has been too much and now you're being treated like a criminal. You can't hold\n"
                                  ">>in your anger anymore, 'Go milk a goat', you hear yourself say almost before you realize it")
                            # sleep(1)
                            print(">>>Rem looks at you a little disappointed before turning to his sister, 'See Shae, this is why\n"
                                  ">>we try to use our words before binding people in mystical forces'")
                            # sleep(1)
                            print(">>>You see Shae roll her eyes before looking back at you, 'Might I recommend you listen to my\n"
                                  ">>brother, I assure you he's the only person you're going to find with your best interest at heart'")
                            # sleep(1)
                            print(">>>You take a second to collect your thoughts before coming to the conclusion that your options are\n"
                                  ">>severally limited. 'Fine', you say, 'I'll hear you out'")
                            # sleep(1)
                            print(">>>'Good', Rem says, 'Now, why don't we continue this in my study?' And you feel the restraints holding\n"
                                  ">>you disappear suddenly. Rubbing your wrists, you follow the strange figures into the room")
                            rems_story()
                        if zaayaa == "c":
                            print(">>>You decide to answer by staring straight into his eyes without blinking")
                            # sleep(1)
                            print(">>>After a tense few moments, you see Rem relax a little before he nods to his sister and suddenly the\n"
                                  ">>restraints holding you disappear")
                            # sleep(1)
                            print(">>>You take a second to collect yourself before looking up at the pair. They return your look before\n"
                                  ">>Rem says, 'I understand, you've had an insane day, but if you don't let me help you, I promise you\n"
                                  ">>It's going to get a lot worse'")
                            # sleep(1)
                            print(">>>They turn and walk into the room. After a few seconds of consideration you accept that your options\n"
                                  ">>are severally limited and you go to follow them")
                        rems_story()
                    if zaaya.lower() == "b":
                        print(">>>You decide it's best to try and get some answers, and if this person knows your name, there's\n"
                              ">>a good chance she knows something about what's going on")
                        # sleep(1)
                        if Window_Guest_Shae.misc == 0:
                            print(">>>You turn around and you're shocked at what you see. The lady in front of you appears mostly\n"
                                  ">>human, except for the pink hue of her skin and her hair is a deep blue you don't recall seeing before")
                            # sleep(1)
                        if Window_Guest_Shae.misc == 1:
                            print(">>>As you turn around, you see a woman unlike any you've seen before. Unlike the man you saw outside\n"
                                  ">>the window before, her skin is a light shade of pink and her hair is a deep blue")
                        if Window_Guest_Shae.misc == 2:
                            print(">>>The woman you see when you turn around has the same pink skin and blue hair of the women you saw\n"
                                  ">>outside the window earlier")
                        print(">>>You see her call through the open door, 'Rem, I think I've found your spiritling'")
                        # sleep(1)
                        if Window_Guest_Shae.misc == 0:
                            print(">>>A moment later you're shocked further when a man with purple skin and light pink hair comes through the door")
                        if Window_Guest_Shae.misc >= 1:
                            print(">>>After a few seconds you see a man with the same purple complexion and pink hair you saw out the window earlier")
                        print(">>>You see the man's face light up as he says, 'Yes! Yes that's him!', he looks at the woman before continuing, 'I know\n"
                              ">>I said he'd be here, but even I was starting to doubt.'")
                        # sleep(1)
                        print(">>>He approaches you with his arm extended and his palm flat out, all the while maintaining eye contact")
                        zaayab = input("Do you:\n"
                                       "a. Stare at him perplexed\n"
                                       "b. Imitate him and hold your arm out")
                        if zaayab == "a".lower():
                            print(">>>He see's the confusion in your eyes and let's out a small laugh. 'Right, humans do it like this', and he holds\n"
                                  ">>out his hand for a handshake")
                            zaayaba = input("Shake his hand? Y/N: ")
                            if zaayaba == "y".lower():
                                print(f">>>You see a smile touch his lips as you hold out your hand to complete the gesture. 'Now then, I'm Rem, and this\n"
                                      f">>person staring a hole in you is my sister, Shae. Obviously we already know your name, {player.name}'")
                                # sleep(1)
                                print(">>>If you wouldn't mind, follow me into my study and I'll explain as much as I know")
                                rems_story()
                            if zaayaba == "n".lower():
                                print(">>>You recognize his intent and simply look him in the eyes. He looks a little uncomfortable but seems to shake it\n"
                                      ">>off. 'I understand you're probably having a pretty bad day, but I'm here to help'")
                                # sleep(1)
                                print(">>>'Look', he continues, 'just come sit in my office and at least hear me out.' His eyes look at you with an unmistakable\n"
                                      ">>sympathy.")
                                # sleep(1)
                                print(">>>You look around and decide your list of options are pretty short and you nod your head towards the man. He smiles and\n"
                                      ">>turns around to lead you into the office")
                                rems_story()
                        if zaayab == "b".lower():
                            print(">>>You don't recognize the gesture but you copy his movements and he presses his palm into yours, makes eye contact and\n"
                                  ">>bows his head. You do the same and he smiles at you before saying, 'My name is Rem, and this is my sister Shae. I know you\n"
                                  ">>must be very confused, but if you'll follow me into my study, I'll tell you what I know'")
                            # sleep(1)
                            print(">>>You nod your head and he turns around and leads you into his office")
                            rems_story()
                if zaay.lower() == "b":
                    print(">>>You think about running at first but as you listen you realize that they're probably talking\n"
                          ">>about you. You're hand shakes as you go to knock on the door but you force yourself to go through\n"
                          ">>with it, after all, if these people know what's going on, you need to talk to them")
                    # sleep(1)
                    print(">>>As you knock you hear the voices go quiet suddenly before you hear steps coming towards the\n"
                          ">>door")
                    if Window_Guest_Shae == 0:
                        print(">>>The two people who come out of the door shock you. One appears to be a tall woman, except\n"
                              ">>her skin is pink and her hair is a dark blue color. Before you can take that in fully a man\n"
                              ">>comes around the corner as well. His skin is a light purple and his hair is pink.")
                        # sleep(1)
                        print(">>>You look between the two of them repeatedly and you see them share a look and a smile")
                    if Window_Guest_Shae == 1 or Window_Guest_Shae == 2:
                        print(">>>")
                if zaay.lower() == "c":
                    print(">>>")
            if zaa.lower() == "n":
                print(">>>")
        if za.lower() == "b":
            print(">>>")
    if z.lower() == "b":
        print(">>>You decide to head left first")


def hallway_smash_shae():
    while True:
        if not Door_Guest_Shae.intact:
            print(
                ">>>As you step into the hallway, you check both directions for someone coming to check on the noise you just made")
            # sleep(1)
            print(
                ">>>After a second you start to hear footsteps from the right. You look towards the noise and see a corner\n"
                ">>that the footsteps are headed towards.")
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
                        f">>>'Good' you say as you remove your hand. 'Look my name is {player.name} and I have no idea where\n"
                        f">>I am or how I got here and I've never seen anyone like you.'")
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
                        player.hurt()
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
                    # sleep(1)
                    print(">>>The only problem is the obvious lack of a doorknob on the door but you don't have much\n"
                          ">>of a choice right now.")
                    # sleep(1)
                    print(">>>Almost as soon as you pull the door closed you hear the footsteps round the corner")
                    print(">>>The footsteps stop for a second before someone calls out\n"
                          ">>'I know you're here. Just come out and I'll explain'")
                    print("Do you: ")
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
                        meet_rem_caught()  # Make sure this makes sense later
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
                            ">>is also the deep blue of the sea")
                        # sleep(2)
                        print(
                            "She notices you staring and just laughs before saying, 'Trust me, you look pretty weird too,\n"
                            "but I'm here to help you.'")
                    if found.lower == "c":
                        print(">>>You take one deep breath before calling out through the door\n"
                              ">>'Why would I trust you?'")
                        # sleep(1)
                        print(
                            f">>>You hear her sigh somewhat dramatically before she says, 'Because {player.name}, me and\n"
                            f">>my brother are the only fae in Varnuul that aren't going to lose their minds when they see you")
                        # sleep(1)
                        print(">>>")


def meet_rem_caught():
    print("You meet the brother")
    quit()


def street():
    print("You're on the street")
    quit()


def rooftops():
    print("You're on the roof")
    quit()


def rems_story():
    print("")
