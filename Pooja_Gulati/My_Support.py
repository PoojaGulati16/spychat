import time
from datetime import datetime

from steganography.steganography import Steganography

spy_list = {}
friend_list = {}
data = {'Name': '', 'Sal': '', 'Age': 0, 'Rating': 0.0}
status_list = ['Single', 'Taken', 'In Field', 'Technical Assistance Required']
my_status = {'Msg': '', 'Status': 0}
chat_list = {}
temp_friend_list = []


def spy_profile(name, sal, age, rating):
    data = {'Name': name, 'Sal': sal, 'Age': age, 'Rating': rating}

    spy_list.update({data['Name']: data})


def friend_profile(spy, name, sal, age, rating):
    data = {'Spy': spy, 'Name': name, 'Sal': sal, 'Age': age, 'Rating': rating}

    friend_list.update({data['Name']: data})


def spy_social(spy):
    F_name = raw_input("Please add your friend's name:\n ")
    F_salutation = raw_input("Are they Mr. or Miss.?: \n")

    # F_name = F_salutation + " " + F_name

    F_age = int(raw_input("Age?\n"))

    F_rating = float(raw_input("Spy rating?\n"))

    if len(F_name) > 0 and F_age > 12 and F_rating >= spy_list[spy]['Rating']:

        friend_profile(spy, F_name, F_salutation, F_age, F_rating)

        print 'Friend Added!'
        print friend_list
    else:

        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'


def status():
    if my_status['Status'] == 0:
        print "You don't have any status\n"
    else:
        print "Your current status is :%s\n" % my_status['Msg']
    ch = raw_input("Do you want to select from existing status messages(Y/N)\n")

    if ch == 'Y' or ch == 'y':
        item_position = 1

        for message in status_list:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("Choose from the above messages\n"))

        if len(status_list) >= message_selection:
            updated_status_message = status_list[message_selection - 1]
            my_status.update({'Msg': updated_status_message, 'Status': 1})
            # status_list.append(updated_status_message)
            print "Your New Status is--> %s" % updated_status_message;
        elif len(status_list) < message_selection:
            print "Invalid Choice\n"
    elif ch == 'N' or ch == 'n':
        msg = raw_input("Enter your Status Message:\n");
        my_status.update({'Msg': msg, 'Status': 1})
        status_list.append(msg)
        print "Your New Status is--> %s" % msg


def select_friend():
    item_number = 0

    for friend in friend_list.keys():
        print '%d. %s %s aged %d with rating %.2f is online' % (
            item_number + 1, friend_list[friend]['Sal'], friend_list[friend]['Name'],
            friend_list[friend]['Age'],
            friend_list[friend]['Rating'])

        item_number = item_number + 1
        temp_friend_list.append(friend_list[friend]['Name'])

    friend_choice = raw_input("Choose from your friends\n")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position


def chat(message, name):
    print "%s   %s" % (message, name)
    chat_list.update({name: {'Name': name, 'Message': message, 'Time': datetime.now().strftime("%d %B %Y")}})
    print chat_list


def send_message():
    friend_choice = select_friend()

    original_image = raw_input("Enter Name of image?\n")
    output_path = "encoded.jpg"
    text = raw_input("Enter Your Secret Message?\n")
    Steganography.encode(original_image, output_path, text)

    chat(text, temp_friend_list[friend_choice])
    # new_chat = ChatMessage(text, True)

    # friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"
    print chat_list


def read_message():
    sender = select_friend()

    output_path = raw_input("What is the name of the file?\n")

    secret_text = Steganography.decode(output_path)

    chat(secret_text, friend_list[temp_friend_list[sender]]['Spy'])

    # new_chat = ChatMessage(secret_text,False)

    # friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"


def read_chat_history():
    read_for = select_friend()

    print '\n'

    # for chat in chat_list[friend_list[temp_friend_list[read_for]]]:
    for chatC in chat_list.keys():
        if chatC == friend_list[temp_friend_list[read_for]]['Spy']:
            print "At %r     You Said:   %s" % (chat_list[chatC]['Time'], chat_list[chatC]['Message'])
        else:
            print "At %r     %s said:    %s" % (chat_list[chatC]['Time'], chatC, chat_list[chatC]['Message'])
