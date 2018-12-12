#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import speech_recognition as sr
import pygame
import _thread
import datetime
from weather import Weather, Unit
from multiprocessing import Process
def clock():
    listi = str(datetime.datetime.now()).split(" ")
    text = font.render(listi[1], True, WHITE)
    window.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.set_caption(texti)
 
def speachToText():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        #`r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        print("You said: " + r.recognize_google(audio))
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
pygame.init()
window_size = window_width, window_height = 640, 480
window = pygame.display.set_mode(window_size)
mutex = _thread.allocate_lock()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
window.fill(BLACK)
font = pygame.font.SysFont("comicsansms", 72)
while (True):
    texti = ""
    texti = speachToText()
    if (texti == "time"):
        clock()
    elif (texti == "weather"):
        text = font.render("Where?", True, WHITE)
        window.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.update()
        window.fill(BLACK)
        weather = Weather(unit=Unit.CELSIUS)
        stadur = speachToText()
        location = weather.lookup_by_location(stadur)
        condition = location.condition
        text = font.render(condition.text, True, WHITE)
        window.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.update()
    window.fill(BLACK)