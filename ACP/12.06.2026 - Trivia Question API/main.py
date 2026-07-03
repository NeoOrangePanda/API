from colorama import Fore, init
import requests, html
import random
import time
import os, sys

init(autoreset=True)

print(f"{Fore.GREEN}1. General Knowledge")
print(f"{Fore.GREEN}2. Computers")
print(f"{Fore.GREEN}3. Mathematics")
print(f"{Fore.GREEN}4. History")
print(f"{Fore.GREEN}5. Vehicles")
print(f"{Fore.GREEN}6. Animals")

def set_education_category():
    categories = dict([(1, 9), (2, 18), (3, 19), (4, 23), (5, 28), (6, 27)])
    category_input = int(input("Select any of these categories (1-6): "))
    selected_category = categories.get(category_input)

    if selected_category is None:
        print(f"{Fore.RED}Invalid Input! Please wait 3 seconds and try again.")
        time.sleep(3)
        os.system("cls" if os.name == "nt" else "clear")
        set_education_category()

    return selected_category
    
def fetch_questions(category: int):
    API = f"https://opentdb.com/api.php?amount=10&category={category}&type=multiple"
    response = requests.get(API)

    if response.status_code == 200:
        data = response.json()
        if data['response_code'] == 0 and data['results']:
            return data['results']
        else:
            print(f"{Fore.RED}Error while loading!")
            sys.exit()
        