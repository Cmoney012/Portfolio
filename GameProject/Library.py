from dataclasses import dataclass

#                                   ####~~~~Functions Used In Classes~~~~####


def let_user_pick(a):
    while True:
        for idx, element in enumerate(a):
            print("{}) {}".format(idx + 1, element))

        g = input("Enter number of desired book to read: ")
        try:
            if 0 < int(g) <= len(a):
                return int(g) - 1
        except ValueError:
            print("Input not recognized, please try again")
            continue


#                                           ####~~~~Classes~~~~####
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


@dataclass
class Books(Items):
    text: str

    def read_book(self):
        print(self.text)


@dataclass
class Inventory:
    content: []
    total_weight: int

    def add_item(self, a):
        self.content.append(a)

    def remove(self, a):
        self.content.remove(a)

    def check_weight(self):
        self.total_weight = 0
        for b in self.content:
            self.total_weight += b.weight
        print(f"The total weight of your inventory is {self.total_weight}")

    def check_inventory(self):
        for a in self.content:
            print(a.name)
        print(f"You have {player.gold} gold")
        self.check_weight()

    def read_book(self):
        book_list = [c for c in self.content if isinstance(c, Books)]
        print("The books in your inventory are: ")
        print(book_list[let_user_pick(book_list)].text)

    def check_description(self):
        print("Which item would you like the description of?")
        print(self.content[let_user_pick(self.content)])


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

    def total_dam(self):
        total_dam = self.equipped.dam + self.dam
        return int(total_dam)

    def check_attr(self):
        print(vars(self))

    def current_hp(self):
        if self.hp < 1:
            print(f"%%%##{self.name} is dead##%%%")
        else:
            print(f"***You have {self.hp}/{self.max_hp} hp remaining***")

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
        print(f"You currently have {player.equipped.name} equipped")
        print("The weapons in your inventory are:")
        for f in playerinven.content:
            if isinstance(f, Weapons):
                print(f.name)
        while True:
            x = input("What would you like to equip?: ")
            for k in self.inventory.content:
                while x.lower() == k.name.lower():
                    if self.equipped != NONE:
                        self.equipped = NONE
                    if self.equipped is NONE:
                        self.equipped = k
                        return self.equipped

    def unequip(self):
        if self.equipped != NONE:
            self.equipped = NONE
            return self.equipped
        else:
            print("You're already unarmed")

    def die(self):
        if self.hp < 1:
            Start()


@dataclass
class Player(Characters):
    backstory: str
    last_night: str


#                              ######################~~~~Exits~~~~######################
Door1 = Exits("Room One", True, True, True, 0)
Window1 = Exits("Room One", True, True, True, 0)

#                              ######################~~~~Items~~~~######################
NONE = Weapons(0, "Nothing", 0, 0, "You have nothing equipped", 0, 0)
Torch = Weapons(4, "Torch", 1, 1, "Lets user see in the dark for awhile", 1, 1)
Hammer = Weapons(5, "Hammer", 5, 1, "Forging hammer you always have on you for some reason", 3, 3)
Dagger = Weapons(6, "Dagger", 5, 1, "Stabby boi go brrrr", 2, 3)
SilverRing = Items(7, "Silver Ring", 10, 1, "A nice ring, might be worth something", 0)
DoorKey1 = Items(200, "Key", 0, 1, "Looks like it might fit in the door", 0)
HouseKey1 = Items(201, "Key", 0, 1, "A very fancy key", 0)
FaerieTales = Books(100, "'Faerie' Tales", 0, 1, "A children's book that seems strange", 0, "story go brr")
BigMap = Books(101, "Map of Varnuul", 0, 1, "Is map", 0, "Do later")
HistoryBook = Books(102, "Origin of Varnuul and the Griisaari", 10, 1, "History according to whoever wrote it", 0,
                    "Do Later")

#                             ######################~~~~Player~~~~######################
playerinven = Inventory([Torch], 0)
for i in playerinven.content:
    i.weight += i.weight
player = Player(1, "", 10, 7, 10, 10, 0, Torch, playerinven, "", "")

#                             ######################~~~~NPC'S~~~~######################
Shae_Orra_Inv = Inventory([DoorKey1, HouseKey1], 0)
Shae_Orra = Characters(10, "Shae-Orra", 7, 7, 3, 10, 30, NONE, Shae_Orra_Inv)

#                           ######################~~~~Sequences~~~~######################
AllCharacters = [player, Shae_Orra]
AllItems = [Torch, Hammer, Dagger, SilverRing, DoorKey1]
AllBooks = [FaerieTales]
AllLists = [AllBooks, AllItems, AllCharacters]


#                        ######################~~~~PlayerCommands~~~~######################

def static_options(a):
    if a.lower() == "hp":
        player.current_hp()
    if a.lower() == "inv":
        playerinven.check_inventory()
    if a.lower() == "eq":
        player.equip()
        print(f"{player.equipped.name} equipped")
    if a.lower() == "read":
        playerinven.read_book()
    if a.lower() == "describe":
        playerinven.check_description()
    if a.lower() == "help":
        print("hp = check your current health\n"
              "inv = check your inventory\n"
              "eq = change your equipped weapon\n"
              "read = choose book to read\n"
              "describe = check items description\n"
              "help = check the commands")


#                   ######################~~~~Functions That Use Classes~~~~######################

def Fight(a, b):
    while True:
        x = a.dam + a.equipped.dam
        y = b.dam + b.equipped.dam
        if b.hp < 1:
            # print(f"You successfully defeat {b.name}.")
            break
        if a.hp < 1:
            print("You lost the fight")
            a.die()
        else:
            a.current_hp()
            b.current_hp()
            print("Do you want to keep fighting?")
            keep_fighting = input("Y/N: ")
            if keep_fighting.lower() == "y":
                pass
            if keep_fighting.lower() == "n":
                break
            print(a.spd, b.spd)
            if a.spd > b.spd:
                b.hp -= a.total_dam
                if b.hp < 1:
                    Fight(a, b)
                a.hp -= b.total_dam
                if a.hp < 1:
                    Fight(a, b)
            if b.spd > a.spd:
                a.hp -= b.total_dam
                if a.hp < 1:
                    print("You lost the fight")
                    a.die()
                else:
                    b.hp -= a.total_dam
                    if b.hp < 1:
                        print(f"You successfully defeat {b.name}.")
            if a.spd is b.spd:
                b.hp -= x
                if b.hp < 1:
                    Fight(a, b)
                a.hp -= y
                if a.hp < 1:
                    Fight(a, b)


# Fight(player, Shae_Orra)
