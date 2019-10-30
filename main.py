####################
# Import libraries #
####################

from tkinter import Button, Label, Tk

from colorama import Back, Fore, Style

from Welcomepage import *
from Login import accounts, login
from Menu import *

################
# Login Page   #
################

login_status = True

print_welcome_page()

while not login() :
    print("Access Denied !")
    print_welcome_page()
    
    
#############
# Menu Page #
#############

while login_status == True:
    print_menu()
    navigation = input("What would you like to do today? : ").upper()
    
    if navigation == "P1" :
        P1()
        
    elif navigation == "P2" :
        P2()
    
    elif navigation == "P3" :
        if all_patient == {} :
            print("There is no patient in your hospital !")
        else :
            print(all_patient)

    elif navigation == "LO" :
        login_status = False
        print("You have successfully logged out ! Sayonara !")
        
