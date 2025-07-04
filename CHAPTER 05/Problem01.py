# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up!

translations = {
    "पानी": "water",
    "आग": "fire",
    "धरती": "earth",
    "आसमान": "sky",
    "पेड़": "tree",
    "फूल": "flower",
    "प्यार": "love",
    "दोस्त": "friend",
    "घर": "home",
    "खुशी": "happiness"
}

print(translations)

translate = translations.get(input("Enter the Hindi word you want to translate: "))

if translate:
    print(f"The english translation is: {translate}")
else:
    print("Sorry, the word is not in the dictionary.")