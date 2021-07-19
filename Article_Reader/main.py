import pyttsx3  # version 2.7
import requests
from bs4 import BeautifulSoup

url = "https://medium.com/hackernoon/50-data-structure-and-algorithms-interview-questions-for-programmers-b4b1ac61f5b0"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume',1.0)


def content(url_input):
    res = requests.get(url_input)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = []
    res = ""
    for i in range(len(soup.select('.p'))):
        article = soup.select('.p')[i].getText().strip()
        articles.append(article)
        res = " ".join(articles)
    return res


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def read_file(file):
    f = open(file, "r")
    return f.read()


contents = content(url)
# contents = read_file("Speak.txt")
print(contents)
speak(contents)
