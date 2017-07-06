from My_Support import *

print "*******Welcome Spy*******\n"
spy_profile('Pooja', 'Miss.', 20, 4.2)
friend_profile('Pooja', 'Aashi', 'Miss', 23, 4.9)
friend_profile('Pooja','Aanya','Miss',22,4.5)
var = 0
while var == 0:
    start = raw_input("Do you want to continue as Pooja.(Y/N)\n")
    if start == 'Y' or start == 'y':
        print "Welcome Back Miss. Pooja"
        spy_name = 'Pooja'
        spy_sal = data['Sal']
        spy_age = data['Age']
        spy_rating = data['Rating']
    elif start == 'N' or start == 'n':
        spy_name = raw_input("Please Enter Your Name\n");
        if len(spy_name) > 0:

            spy_sal = raw_input("You are (Mr. or Miss.)\n")

            spy_age = int(raw_input("What\'s your age %s %s\n" % (spy_sal, spy_name)))
            if 12 <= spy_age < 50:
                spy_rating = float(raw_input("Please provide your current ratings(0 to 5)\n"))
                if 2.0 > spy_rating:
                    print "Please Try Harder, rating is just a number\n"

                elif 2.0 <= spy_rating < 4.0:
                    print "Nice Ratings, Keep Going\n"

                elif 4.0 <= spy_rating < 5.0:
                    print "Wow.. You are about to reach 007 grade\n"

                elif spy_rating == 5.0:
                    print "Welcome %s %s 007\n" % (spy_sal, spy_name)

                else:
                    print "Invalid Ratings\n"
                    exit()
                spy_profile(spy_name, spy_sal, spy_age, spy_rating)
            else:
                print "You are not of correct age yet."

    print "User Authorized: Welcome %s %s\n" % (spy_sal, spy_name)
    index = 0
    while index == 0:
        menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret " \
                       "message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application " \
                       "\n "
        menu_choice = int(raw_input(menu_choices))
        if menu_choice == 2:
            spy_social(spy_name)
            print "Now you have %d friends" % len(friend_list.keys())
        elif menu_choice == 1:
            status()
        elif menu_choice == 3:
            send_message()
        elif menu_choice == 4:
            read_message()
        elif menu_choice == 5:
            read_chat_history()
        else:
            exit()

    else:
        print "Enter Correct Name\n"
else:
    print "Wrong Choice"
