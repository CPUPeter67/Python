# Greet the user
print("Hello! I am your AI assistant. What's your name?")

# Get user input
name = input()

# Respond to the user's name
print(f"Nice to meeet you, {name}!")

# Ask a question
print("How are you doing today? (Good/Bad)")
mood = input().lower()

# Use conditional statements to respond based on mood
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feelings into words.")

# End the conversation
print(f"It was nice chatting with you {name}. Have a great day!")
        