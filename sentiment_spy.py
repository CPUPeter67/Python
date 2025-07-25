import colorama
from colorama import Fore, Style
from textblob import TextBlob

# Initialize colorama for colored output
colorama.init()

# Emojis for the start of the program
print(f"{Fore.CYAN}👋🎉 Welcome to Sentiment Spy! {Style.RESET_ALL}")

user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "Mystery User" # Fallback if user dosen't provide a name

# Store conversations as a list of tuples: (text, polarity, sentiment_type)
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a sentence and I will analyze your sentences with TextBlob and show you the sentiment. 🔎")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, "
      f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a valid command.{Style.RESET_ALL}")
        continue

    # Check for commands 
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE} Exiting Sentiment Spy. Farewell, Agent {user_name}! {Style.RESET_ALL}")
        break

    elif user_input