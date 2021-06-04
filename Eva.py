import JarvisAI
import re
import pprint
import random
from tkinter import *
from tkinter.ttk import *
from time import strftime
import phonenumbers
import time
obj = JarvisAI.JarvisAssistant()
def t2s(text):
    obj.text2speech(text)
print("Hello I am Eva. What can I do for you?")
t2s("hello i am Eva. What can i do for you")

while True:
    res = obj.mic_input()
    if re.search('hello', res):
        print('Hi, I am your Assistant Eva')
        t2s('Hi,I am your Assistant Eva')
    if re.search('your name|who are you', res):
        print("My name is Eva, I am your personal assistant")
        t2s("My name is Eva, I am your personal assistant")
    if re.search('how are you', res):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")
    if re.search('what can you do', res):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "news": "Example: 'news for today' ",
            "time":"Example: 'show me the time' ",
            "phone number":"Example:'verify the phone number'",
            "birthday":"Example: 'search birthday'",
            "joke":"Example: 'tell me a joke' "
        }
        ans = """I can do lots of things, for example you can ask me time, date,  
                I can open websites for you, tell you a joke, launch application , tell the service provider of your phone number and more. 
                See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        t2s(ans)
    if re.search('date', res):
        date = obj.tell_me_date()
        print(date)
        print(t2s(date))
    if re.search('show me the time',res):
        root = Tk()
        root.title("Clock")
        def time():
            string = strftime('%H:%M:%S %p')
            label.config(text=string)
            label.after(1000, time)
        label = Label(root, font=("ds-digital", 80), background="black", foreground="cyan")
        label.pack(anchor="center")
        time()
        mainloop()

    if re.search('tell me a joke', res):
        li = ['Mother: Did you enjoy your first day at school? Girl: First day? Do you mean I have to go back tomorrow? ',
              'If big elephants have big trunks, do small elephants have suitcases?',
              'In a restaurant: Customer: Waiter, waiter! There is a frog in my soup!!! Waiter: Sorry, sir. The fly is on vacation.',
              'Student: I was born in California. Teacher: Which part? Student: All of me.',
              'Teacher: Do you have trouble making decisions? Student: Well...yes and no.',
              'Son: Dad, what is an idiot? Dad: An idiot is a person who tries to explain his ideas in such a strange and long way that another person who is listening to him cannot understand him. Do you understand me? Son: No.',
              'Teacher: How can we get some clean water? Student: Bring the water from the river and wash it.',
              'Father: Can a kangaroo jump higher than the Empire State Building? Son: Yes, because the Empire State Building cannot jump!'
              ]
        response = random.choice(li)
        print(f"{response}")
        t2s(f"{response}")
    if re.search('search birthday',res):
        t2s('enter name to look for birthday')
        dicti = {"ishita": "26 january", "sam": "28 aug", "harry": "5 june", "arya": "16 march"}
        name = input("Enter name to look for Birthday: ")
        birthday = dicti.get(name, "No data found")
        speak = "{}'s birthday is on {}".format(name, birthday)
        t2s(speak)
        print(name, "'s birthday is on", birthday)
    if re.search('open', res):
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain)
        print(open_result)
        t2s("opening "+domain+"for you")
    if re.search('launch', res):
        dict_app = {
            'chrome': "C:\Program Files\Google\Chrome\Application\chrome.exe",
            'microsoft edge': "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
        }
        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)
    if re.search('verify the phone number',res):
        t2s('Enter the phone number')
        num = input("Enter the phone number: ")
        number = phonenumbers.parse(num)
        from phonenumbers import geocoder
        print(geocoder.description_for_number(number, "en"))
        t2s('The phone number belongs to')
        t2s(geocoder.description_for_number(number, "en"))
        from phonenumbers import carrier
        print(carrier.name_for_number(number, "en"))
        t2s('The service provider of the phone number is')
        t2s(carrier.name_for_number(number, "en"))
    if re.search('tell me the news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 3 of them")
        t2s(news_res[0])
        t2s(news_res[1])
        t2s(news_res[2])
    if re.search('thank you', res):
        t2s('You are welcome')
        print("You are welcome!!")
        break