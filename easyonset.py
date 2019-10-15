#!/usr/bin/env python3

# EASYONSET™
# Author: Zachary Bowditch (Edargorter) 2017
# Quick-access text-to-speech using pre-installed tts software.
# Ideal for throat infections.

import os
import re
import platform
import time
import random
from _thread import *

# TODO create alternative link/symlink to fix directory issues 
path = os.getenv("HOME") + "/Easyonset"

os_name = platform.system()
if os_name == "Linux":
    speak_com = "espeak"
elif os_name == "Darwin":
    speak_com = "say"

global options
global dictionary
global topics
global topic_dictionary
global title
global about

options = ["Salutations", "Goodbyes", "Responses", "Statements", "Questions", "Topics"]
dictionary = []
topics = []
topic_dictionary = []
title = []
about = "I was designed and built in Python, by Zachary Bowditch, also known as Edargorter, in the event that he wouldn't have to use his voice, to verbally communicate, should it be too hoarse. Easy Onset grants the user an efficiently-organised selection of key phrases, and allows the user to customize the program further, by grouping topics and adding relevant phrases to those topics. The program verbalises the text, by using the Terminal's default text-to-speech program."
reset_text = "Reloading data..."

''' Helper functions '''

def newline(n=1):
        print("\n"*n)

def clearScreen():
        print("\033[H\033[J")

def process_sound(speech):
        os.system('{} "{}"'.format(speak_com, speech))

def voice(output):
        start_new_thread(process_sound, (output,))

def displayOptions():
        i = 0
        print("Type 'about' for more info. Type 'reset' to reload data.")
        newline()
        print("%d)  Exit" % i)
        while i < len(options):
                print(str(i + 1) + ")  " + options[i])
                i += 1
        i += 1
        print("%d)  Enter VIM" % i)
        i += 1
        newline()
        print("To verbalise a number: enter '.' and then the number.")
        print("Otherwise, enter in your text here")
        newline()
        print("y = 'yes' n = 'no'")

def dislaySettings():
        clearScreen()

def displayTitle():
        limit = len(title)
        for i in range(limit):
                print(title[i], end="")

def addTopic(topic):
        global topics
        topic_file = open(path + "/Topics/topics.txt", "w")
        topics.append(topic)
        topics.sort()
        limit = len(topics)
        topic_file.write("TEMP" + "\n")
        for i in range(limit - 1):
                topic_file.write(topics[i] + "\n")
        topic_file.write(topics[limit - 1])
        topic_file.close()
        new_topic_file = open(path + "/Topics/topics" + ".txt", "w")
        new_topic_file.close()
        empty()
        readData()

def addPhrase(phrase, topicnum):
        global topic_dictionary
        phrase_file = open(path + "/Topics/" + topics[topicnum] + ".txt", "w")
        topic_dictionary[topicnum].append(phrase)
        topic_dictionary[topicnum].sort()
        limit = len(topic_dictionary[topicnum])
        phrase_file.write("TEMP" + "\n")
        for i in range(limit - 1):
                phrase_file.write(topic_dictionary[topicnum][i] + "\n")
        phrase_file.write(topic_dictionary[topicnum][limit - 1])
        phrase_file.close()

def displayAddPhraseOptions(topicnum):
        clearScreen()
        new_phrase = input("Enter in a new phrase: ")
        resp = input("Are you sure? (y/n) ")
        if resp.lower() == 'y':
                addPhrase(new_phrase, topicnum)
        return

def displayPhrases(topicnum):
        message = ""
        global topic_dictionary
        while True:
                clearScreen()           
                limit = len(topic_dictionary[topicnum])
                print("0)  Back")
                print("1)  Add Phrase")
                for i in range(limit):
                        print(str(i + 2) + ")  " + topic_dictionary[topicnum][i])
                newline()
                print(message)
                newline()
                text = input()
                try:
                        num = int(text)
                        message = ""
                        if num == 0:
                                return
                        elif num == 1:
                                displayAddPhraseOptions(topicnum)
                        elif num < 0 or num > limit + 1:
                                message = "Integer out of range."
                        else:
                                voice(topic_dictionary[topicnum][num - 2])
                                return
                except ValueError:
                        message = "Invalid input. Please enter in an integer."

def displayItems(n):
        global dictionary
        message = ""
        while True:
                clearScreen()
                limit = len(dictionary[n])
                print("0)  Back")
                for i in range(limit):
                        print(str(i + 1) + ")  " + dictionary[n][i])
                newline()
                print(message)
                newline()
                text = input()
                try:
                        num = int(text)
                        message = ""
                        if num == 0:
                                return
                        elif num < 0 or num > limit:
                                message = "Integer out of range."
                        else:
                                voice(dictionary[n][num - 1])
                                return
                except ValueError:
                        message = "Invalid input. Please enter in an integer."

