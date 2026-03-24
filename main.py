#############################
# Study Tracker
# This is a command line program that will allow the user to:
# Have a study session timer
# Have a file that logs their hours studied
# log how effective a study session was

import time

subject_list = ["English", "Maths", "Music", "Business", "Science"]


def main_menu():

    print("############################")
    print("The Study Centre")
    print("############################")
    print("")
    print("What would you like to do today?")
    print("1. Timed Study Session")
    print("2. Track a Study Session")
    print("3. Check previous study sessions")
    print("4. Check what needs studying next")
    print("5. View/Edit Subject List")
    print("6. Help/FAQ")

    while True:
        user_choice = input("Please select one of the following options above by entering a number between 1-6.")
        try:
            int(user_choice)
            user_choice = int(user_choice)
            if 1 <= user_choice <= 6:
                break
            int(user_choice)
        except ValueError:
            print("Invalid - please try again with an integer between 1-6.")

    if user_choice == 1:
        print("tbc")
    elif user_choice == 2:
        print("tbc")
    elif user_choice == 3:
        print("tbc")
    elif user_choice == 4:
        print("tbc")
    elif user_choice == 5:
        subject_editing(subject_list)
    elif user_choice == 6:
        print("tbc")

def subject_editing(subject_list):

    print("############################")
    print("SUBJECT LIST EDITING/VIEWING")
    print("############################")

    print("Please select an option:")
    print("1. View current subject list")
    print("2. Remove subjects from the subject list")
    print("3. Add subjects to the subject list")
    print("4. Quit subject editing")

    #data validation - ensures the user cannot proceed if the inputted option is not an integer or between 1-4
    while True:
        option = input("Input a number between 1-4 to proceed.")
        try:
            int(option)
            if 1 <= int(option) <= 4:
                break
            else:
                print("Please enter a number between 1-4.")
        except ValueError:
            print("You did not enter a value that is an integer, please try again with a number from 1-4.")

    #converts option into an integer
    option = int(option)

    if option == 1:
        print("##################################")
        print("View current subject list selected")
        print("##################################")
        print("The current subject list is:")
            
        for subject in subject_list:
            print(subject)

        # DATA VALIDATION TO CHECK IF ITS Y OR N
        while True:
            back_to_menu = input("Would you like to go back to the subject editing menu? Y/N")
            if back_to_menu.lower() == "y":
                subject_editing(subject_list)
            elif back_to_menu.lower() == "n":
                return None
            else:
                print("Please enter Y or N.")

    #REMOVE SUBJECTS FROM LIST 
    elif option == 2:
        print("tbc")

    #ADD SUBJECTS TO THE LIST
    elif option == 3:
        print("###########################################")
        print("Add a subject to the subjects list selected")
        print("###########################################")

    while True:
        users_added_subject = input("Enter the subject you would like to add to the list.")
        if not users_added_subject:
            print("The input is empty, please try again.")
        else:
            confirmation = input(f"Please confirm if you would like to add the subject {users_added_subject}. Y/N")
            if confirmation.lower() == "y":
                subject_list.append(users_added_subject)
                print(f"Your subject ({users_added_subject}) has been added to the list.")
                print("\nThe updated list:")
                for subject in subject_list:
                    print(subject)
                break
            elif confirmation.lower() == "n":
                print("Subject not added.")
                return None
            else:
                "You did not enter Y or N to confirm, please try again."

    #QUIT
   # elif option == 4:
       # return None


def get_study_time():
    print("Time a study session selected.")
    # make it so its a list of subjets and they choose one
    print("What is this study session for?")
    # add input cvalidation to ensure the inputs not an empty string
    subject_studied = input("Please input your subject you're studing for:")
    print("\n Input accepted.")
    begin = input("Would you like to begin? Y/N")
    if begin.lower() == "y":
        start = time.time()
    else:
        #fix this so it returns that the user quits
        return None
    finished_studying = input("Enter 'Y' when you are finished studying and wish to end the timer.")
    # make it so the user has to enter "y" for the program to end
    if finished_studying.lower() == "y":
        end = time.time()
        # gets the time elapsed in seconds
    elapsed_time = end - start
    converted_time = convert_time(elapsed_time)

    if converted_time == False:
        print("Time elapsed was less than one minute, this will not be logged.")
    else:
        print(f"You spent {int(converted_time)} studying {subject_studied}. Well done!")
        print("This will be logged.")

def convert_time(elapsed_time):
    elapsed_time = round(elapsed_time, 1)
    #checks if the elapsed time is atleast one minute
    if elapsed_time < 60:
        more_than_one_min = False
    elif elapsed_time >= 60:
        more_than_one_min = True

    #returns if its more than one minute
    if more_than_one_min == False:
        return False
    elif more_than_one_min == True:
        time_into_mins = elapsed_time / 60
        return time_into_mins

        
#get_study_time()

main_menu()



