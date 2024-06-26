animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)
#{'zebras': 8, 'monkeys': 12, 'dinosaurs': 0}

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

#create a variable called zipped_drinks that is an iterator of pairs between the drinks list and the caffeine list.
zipped_drinks = zip(drinks, caffeine)

# Create a dictionary called drinks_to_caffeine by using a dict comprehension that goes through
# the zipped_drinks iterator and turns each tuple pair into a key:value item.
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

###########

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Using a dict comprehension, create a dictionary called plays that goes through zip(songs, playcounts) 
# and creates a song:playcount pair for each song in songs and each playcount in playcounts.
plays = {key:value for key, value in zip(songs, playcounts)}

print(plays)
#{'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 89, 'Good Vibrations': 5}

# add a new entry
plays["Purple Haze"] = 1

# update 
plays["Respect"] = 94

# Create a dictionary called library that has two key: value pairs: 
# key "The Best Songs" with a value of plays, the dictionary you created, key "Sunday Feelings" with a value of an empty dictionary
library ={"The Best Songs": plays, "Sunday Feelings": {}}

print(library)
#{'The Best Songs': {'Like a Rolling Stone': 78, 'Satisfaction': 29, 'Imagine': 44, "What's Going On": 21, 'Respect': 94, 'Good Vibrations': 5, 'Purple Haze': 1}, 'Sunday Feelings': {}}

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
# get the key
print(zodiac_elements["earth"])
#['Taurus', 'Virgo', 'Capricorn']
print(zodiac_elements["fire"])
#['Aries', 'Leo', 'Sagittarius']

# check if a key exists
if 'energy' in zodiac_elements:
  print(zodiac_elements["energy"])

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
#.get() method to search for a value, 
# you can also specify a value to return if the key doesn’t exist
tc_id = user_ids.get('teraCoder', 100000)
print(tc_id)
#100019

#.pop() works to delete items from a dictionary, when you know the key value
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
# In one line, add the corresponding value of the key "stamina grains" to the health_points variable
# and remove the item "stamina grains" from the dictionary.
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("mystic bread", 0)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
# built-in list() function return only keys
#.keys() method returns a dict_keys object
# A dict_keys object is a view object, which provides a look at the current state of the dictionary,
# without the user being able to modify anything
# but it can be used in the place of a list for iteration
users = user_ids.keys()
print(users)
#dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
lessons = num_exercises.keys()
print(lessons)
#dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
#.values() method that returns a dict_values object
total_exercises = 0
for i in num_exercises.values():
  total_exercises += i

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
# you can get both the keys and the values with the .items() method
for key, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + key + "s.")

####################

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

# The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.
spread["past"] = tarot.pop(13)

# The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.
spread["present"] = tarot.pop(22)

# The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your " + str(key) + " is the " + str(value) + " card.")

  #Your past is the Death card.
  #Your present is the The Fool card.
  #Your future is the Wheel of Fortune card.


