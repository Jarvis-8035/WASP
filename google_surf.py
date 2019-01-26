from selenium import webdriver
import requests
import bs4
import random
import time
import speech_recognition as sr

r = sr.Recognizer()
r.energy_threshold=2500
r.operation_timeout = 2
num_list = ['one','two','to','too','three','four','five','1','2','3','4','5']
num_dic = {'one':1,'two':2,'three':3,'four':4,'five':5,'to':2,'too':2}

def listenn():
    while True:
        with sr.Microphone() as source :
            print("Say something!")
            audio = r.listen( source )
        try:
            strr = r.recognize_google(audio)
            strr = strr.lower()
            sx = strr.split(" ")
            if sx[0]=="open" and sx[2] in num_list:
                if len(sx[2])==1:
                    return int(sx[2])
                return num_dic[sx[2]]
            return strr
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

query_url = "https://google.com/search?q="

def search():
#    def back_click():
#        browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
    browser = webdriver.Chrome("E:\chromedriver.exe")
    browser.get("https://google.com")
    st = listenn()
    if st=="close":
        browser.quit()
    st = st.split(" ")
    st = "+".join(st)
    url = query_url + st
    request = requests.get(url)
    browser.get(url)
    soup = bs4.BeautifulSoup(request.text, "lxml")
    tracks = soup.select("h3")[3:]
    track_links = []
    track_names = []

    for index, track in enumerate(tracks):
        track_links.append(track.a.get("href"))
        track_names.append(track.text)
    while True:
        choice = listenn()
        if choice == "close":
            browser.quit()
            break
        print("Opening : " + track_names[choice])
        browser.get("http://google.com" + track_links[choice])
    #    browser.find_element_by_css_selector('.sc-button-play.playButton.sc-button.m-stretch').click()
#search("how are you")
