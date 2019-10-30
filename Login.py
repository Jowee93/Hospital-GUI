import getpass

accounts = {
    'account1' : {
        "name": "CEO",
        "password" : "CEO123",
        "occupation" : "Chief Executive Officer",
        "grade" : 10
    },
    
    'account2' : {
        "name": "Manager",
        "password" : "Manager123",
        "occupation" : "Manager",
        "grade" : 6
    },
    
    'account3' : {
        "name": "Bangla",
        "password" : "Bangla123",
        "occupation" : "Bangla",
        "grade" : 0
    } 
}

def login () :
    username = input("Enter your username : ")
    password = getpass.getpass(prompt = "Enter your password : ")
    details = [username, password]
    
    for account in accounts :
        account_details = [accounts[account]["name"], accounts[account]["password"]]
        
        if account_details == details :
            return [True, username]
        else:
            continue
        
    return False


        
        
    
            

    



