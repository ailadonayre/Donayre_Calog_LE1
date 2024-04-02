#Calog_Donayre_LE1_
game_library = {
    "Donkey Kong": {"Quantity": 3, "Cost": 2},
    "Super Mario Bros": {"Quantity": 5, "Cost": 3},
    "Tetris": {"Quantity": 2, "Cost": 1}
}

user_inventory = {
    "Donkey Kong": 0,
    "Super Mario Bros": 0,
    "Tetris": 0
}

users = {}
username = ""
adm_user = "admin"
adm_pass = "adminpass"
user_coins = 0
user_points = 0

def sign_up(username, user_coins, user_points):
    print("_" * 100)
    print("\nCreate an account")

    while True:
        try:
            username = str(input("\nEnter your username: "))
            if username in users:
                print("\nUsername already exists. Please enter a different username.")
                continue
            while True:
                password = str(input("Enter your password (at least 8 characters): "))
                if len(password) >= 8:
                    users[username] = {"password": password, "user_coins": 0, "user_points": 0}
                    print(users)
                    print("\nYou have successfully signed up to CD Game Rentals!")
                    main_menu(username, user_coins, user_points)
                else:
                    print("\nYour password must have at least 8 characters. Please try again.")
                    sign_up(username, user_coins, user_points)
        except ValueError:
            print("\n[ValueError] Invalid input. Please try again.")
        except KeyError:
            print("\n[KeyError] Invalid input. Please try again.")

def sign_in(username, user_coins, user_points):
    print("_" * 100)
    print("\nSign in to your account")
    
    while True:
        try:
            username = str(input("\nEnter your username: "))
            password = str(input("Enter your password: "))

            if username not in users:
                print("\nUser does not exist. Please enter your proper log-in credentials.")
                sign_in(username, user_coins, user_points)
                break
            if users[username]['password'] == password:
                users[username].update(user_inventory)
                print("\nYou have successfully signed in.")
                signed_menu(username, user_coins, user_points)
                break
            else:
                print("Your log-in credentials are incorrect. Please try again.")
                sign_in(username, user_coins, user_points)
                break            
        except ValueError:
            print("\n[ValueError] Invalid input. Please try again.")
        except KeyError:
            print("\n[KeyError] Invalid input. Please try again.")

def display_games(username, user_coins, user_points):
    print("_" * 100)
    print("\nDisplay Games")

    i = 1
    for games in game_library:
        print(f"{i}. {games}")
        i += 1
        for details in game_library[games]:
            print(f"{details}: {game_library[games][details]}")

    try:
        choice = str(input("\nWould you like to go back to the main menu? (Y/N) "))
        if choice == 'Y' or choice == 'y':
            main_menu(username, user_coins, user_points)
        elif choice == 'N' or choice == 'n':
            display_games(username, user_coins, user_points)
        else:
            print("\nInvalid input. Please try again.")
    except ValueError:
            print("\n[ValueError] Invalid input. Please try again.") 

def sign_admin(username, user_coins, user_points):
    print("_" * 100)
    print("\nSign in to your account")
    
    while True:
        try:
            admin_username = str(input("\nEnter your username: "))
            admin_password = str(input("Enter your password: "))

            if admin_username == adm_user and admin_password == adm_pass:
                print("\nYou have successfully signed in as administrator.")
                signed_admin(username, user_coins, user_points)
                break
            else:
                print("Your log-in credentials are incorrect. Please try again.")
                sign_admin(username, user_coins, user_points)
                break            
        except ValueError:
            print("\n[ValueError] Invalid input. Please try again.")
        except KeyError:
            print("\n[KeyError] Invalid input. Please try again.")

def rent_game(username, user_coins, user_points):
    print("_" * 100)
    print("\nRent a Game")

    while True:
        i = 1
        for games in game_library:
            print(f"{i}. {games}")
            i += 1
            for details in game_library[games]:
                print(f"{details}: {game_library[games][details]}")
        
        try:
            pass
        except ValueError:
            print("\n[ValueError] Invalid input. Please try again.")
        except KeyError:
            print("\n[KeyError] Invalid input. Please try again.")