def displayAddOptions():
        clearScreen()
        new_topic = input("Enter in new topic: ")
        resp = input("Are you sure? (y/n) ")
        if resp.lower() == "y":
                addTopic(new_topic)

def displayTopics():
        global topics
        message = ""
        while True:
                limit = len(topics)
                clearScreen()
                print("0)  Back")
                print("1)  Add Topic")
                for i in range(limit):
                        print(str(i + 2) + ")  " + topics[i])
                newline()
                text = input()
                try:
                        num = int(text)
                        message = ""
                        if num == 0:
                                break
                        elif num == 1:
                                displayAddOptions()
                        elif num < 0 and num > limit:
                                message = "Integer out of range"
                        else:
                                displayPhrases(num - 2)
                                return
                except ValueError:
                        message = "Invalid input. Please enter in an integer."

def use_vim():
        resp_tmp = "resp_tmp.txt"
        os.system("echo '' > %s" % resp_tmp)
        os.system("vi %s" % resp_tmp)
        f = open(resp_tmp)
        lines = f.readlines()
        resp = '\t'.join([line.strip() for line in lines])
        submit(resp)

def submit(s):
        global about
        global reset_text
        s = s.lower()
        s = re.sub('[^A-Za-z0-9 ]+', '', s)
        if s == "n":
                voice("No")
        elif s == "y":
                voice("Yes")
        elif s == ".":
                s = input() 
                voice(s)
        elif s == "about":
                voice(about)
        elif s == "reset":
                voice(reset_text)
                reset() 
        elif s == 'vi' or s == 'vim':
                use_vim()
        else:
                try:
                        num = int(s)
                        if num > 0 and num < 6:
                                displayItems(num - 1)
                        elif num == 6:
                                displayTopics()
                        elif num == 7:
                                use_vim()
                        else:
                                return "Number out of range."
                except ValueError:
                        voice(s)
        return ""

def empty():
        del dictionary[:]
        del topics[:]
        del topic_dictionary[:]

def writeToFile(filenum, string):
        global dictionary
        wordfile = open(path + "/Options/" + options[filenum] + ".txt", "w")
        dictionary[filenum].sort()
        limit = len(dictionary[filenum])
        wordfile.write("TEMP"  + "\n")
        for i in range(limit):
                wordfile.write(dictionary[filenum][i] + "\n")
        readFile(filenum)
        wordfile.close()

def readFile(filenum):
        wordfile = open(path + "/Options/" + options[filenum] + ".txt", "r")
        dictionary[filenum] = wordfile.readlines()
        dictionary[filenum].pop(0)
        limit = len(dictionary[filenum])
        for i in range(limit):
                dictionary[filenum][i] = dictionary[filenum][i].rstrip()
        wordfile.close()

def readTopic(topicnum):
        global topics
        topic = open(path + "/Topics/" + topics[topicnum] + ".txt", "r+")
        topic_dictionary.append([])
        limit = len(topic_dictionary) - 1
        topic_dictionary[limit] = topic.readlines()
        limit_range = len(topic_dictionary[limit])
        for i in range(limit_range):
                topic_dictionary[limit][i] = topic_dictionary[limit][i].rstrip()
        topic.close()

def readTitle():
        global title
        titlefile = open(path + "/title.txt", "r+")
        title = titlefile.readlines()

def readTopicFiles():
        global topics
        topic_file = open(path + "/Topics/topics.txt", "r+")
        topics = topic_file.readlines()
        topics.pop(0)
        limit = len(topics)
        print("retrieving files...")
        for i in range(limit):
                topics[i] = topics[i].rstrip()
                readTopic(i)
        print("Classifying data...")
        topic_file.close()      

def readData():
        print("Loading dictionary...")
        for i in range(5):
                dictionary.append([])
                readFile(i)
        print("Loading topics...")
        readTopicFiles()
        print("Done.")

def restart():
    os.execv("easy")
    exit()

def reset():
        empty()
        readData()

def run():
        message = ""
        readData()
        readTitle()
        voice(dictionary[0][random.randint(1, len(dictionary[0]) - 1)])
        while True:
                clearScreen()
                displayTitle()
                newline(2)
                displayOptions()
                newline()
                print(message)
                newline()
                print("-> ", end=" ")
                text = input()
                if text == "0":
                        voice(dictionary[1][random.randint(1, len(dictionary[1]) - 1)])
                        clearScreen()
                        exit()
                message = submit(text)
run()
