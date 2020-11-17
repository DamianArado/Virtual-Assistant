#Version 1
import JarvisAI
import re
import pprint
import random

# Object creation of JarvisAI as per as documentation
obj = JarvisAI.JarvisAssistant()

# t2s(text) function will convert any text to speech.
# The entire program we will use (call) this function to produce speech from text.
def t2s(text):
    obj.text2speech(text)

#‘mic_input()’ will try to fetch audio from the computer’s microphone continuously.
# It will process the audio and return text in ‘res’ variable.
# We can use this ‘res’ variable to perform some action according to user input.
# We are using a regular expression to match queries in user input. If ‘weather’ or ‘temperature’ is found in user input ‘res’ then we want to do weather forecasting.
# No need to write things from scratch, just call ‘obj.weather(city=city)’.
# You just need to fetch the city from user input and pass it to the weather function. It will tell you the weather forecasting for your city.
# We can pass this returned ‘weather_res’ to ‘ t2s(weather_res)’ to produce speech from ‘weather_res’ string.
while True:
    res = obj.mic_input()

    if re.search('weather|temperature', res):
        city = res.split(' ')[-1]
        weather_res = obj.weather(city=city)
        print(weather_res)
        t2s(weather_res)

# Similarly as above, match the ‘news’ word from user input ‘res’. If matched then call ‘obj.news’.
# It will return 15 news as a list of strings. So, we can fetch news as ‘news_res[0]’ and pass it to ‘t2s(news_res[0])’.
    if re.search('news', res):
        news_res = obj.news()
        pprint.pprint(news_res)
        t2s(f"I have found {len(news_res)} news. You can read it. Let me tell you first 2 of them")
        t2s(news_res[0])
        t2s(news_res[1])

# Tells about almost everything: It will fetch the first 500 characters from Wikipedia and return them as a string. You can use ‘obj.tell_me(topic)’.
# You need to pass ‘topic’ to ‘tell_me(topic=topic)’. The topic is the keyword you want to know about.
    if re.search('tell me about', res):
        topic = res.split(' ')[-1]
        wiki_res = obj.tell_me(topic)
        print(wiki_res)
        t2s(wiki_res)

# Date and Time: It will tell you the current date and time of your system.
    if re.search('date', res):
        date = obj.tell_me_date()
        print(date)
        print(t2s(date))

    if re.search('time', res):
        time = obj.tell_me_time()
        print(time)
        t2s(time)

# This ‘obj.website_opener(domain)’ will open any website for you. You just need to fetch the domain from user input then pass to ‘obj.website_opener(domain)’.
# It will open the website in your default browser.
    if re.search('open', res):
        domain = res.split(' ')[-1]
        open_result = obj.website_opener(domain)
        print(open_result)

# This is little tricky, in ‘obj.launch_any_app(path_of_app=path)’ the function you need to pass the path of your ‘.exe’ file.
# So we have created ‘dict_app’ dictionary which is having an ‘app name’ as key and ‘path’ as value. We can use this ‘dict_app’ for lookup. If the user input app exists in the dictionary then we will open it by fetching the path.
# The below example is only for Chrome and Epic Games.
    if re.search('launch', res):
        dict_app = {
            'chrome': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
            'epic games': 'C:\Program Files (x86)\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe'
        }

        app = res.split(' ', 1)[1]
        path = dict_app.get(app)
        if path is None:
            t2s('Application path not found')
            print('Application path not found')
        else:
            t2s('Launching: ' + app)
            obj.launch_any_app(path_of_app=path)

# Greetings and Chat, you can create greetings and chat like this for now. Major work in progress
    if re.search('hello', res):
        print('Hi')
        t2s('Hi')

    if re.search('how are you', res):
        li = ['good', 'fine', 'great']
        response = random.choice(li)
        print(f"I am {response}")
        t2s(f"I am {response}")

    if re.search('your name|who are you', res):
        print("My name is Jarvis, I am your personal assistant")
        t2s("My name is Jarvis, I am your personal assistant")

    if re.search('what can you do', res):
        li_commands = {
            "open websites": "Example: 'open youtube.com",
            "time": "Example: 'what time it is?'",
            "date": "Example: 'what date it is?'",
            "launch applications": "Example: 'launch chrome'",
            "tell me": "Example: 'tell me about India'",
            "weather": "Example: 'what weather/temperature in Mumbai?'",
            "news": "Example: 'news for today' ",
        }
        ans = """I can do lots of things, for example you can ask me time, date, weather in your city,
        I can open websites for you, launch application and more. See the list of commands-"""
        print(ans)
        pprint.pprint(li_commands)
        t2s(ans)
