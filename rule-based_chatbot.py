import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
DESTINATIONS = {
    "Beaches": ["Bali", "Maldives", "Hawaii"],
    "Mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],
    "Cities": ["London", "Paris", "Tokyo"]
}
jokes = [
    "Why don't programmers like nature? It has too many bugs!",
    "Why did the computer go to the doctor? It had a virus!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
]

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def reccomend():
    print(Fore.CYAN + "TravelBot: Beaches, mountains or cities? Choose one!")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)

    if preference in DESTINATIONS:
        suggestion = random.choice(DESTINATIONS[preference])
        print(Fore.GREEN + f"TravelBot: How about {suggestion}?")
        print(Fore.CYAN + "TravelBot: Do you like it? (Yes/No)")
        answer = input(Fore.YELLOW + "You: ").lower()

        if answer == "Yes":
            print(Fore.GREEN + "TravelBot: Great! Enjoy your holiday in {suggestion}!")
        elif answer == "No":
            print(Fore.Red + "TravelBot: No problem! Let's try another.")
        else:
            print(Fore.RED + "TravelBot: Sorry, I don't have those types of destinations.")

        show_help()

# Offer packing tips based on user's destination and duration
def packing_tips():
    print(Fore.CYAN + "TravelBot: Where to?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "TravelBot: How many days?")
    days = input(Fore.Yellow + "You: ")

    print(Fore.GREEN + f"TravelBot: Packing tips for {days} days in {location}:")
    print(Fore.GREEN + "- Pack versatile clothes.")
    print(Fore.GREEN + "- Bring chargers/AC adapters.")                    