def return_game(username, user_coins, user_points):
    print("_" * 100)
    print("\nReturn a Game")

def topup_account(username, user_coins, user_points):
    topup_user_coins = 0

    print("_" * 100)
    print("\nTop-up Account")

    while True:
        try:
            topup_user_coins = int(input("\nEnter the amount of coins that you would like to add to your account: "))
            users[username]['user_coins'] += topup_user_coins
            print(f"\nYou have successfully topped up {topup_user_coins} coin/s. You now have {users[username['user_coins']]} coin/s.")
        except ValueError:
            print("\n[ValueError] Invalid input. Please try again.")

def display_inventory(username, user_coins, user_points):
    print("_" * 100)
    print("\nDisplay Inventory")

def redeem_game(username, user_coins, user_points):
    print("_" * 100)
    print("\nRedeem Free Game")

def check_points(username, user_coins, user_points):
    print("_" * 100)
    print("\nCheck Points")

    print(f"\nYou have {users[username]['user_points']} point/s.")

    try:
        choice = str(input("\nWould you like to go back to the user menu? (Y/N) "))
        if choice == 'Y' or choice == 'y':
            signed_menu(username, user_coins, user_points)
        elif choice == 'N' or choice == 'n':
            check_points(username, user_coins, user_points)
        else:
            print("\nInvalid input. Please try again.")
    except ValueError:
            print("\n[ValueError] Invalid input. Please try again.") 

def increase_qty(username, user_coins, user_points):
    print("_" * 100)
    print("\nIncrease Quantity")

def change_price(username, user_coins, user_points):
    print("_" * 100)
    print("\nChange Price")

def addrem_game(username, user_coins, user_points):
    print("_" * 100)
    print("\nAdd or Remove Game")

def signed_admin(username, user_coins, user_points):
    print("_" * 100)
    print(f"\nLogged in as {adm_user}.")
    print("\n1. Increase Quantity")
    print("2. Change Price")
    print("3. Add or Remove Game")
    print("4. Log Out")

    choice = int(input("\nKindly enter the numerical input of your choice: "))

    if choice == 1:
        increase_qty(username, user_coins, user_points)
        return
    if choice == 2:
        change_price(username, user_coins, user_points)
        return
    if choice == 3:
        addrem_game(username, user_coins, user_points)
        return
    if choice == 4:
        main_menu(username, user_coins, user_points)
        return

def signed_menu(username, user_coins, user_points):
    print("_" * 100)
    print(f"\nLogged in as {username}.")
    print(f"\nCoins: {user_coins}")
    print(f"Points: {user_points}")
    print("\n1. Rent Game")
    print("2. Return Game")
    print("3. Top-up Account")
    print("4. Display Inventory")
    print("5. Redeem Free Game")
    print("6. Check Points")
    print("7. Log Out")

    choice = int(input("\nKindly enter the numerical input of your choice: "))

    if choice == 1:
        rent_game(username, user_coins, user_points)
        return
    if choice == 2:
        return_game(username, user_coins, user_points)
        return
    if choice == 3:
        topup_account(username, user_coins, user_points)
        return
    if choice == 4:
        display_inventory(username, user_coins, user_points)
        return
    if choice == 5:
        redeem_game(username, user_coins, user_points)
        return
    if choice == 6:
        check_points(username, user_coins, user_points)
        return
    if choice == 7:
        user_coins = 0
        user_points = 0
        main_menu(username, user_coins, user_points)
        return

def main_menu(username, user_coins, user_points):
    print("_" * 100)
    print("\nWelcome to CD Game Rentals!")
    print("\n1. Display Available Games")
    print("2. Sign Up")
    print("3. Sign in")
    print("4. Sign in as Administrator")
    print("5. Exit")
    
    choice = int(input("\nKindly enter the numerical input of your choice: "))

    if choice == 1:
        display_games(username, user_coins, user_points)
        return
    if choice == 2:
        sign_up(username, user_coins, user_points)
        return
    if choice == 3:
        sign_in(username, user_coins, user_points)
        return
    if choice == 4:
        sign_admin(username, user_coins, user_points)
        return
    if choice == 5:
        exit()

main_menu(username, user_coins, user_points)
    