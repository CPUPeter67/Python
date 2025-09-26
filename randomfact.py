import requests
# Technology category fact endpoint
url = "https://uselessfacts.jsph.pl/random.json?language=en&category=technology" # Function to get a random technology fact
def get_random_technology_fact():
    response=requests.get(url)
    if response.status_code==200:
        fact_data = response.json()
        print(f"Did you know? {fact_data['text']}")
    else:
        print('Failed to fetch a fact. Please try again later.')
# Main loop to interact with the user
while True:
    user_input = input("Would you like to hear a random fact? (Press enter if yes).")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()            