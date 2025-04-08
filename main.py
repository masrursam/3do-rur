import os
from colorama import init, Fore, Style

init(autoreset=True)

def print_brand():
    print(Style.BRIGHT + Fore.LIGHTGREEN_EX + "\n=== FORESTARMY TOOLKIT ===")

def print_menu():
    print(Style.BRIGHT + Fore.CYAN + "\n========= MAIN MENU =========")
    print(Style.BRIGHT + Fore.GREEN + "1 - Account Setup")
    print(Style.BRIGHT + Fore.YELLOW + "2 - Token Setup")
    print(Style.BRIGHT + Fore.MAGENTA + "3 - Run Script")
    print(Style.BRIGHT + Fore.BLUE + "4 - Proxy Setup")
    print(Style.BRIGHT + Fore.RED + "=============================")

def account_setup():
    email = input(Style.BRIGHT + Fore.CYAN + "Enter Email: ")
    password = input(Style.BRIGHT + Fore.CYAN + "Enter Password: ")
    with open("data.txt", "w") as f:
        f.write(f"{email}|{password}")
    print(Style.BRIGHT + Fore.GREEN + "Credentials saved in email|password format.")

def token_setup():
    print(Style.BRIGHT + Fore.YELLOW + "Running setup.js...")
    os.system("node setup.js")

def run_script():
    print(Style.BRIGHT + Fore.MAGENTA + "Running main.js...")
    os.system("node main.js")

def proxy_setup():
    proxy = input(Style.BRIGHT + Fore.BLUE + "Enter Proxy: ")
    with open("proxy.txt", "w") as f:
        f.write(proxy)
    print(Style.BRIGHT + Fore.GREEN + "Proxy saved to proxy.txt")

# Start the loop
while True:
    print_brand()
    print_menu()
    choice = input(Style.BRIGHT + Fore.WHITE + "Enter your choice (1-4): ").strip()
    if choice == "1":
        account_setup()
    elif choice == "2":
        token_setup()
    elif choice == "3":
        run_script()
    elif choice == "4":
        proxy_setup()
    else:
        print(Style.BRIGHT + Fore.RED + "Invalid choice! Please enter 1, 2, 3, or 4.")
