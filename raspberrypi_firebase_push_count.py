import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import RPi.GPIO as GPIO
import time
GPIO_SW = 7
GPIO_LED = 8

count_value =0

def my_callback(channel):
    time.sleep(0.05)
    global  count_value
    if(GPIO.input(channel)==GPIO.LOW):
        updates = {
            'counter':count_value
        }
        users_ref.update(updates)
        GPIO.output(GPIO_LED,GPIO.HIGH
        print('button pushed '+ str(channel) +"  Count:" + str(count_value))
        count_value +=1
    else:
        GPIO.output(GPIO_LED,GPIO.LOW)
        print(users_ref.get().get("counter"))

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_SW, GPIO.IN, pull_up_down =GPIO.PUD_UP)
GPIO.setup(GPIO_LED, GPIO.OUT)
GPIO.output(GPIO_LED, GPIO.LOW)

GPIO.add_event_detect(GPIO_SW, GPIO.BOTH,
    callback=my_callback, bouncetime =50)

cred = credentials.Certificate("service-account-file.json")

firebase_admin.initialize_app(cred,{
    'databaseURL': "https://m5data-XXXXXX.firebaseio.com"
})

users_ref = db.reference('/M5Stack')

try:
    while(True):
        time.sleep(1)

except KeyboardInterrupt:
    print("break")
    GPIO.cleanup()
    GPIO.remove_event_detect(GPIO_SW)
                    
#参考にしたサイト:https://qiita.com/sai-san/items/24dbee74c5744033c330
