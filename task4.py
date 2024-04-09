#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""





print("Today we picked apple from _PERSON_'s Orchard.")
per1 = input()

print("I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples")
adj1 = input()

print(" straight off the tree that tasted like _FOOD_.")
food1 = input()

print("Then there was a _ADJECTIVE_ apple")
adj2 = input()

print("that looked like a _NOUN_.")
noun1 = input()

print("When our bag was full, we went on a free hay ride to _PLACE_ and back.")
place1 = input()

print("It ended at a hay pile where we got to _VERB_")
verb1 = input()

print("_ADVERB_. ")
adv1 = input()

print("I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_")
food2 = input()

print("and _THINGS_ pies!")
things1 = input()





print(f"Today we picked apple from {per1} Orchard. I had no idea there were so many different varieties of apples. I ate {adj1} apples straight off the tree that tasted like {food1}. Then there was a {adj2} apple that looked like a {noun1}.  When our bag was full, we went on a free hay ride to {place1} and back. It ended at a hay pile where we got to {verb1} {adv1}. I can hardly wait to get home and cook with the apples. We are going to make apple {food1} and {things1} pies!")






