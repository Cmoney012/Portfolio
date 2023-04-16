#Names: Ren-Orrin(brother), Shae-Orra(sister)
#Dictionary: Spiritling - name given to a certain type of creature from fae childrens tales. Typically pale fae like creatures.
#
#
#
#
#
#So, since I wanted to make a game where the player would exist in a
#room and be able to interact with multiple different objects, and I
#wanted some of those actions to be contextual to the players decisions,
#I thought the best way to do that would be to define functions that
#act like different objects and put them inside a function that acted
#like a sort of nexus between the objects in a room. This certainly
#wasn't my first thought though xD
#Anyway, once I settled on this design of importing from my Library file
#and Game_Script for things I thought it might be helpful to do things
#like this if/when I need my "Nexus" functions to interact. I'm sure there's
#a better way

#I just had the idea that instead of using functions to define my rooms, to define my rooms as classes and have the
#interactable objects in the room assigned as attributes. I could then use methods to define interactions, and having
#a room be a class I think would make it easier to allow the things inside i.e. attributes to interact

#Been thinking about how to deal with inputs that aren't directly accounted for. so far ive been doing else
#statements to catch rogue inputs but that means for every decision tree I need something to loop back to.
#I guess this means every tree needs to be a function.
#Maybe a better idea is to make a class named Events and make every tree an object with that class. Then
#I could just program a method that prints "input not recognized, please try again" that loops back to self?
#Making events a class would also allow me to easily handle the global player commands with a few methods

#I swear the bookshelf was working earlier but if you choose option c on the bookshelf and then try
#the door it should give you the option to escape. For some reason my dream journal part loops back
#to SelfIndex. I should've never tried to make it better xD

#Maybe making my more complex decision trees into dictionaries will allow me to
#have more control than getting buried five indents deep into an if/else tree

#Since last entry I've done a lot. figured out how to trigger events only once or only if you haven't taken the item that
#Triggers it. also added an option to window that increments. allow player to not leave the room after they open an exit,
#but still show the option to leave next time. Orphan window tree feeds into regular window tree so they can look out the
#window without repeating code. rogue inputs have been handled with while loops. decided instead of using classes for events
#(which I did try for hours) just making exits and other important objects in rooms into classes is better. It works!

# Using wrapper functions, implement global player options by making a function that contains instructions on what to do
# if one of the global options is input by the player, and use it to wrap all functions that request an input...?
