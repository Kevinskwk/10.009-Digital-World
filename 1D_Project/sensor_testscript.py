from libdw import pyrebase
import random

projectid = "dw1dproject"
dburl = "https://" + projectid + ".firebaseio.com"
authdomain = projectid + ".firebaseapp.com"
apikey = "AIzaSyCMv0kFFwAnStTfLbI94PVdppuPZAhmS_Q"  # unique token used for authentication
email = "angsonggee@yahoo.com.sg"
password = "password"

config = {
    "apiKey": apikey,
    "authDomain": authdomain,
    "databaseURL": dburl,
}

# Create a firebase object by specifying the URL of the database and its secret token.
# The firebase object has functions put and get, that allows user to put data onto
# the database and also retrieve data from the database.
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(email, password)


# CODE ABOVE IS FOR FIREBASE

# CODE BELOW WILL GENERATE RANDOM VALUES AND FILL UP THE FIREBASE LIST

myBins = {}
binNames = []
# Create dictionary of bins and list of binNames to access the Dict
for i in range(1, 6):
    name = 'Bin' + str(i)
    binNames.append(name)
    myBins[name] = {'Smell': random.randint(0, 1), 'Ultrasonic': random.randint(0, 1), 'Water': random.randint(0, 1)}

# print(myBins)
# print(binNames)
# root = db.child('current_bin_states').child('Bin1').get(user['idToken'])
# print(root.key(), root.val())

for i in binNames:
    for log_no in range(3):
        log_string = f"{random.randint(1, 7)} {random.randint(0, 23)} {random.randint(0, 59)} {random.randint(0, 1)}"
        db.child('log').child(i).push(log_string)


db.child('current_bin_states').update(myBins)
root = db.child('current_bin_states').get(user['idToken'])

print(root.key(), root.val())