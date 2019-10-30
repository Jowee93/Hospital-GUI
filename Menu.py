import re
import time

from colorama import Fore, Style
from Database import *

all_patient = {}
count = 0

def print_menu() :   
    print("") 
    print("Welcome to your hospital page !")
    print("")
    print(Fore.RED + "P1 : Admit a new patient")
    print("P2 : Discharge a patient")
    print("P3 : Check all patient records")
    print(Style.RESET_ALL)
    
    print(Fore.GREEN + "D1 : Add a new staff")
    print("D2 : Remove a staff")
    print("D3 : Check all staff records")
    print(Style.RESET_ALL)
    
    print(Fore.YELLOW + "LO : Log Out")
    print(Style.RESET_ALL)
    
def P1() :
    global count
    count += 1
    
    name = input("Enter patient's name : ").upper()
    age = input("Enter patient's age : ").upper()
    state = input("Enter patient's state : ").upper()
    status = input("Enter patient's status : ").upper()
    
    added_patient = {patient(count, name, age, state, status)}
    
    for each in added_patient :
        all_patient.setdefault(each.num, {"name" : name, "age" : age, "state" : state, "status" : status})
        
    print(f"You have added the following patient details : \n Name : {all_patient[count]['name']} \n Age : {all_patient[count]['age']} \n State : {all_patient[count]['state']} \n Status : {all_patient[count]['status']} ")
    
    # all_patient[count] = {"name" : name}, {"age" : age}, {"state" : state}, {"status" : status}
    
    # print(f"You have added the following patient details : \n Name : {all_patient[count][0]['name']} \n Age : {all_patient[count][1]['age']} \n State : {all_patient[count][2]['state']} \n Status : {all_patient[count][3]['status']} ")

def P2() :
    validation = False
    
    print(all_patient)
    
    reg = re.compile(r"\D*")
    
    while validation == False :
        try:
            discharge = int(input("Please enter patient's number to be removed : "))

            if discharge == 000 :
                print("EXITING...")
                time.sleep(0.5)

                validation = True
                break
                
        except:
            print("Please enter an integer !")
            continue
            
        else :
            try:
                print(f"Patient removed as follows: {all_patient.pop(discharge)}")
                
            except:
                print("Hmmm, you might have entered a patient's number that don't exist, please try again")
                print("You may enter '000' to exit")
            
            else:
                validation = True
    
    
    
    
