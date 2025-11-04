
    
            

hasUpper = hasLower = hasDigit = hasSpChar = False
noSpace = True
string = input("Enter your password: ")

if len(string)< 8 :
    print("Invalid Password, must contain atleast 8 charecters !")
else:   
    for ch in string:
        if not ch.isalnum() and ch != " ":
            hasSpChar = True
        elif ch == " ":
            noSpace = False
        elif ch.isdigit():
            hasDigit = True
        elif ch.isupper():
            hasUpper = True
        elif ch.islower():
            hasLower = True
        if "password" in string.lower():
            print("Password must not contain the word Password !")
            exit()
    if hasDigit and hasLower and hasUpper and hasSpChar and noSpace:
        print("A valid strong password.")
    elif noSpace:
        print("weak Password, better if changed")
    else:
        print("Invalid Password, Dont use space charecter !")
            