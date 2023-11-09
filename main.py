import colorama
import time


colorama.init(autoreset=True)


def rest(seconds: float, printing: str):
    time.sleep(seconds)
    print(printing)


# Colors Variables
RED = colorama.Fore.RED
GREEN = colorama.Fore.GREEN
BLUE = colorama.Fore.BLUE
YELLOW = colorama.Fore.YELLOW
MAGENTA = colorama.Fore.MAGENTA

year = int(time.strftime("%Y"))
print("Welcome to poor to rich journey")
print(BLUE + "Before you play sign up to the game".center(30, "-"))

# Sign in
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
re_type = input("Confirm your password: ")

# checking password
while password != re_type:
    re_type = input("Password doesn't match: ")

# dict of information of user
basicInfo = {
    "name": name,
    "email": email,
    "pass": password
}

print(f"Welcome to the {YELLOW + "GAME!"}")

