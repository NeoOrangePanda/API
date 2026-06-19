from colorama import Fore, init
import requests
import random
import html

init(autoreset=True)

print(f"{Fore.GREEN} 1. General Knowledge" / 
      f"{Fore.GREEN} 2. Computers" /
      f"{Fore.GREEN} 3. Mathematics" /
      f"{Fore.GREEN} 4. History" /
      f"{Fore.GREEN} 5. Vehicles" /
      f"{Fore.GREEN} 6. Animals" )

def set_education_category():
    category_input = int(input("Select any of these categories (1-6): "))
    if 1 <= category_input <= 6:
        print("okay")

set_education_category()