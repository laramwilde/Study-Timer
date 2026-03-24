#############################
# Study Tracker
# This is a command line program that will allow the user to:
# Have a study session timer
# Have a file that logs their hours studied
# log how effective a study session was

import time


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


def test_time_func():
    start = input("Start counting? Y/N")
    if start.lower() == "y":
        #marks time stamp for the stat
        start = time.time()
        print("Timer started")
    else:
        print("Timer not started.")
    stop = input("Stop counting? Y/N")
    if stop.lower() == "y":
        # marks time stamp for the end
        end = time.time()
        time_elapsed = end - start
        print(time_elapsed)

    # rounded_time = round(time_elapsed, 1)
    rounded_time = 180
    if rounded_time < 60:
        print("Studied for less than one minute.")
        study_time_minutes = 1
    elif rounded_time > 60:
        study_time_minutes = rounded_time / 60
    
    print(study_time_minutes)
    

test_time_func()
