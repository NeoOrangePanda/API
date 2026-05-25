import requests

def get_random_jokes():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Full JSON Response: {response.json()}")

        joke_data = response.json()
        return f"{joke_data['setup']} - {joke_data['punchline']}"
    
    else:
        return "Failed to retrieve joke\n"
    
def main():
    print("Welcome to the Random Joke Generator")

    while True:
        user_input = input("Press Enter to get a new joke, or type 'q' or 'exit' to quit: \n").strip().lower()
        if user_input in ('q', 'exit'):
            exit()
        else:
            joke = get_random_jokes()
            print(joke)

if __name__ == "__main__":
    main()