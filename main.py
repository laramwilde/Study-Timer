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
    print("5. Help/FAQ")
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
        print(f"You spent {converted_time} studying {subject_studied}. Well done!")
        print("This will be logged.")

def convert_time(elapsed_time):
    elapsed_time = round(elapsed_time, 1)
    print(f"TEST TEST TEST {elapsed_time}")
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
        print(f"TESTTESTTEST 2 {time_into_mins}")

        return time_into_mins

        
get_study_time()