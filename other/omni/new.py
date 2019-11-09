from tkinter import *
from tkinter import ttk
import pyttsx3
import datetime
import speech_recognition as sr
from threading import *
from time import sleep
import webbrowser
import os
import random

#-----------------------------------------------------------
''' assisstant codes '''

# -------pyttsx3-------------- 
engine=pyttsx3.init("sapi5")

#***************************
''' rate property of voice '''
rate1=engine.getProperty("rate")
engine.setProperty("rate",170)

#********************************

''' voice of API '''
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

#***************************************
#-----------time date-------------
timedate=datetime.datetime.now()
hour=timedate.hour

#---------speech recognition-------------
r=sr.Recognizer()

#*************************





#----------------------------------------------------------
''' functions '''

#*************************************
''' wish me '''
def wish_me():
    if 0<hour<12:
        speak('Good Morning Omnish sir')
    elif 12<=hour<=17:
        speak('Good Afternoon Omnish sir')
    else:
        speak('Good Evening Omnish sir')
    speak('I am Veronica , virtual assisstant of this system, how may I help you')

#***************************************************
class L1(Thread):
    def f1(self):
        global notify_label

        notify_label.config(text='Listening....')
        sleep(0.5)

''' this function will take command from user '''
class Listen(Thread):
    def voice_command(self):
        global notify_label, query
        r=sr.Recognizer()

        with sr.Microphone() as source:
            sleep(1)
            print('listening...')
            l1=L1()
            l1.f1()
            r.pause_threshold=1
            r.energy_threshold=500
            r.adjust_for_ambient_noise(source,duration=0.5)
            audio=r.listen(source)
            # notify_label.config(text='Listen Completed')

        try:
            # print('recognizing')
            notify_label.config(text='Recognizing')
            query=r.recognize_google(audio,language="en-in")
            notify_label.config(text=f'you said "{query}"')
            
        except Exception:
            notify_label.config(text='say that again please')
            return 'None'

        else:
            voice_sample=query.lower()
            if 'open youtube' in voice_sample:
                webbrowser.open('youtube.com')

            elif 'open google' in voice_sample:
                webbrowser.open('google.com')

            elif 'open stackoverflow' in voice_sample:
                webbrowser.open('stackoverflow.com')

            elif 'play music' in voice_sample:
                song_no=random.randrange(0,111,1)
                path1='F:\\MP3 Songs\\KK'
                songs_list=os.listdir(path1)
                os.startfile(os.path.join(path1,songs_list[song_no]))

            else:
                speak("sorry, this function is out of my reach")


#*****************************************
''' it  will let your system to  speak '''
def speak(text):
    engine.say(text)
    engine.runAndWait()


''' button function '''
def call():
    wish_me()
    sleep(1)
    l=Listen()
    l.voice_command()

        



#-------------------------------------------------------------

root=Tk()
root.title('Persional Assisstant')
root.geometry("500x600+800+80")
root.resizable(0,0)

#-----------------------------------------------------------
''' frames '''

f1=Frame(root,background="#000000")
f1.pack(expand=True , fill= 'both')

f2=Frame(root,background="#000000")
f2.pack(expand=True, fill='both')

f3=Frame(root,background="#000000")
f3.pack(expand=True, fill='both')

f4=Frame(root,background="#000000")
f4.pack(expand=True,fill='both')



#---------------------------------------------------------------------------------------------------------

''' labels '''

title_label=Label(f1,text='Veronica',font=("Consolas",20,"italic"), fg="blue",bg="#000000")
title_label.pack(pady=(20,0))

note_label=Label(
    f1,
    text="Click on 'Help' button and after listen... will appear then read out following phrases to perform  functions",
    fg="green",
    bg="#000000",
    font=("Veronica",14),
    justify="center",
    wraplength=450
)
note_label.pack(side=BOTTOM,pady=(0,80))

second_label=Label(f2,text='speak these to perform functions',font=('Consolas',14,),fg="orange"
,justify="center",bg="#000000")
second_label.pack(pady=(5,0))

notify_label=Label(
    f3,
    text='This is test label',
    font=("Script Mt",10),
    justify='center',
    bg="#000000",
    fg="#ffffff"
)
notify_label.pack()

#-----------------------------------------------------------------------------------------------------------

''' radiobuttons '''

var=IntVar()
var.set(1)

s=ttk.Style()
s.configure("TRadiobutton",background="#000000", foreground="#ffffff")

r1=ttk.Radiobutton(f2,value=1,variable=var,text='open google',style="TRadiobutton")
r1.place(x=10,y=35)


r2=ttk.Radiobutton(f2,text='open youtube',value=1,variable=var,style="TRadiobutton")
r2.place(x=10,y=60)

r3=ttk.Radiobutton(
    f2,
    value=1,
    variable=var,
    text='open stackflow',
    style="TRadiobutton"
)
r3.place(x=10,y=85)

r4=ttk.Radiobutton(
    f2,text='play music',
    value=1,
    variable=var,
    style="TRadiobutton")
r4.place(x=350,y=35)

r5=ttk.Radiobutton(
    f2,text='open notepad',
    value=1,
    variable=var,
    style="TRadiobutton"
)
r5.place(x=350,y=60)

#-----------------------------------------------------------------------------------
s2=ttk.Style()
s2.configure("TButton",background="#000000")

help_button=Button(
    f4,
    text='Help',
    bd=0,
    font=("Consolas",16),
    bg="#f2f2f2",
    width=8,
    relief='groove',
    command=call
)
help_button.pack(side=BOTTOM)

#-------------------------------------------------------------------------------------

root.mainloop()