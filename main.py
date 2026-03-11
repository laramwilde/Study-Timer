#############################
# Study Tracker
# This is a command line program that will allow the user to:
# Have a study session timer
# Have a file that logs their hours studied

def main_menu():
    print("############################")
    print("The Study Centre")
    print("############################")
    print("")
    print("What would you like to do today?")
    print("1. Timed Study Session")
    print("2. Track a Study Session")
    print("3. Check previous study sessions")
    printed_once = False
    while True:
        try:
            if printed_once == False:
                user_choice = input("Please select one of the following options above.")
                printed_once = True
            elif printed_once == True:
                user_choice = input("Choose an option between 1-3:")
            int(user_choice)
        except ValueError:
            print("Invalid.")
        else:
            return user_choice
        # make it so it checks if number is between 1-3 etc

main_menu()