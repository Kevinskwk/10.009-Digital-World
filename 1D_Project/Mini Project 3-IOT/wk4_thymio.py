from pythymiodw import *
from time import sleep
from libdw import pyrebase


projectid = "replace me"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "replace me"
email = "replace me"
password = "replace me"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
user = auth.sign_in_with_email_and_password(email, password)

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto 
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
db = firebase.database()

robot = ThymioReal()  # create a robot object

no_movements = True

while no_movements:
    # Check the value of movement_list in the database at an interval of 0.5
    # seconds. Continue checking as long as the movement_list is not in the
    # database (ie. it is None). If movement_list is a valid list, the program
    # exits the while loop and controls the robot to perform the movements
    # specified in the movement_list in sequential order. Each movement in the
    # list lasts exactly 1 second.

    # Write your code here
    command_list = db.child("command_list").get(user['idToken'])
    if command_list == None:
        sleep(0.5)
    else:
        no_movements = False
        execute(robot, command_list)
        no_movements = True
        db.child("command_list").set(None, user['idToken'])


# Write the code to control the robot here
def execute(bot, command):
    for i in command:
        if i == "w":
            bot.wheels(100, 100)
        elif i == "a":
            bot.wheels(-100, 100)
        elif i == "d":
            bot.wheels(100, -100)
        else:
            print("Unrecognised command")
        bot.sleep(1)
    
    bot.wheels(0, 0)

# 'up' movement => robot.wheels(100, 100)
# 'left' movement => robot.wheels(-100, 100)
# 'right' movement => robot.wheels(100, -100)

