#Take username and password from user and check it again for the three times whether the user has entered the right
#username and password. If yes then print a message "Logged in Successfully", if not then print invalid credentials
#for consecutive 3 times and if the limit exceeds than print "Attempt finished".

<<<<<<< HEAD
=======

>>>>>>> bd0fdb2a62bb528439e1cc0636b4a95564be97ef
username=input("Enter Your Username: ")
password=input("Enter your Password: ")
for i in range(0,3):
    print("Enter Your Credentials")
    username1=input("Enter Your Username: ")
    password1=input("Enter your Password: ")
    if (username==username1) and (password==password1):
        print("You are successfully Logged.")
        break
<<<<<<< HEAD
    elif i<3:
        if (username!=username1) and (password!=password1) and i<3:
            print("Invalid Credentials")
else:
    print("3 Attempt Finished")
    
=======
    else:
        if(username!=username1 and password==password1):
            print("Invalid Credentials")
else:
    print("3 Attempt Finished")
>>>>>>> bd0fdb2a62bb528439e1cc0636b4a95564be97ef
