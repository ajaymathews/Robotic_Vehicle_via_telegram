#pin connections
'''
PIR : RPI
    vcc - 5v
    OUT-40 PIN
    gnd-gnd

DHT11 : RPI
    s-3 PIN
    + - 5v
    - - gnd
MOTOR_DRIVER : RPI
    IN1 : 31 PIN
    IN2 : 33 PIN
    IN3 : 35 PIN
    IN4 : 37 PIN
    
'''


#Importing modules for the rpi
import RPi.GPIO as GPIO
import os
import glob
import time
import telegram
from telegram.ext import Updater, CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import numpy as np
import dht11
import cv2
import serial
from threading import Thread

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

#setting BOARD mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#setting Pin as variables
trigger_pin = 16
echo_pin = 18

#setting pin as I/O
GPIO.setup(trigger_pin,0)
GPIO.setup(echo_pin,1)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)
GPIO.setup(40,GPIO.IN)


t1 = dht11.DHT11(pin=3)

#definition of start command 
def start(bot, update):
    global user_tele_id
    print (update.message.chat_id)
    user_tele_id=str(update.message.chat_id)
    update.message.reply_text('Welcome')                                                                                                          
    custom_keyboard = [['/Capture_Picture','/status'],['/front','/Back'],['/Left','/Right'],['/stop','/check']]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.sendMessage(update.message.chat_id,text="Loading.....",reply_markup=reply_markup)

#Camera_section
def Capture_Picture(bot, update):
    if(user_tele_id==str(update.message.chat_id)):
        try:
            update.message.reply_text('Capturing.....')
            os.remove('/home/pi/Desktop/PROJECT/MILITARY_ROBOT/image.jpg')
            os.system("sudo fswebcam -r 320x240 /home/pi/Desktop/PROJECT/MILITARY_ROBOT/image.jpg")
            f = open('image.jpg','rb')
            update.message.reply_text('Sending.....')
            bot.sendPhoto(update.message.chat_id,(f))
        except:
            update.message.reply_text('Error While Capturing...')
    else:
        update.message.reply_text('Permission Denied')
     
def Capture_Video(bot, update):
    try:
        update.message.reply_text('Recording.....')
        os.remove('/home/pi/Desktop/MIL_BOT/ak.mp4')
        os.system("sudo avconv -t 10 -f video4linux2 -r 5 -s 320x240 -i /dev/video0 /home/pi/Desktop/MIL_BOT/ak.mp4")
        update.message.reply_text('Sending.....')
        bot.send_video(update.message.chat_id, video=open('ak.mp4','rb'))
    except:
        update.message.reply_text('Error While Capturing...')

#dht11-Temperature/Humidity measurement section
def dht1():
    t1_Result = t1.read()
    if t1_Result.is_valid():
        temp1 = str(t1_Result.temperature)
        humidity = str(t1_Result.humidity)
        return temp1,humidity
    
#HCSR04-Distance measurement section
def send_trigger_pulse():
    GPIO.output(trigger_pin, True)
    time.sleep(0.0001)
    GPIO.output(trigger_pin, False)
def wait_for_echo(value, timeout):
    count = timeout
    while GPIO.input(echo_pin) != value and count > 0:
        count = count - 1
def get_distance():
    send_trigger_pulse()
    wait_for_echo(True, 10000)
    start = time.time()
    wait_for_echo(False, 10000)
    finish = time.time()
    pulse_len = finish - start
    distance_cm = (pulse_len *34300)/2
    print(distance_cm)
    return (distance_cm)

def pir_sense():
    time.sleep(.5)
    while(i<10):
        if(GPIO.input(40)==True):
            msg=('Human presence detected')
            print(msg)
        else:
            msg=('inside function no presence')
            print(msg)
        

#status function to call distance, temperature & humidity     
def status(bot, update):
    dh=dht1()
##    hu=pir()
    tem,humd=dh
    print("temperature:"+tem)
    print("humidity:"+humd)
##    dist=get_distance()
##    distance=dist
##    print("Distance:"+distance)
##    hu=pir()
##    hum=str(hu)
##    print(hu)
##    msg=str('Temperature:'+tem+'*C \n Humidity:'+humd) ##   +'DistanceToImpact:'+dist+'\n'+hum
##    print(msg)
    if dh is None:
        update.message.reply_text('none')
    else:
        update.message.reply_text(str('Temperature:'+tem+'*C \n Humidity:'+humd))

def check(bot,update):
    print('clicked pir')
    if(GPIO.input(40)==True):
        msg=('Human presence detected')
        print(msg)
    else:
        msg=('No Human presence')
        print(msg)
        
        
    update.message.reply_text(str(msg))


    

def front(bot, update):
    GPIO.output(31,True)
    GPIO.output(33,False)
##    GPIO.output(35,True)
##    GPIO.output(37,False)#front
    update.message.reply_text('Moving forward')

def back(bot, update):
    GPIO.output(33,True)
    GPIO.output(31,False)
    GPIO.output(37,True)
    GPIO.output(35,False)#back
    update.message.reply_text('Moving Backward')

def right(bot, update):
    GPIO.output(31,False)
    GPIO.output(33,True)
    GPIO.output(35,True)
    GPIO.output(37,False)#right
    time.sleep(0.1)
    update.message.reply_text('Turning Right')

def left(bot, update):
    GPIO.output(31,True)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,True)#LEFT
    time.sleep(0.1)
    update.message.reply_text('Turning Left')

def stop(bot, update):
    GPIO.output(31,False)
    GPIO.output(33,False)
    GPIO.output(35,False)
    GPIO.output(37,False)#stop
    time.sleep(0.1)
    print('Turning Engine OFF')
    update.message.reply_text('Turning Engine OFF') 
   

bot = telegram.Bot(token='627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM') #'627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM'
updater = Updater('627333566:AAGanhIPY2BP7UqOJcdAhjYR1mOJZG6OuyM')
##bot = telegram.Bot(token='620780485:AAGVZnDEHbC3lxsy5oxTezaECejDM3M43-0')
##updater = Updater('620780485:AAGVZnDEHbC3lxsy5oxTezaECejDM3M43-0')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('Capture_Video', Capture_Video))
updater.dispatcher.add_handler(CommandHandler('Capture_Picture', Capture_Picture))
updater.dispatcher.add_handler(CommandHandler('front', front))
updater.dispatcher.add_handler(CommandHandler('back', back))
updater.dispatcher.add_handler(CommandHandler('right', right))
updater.dispatcher.add_handler(CommandHandler('left', left))
updater.dispatcher.add_handler(CommandHandler('stop', stop))
updater.dispatcher.add_handler(CommandHandler('status', status))
updater.dispatcher.add_handler(CommandHandler('check', check))
#updater.dispatcher.add_handler(CommandHandler('fire_check', fire_check))

print("System Start")
try:    
   updater.start_polling()
   updater.idle()
  
except:
   print("Error: unable to start thread")

while 1:
   pass

    
