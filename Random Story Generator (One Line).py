print("Welcome to the Mad Lib Generator!")

adjective = input("Please type an adjective: ").lower()
noun = input("Please type a noun: ").lower()
verb = input("Please type a verb: ").lower()
place = input("Please type a place: ")

story = f"One day, a {adjective} {noun} decided to {verb} in the middle of the {place}. it was surprising to say the least!"

print("\nHere is your story:")
print(story)

