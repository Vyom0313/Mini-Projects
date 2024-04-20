# timer

from playsound import playsound
import time

#ANSI (charachters or escape sequences)
#used to manipulate the terminal

CLEAR = "\033[2J" #clears terminal
CLEAR_AND_RETURN = "\033[H" #return the cursor to home position thereby printing over what was there before

def alarm(seconds):
    time_elapsed = 0

    print(CLEAR)
    while time_elapsed < seconds:
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60 #this // is for integer divide i.e. 125 // 60 = 2 i.e. no fractions
        seconds_left = time_left % 60 #remaining seconds i.e. 125 % 60 = 5

        # print(f"{minutes_left}:{seconds_left}") 
        # # we dont use the above statement because of unconventional formatting
        print(f"{CLEAR_AND_RETURN}Alarm will sound in: {minutes_left:02d}:{seconds_left:02d}") #that is.. make it two digits and pad with 0    
        # # now if we use just this while loop, it will print everything in different lines.. we need to make it look like it's updating in a single line
        # we don that using the CLEAR_AND_RETURN variable
    playsound("C:/Users/Vyom/Desktop/MIni Python Projects/Alarm Clock/alarm.mp3")

minutes = int(input("How many minutes to wait till alarm goes off: ")) #assuming the user gives valid input, if they don't it will crash the program
seconds = int(input("How many seconds to wait till alarm goes off: "))
total_seconds = minutes * 60 + seconds
alarm(total_seconds) #alarm with seconds