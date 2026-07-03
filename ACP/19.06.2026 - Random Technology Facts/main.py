import requests

url = "https://github.com/AsbDaryaee/facts-api.git/facts-api/api/facts/random"

def get_random_technology_fact():
    response = requests.get(url)
    if response.status_code == 200:
        fact_data = response.json()
        print(fact_data)
    else:
        print(f"Failed to fetch fact {response.status_code}")

while True:
    user_input = input("Press Enter to get random technology fact or type 'q' to quit....")
    if user_input.lower() == 'q':
        break
    get_random_technology_fact()