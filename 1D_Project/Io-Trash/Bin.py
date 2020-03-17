import RPi.GPIO as GPIO
from libdw import pyrebase
from credential import *
import time

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()
user = auth.sign_in_with_email_and_password(email, password)

class Bin:
    def __init__(self, ID, us, water, smell):
        self.ID = str(ID)
        self.sensors = {'us': bool(us),
                      'water': bool(water),
                      'smell': bool(smell)}
        self.needClean = self.sensors['us'] or self.sensors['water'] or self.sensors['smell'] 
        self.cleaning = False

    def get_data(self):
        # get ultrasonic, water and smell sensor data
        pass

    def update(self, db, user):
        db.child('current_bin_states').child(self.ID).set(self.sensors, user['idToken'])

    def check_button(self):
        # check if the button is pressed, change the cleaning state accordingly
        pass

    def log(self, db, user, logType):
        t = time.localtime(time.time())
        log = '{} {} {} {}'.format(t.tm_wday, t.tm_hour, t.tm_min, logType)
        db.child('log').child(self.ID).push(log, user['idToken'])

bin = Bin(1, 0, 0, 0)

def loop():
    while True:
        bin.check_button()
        if not bin.cleaning:
            t = time.localtime(time.time())
            if t.tm_sec <= 1:
                bin.get_data()
                bin.update(db, user)
                


        