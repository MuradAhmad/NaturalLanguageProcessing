#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:05:47 2019

@author: murad
"""
import pickle

from senti_client import sentistrength

senti = sentistrength('EN')

def Senti_List(List):
    Senti_Labels = []
    Score = []
    for label in List:
        Dict = {}
        res = senti.get_sentiment(label)
        Dict[label] = res
        Senti_Labels.append(Dict)
        Score.append(res['neutral'])
    return Senti_Labels,Score

def SaveListToFile(mylist,filename):
    with open(filename, 'wb') as filehandle:
         pickle.dump(mylist, filehandle)
         
def LoadFileToList(filename):
    mylist = []
    with open(filename, 'rb') as filehandle:  
         mylist = pickle.load(filehandle)
    return mylist

def file2txt(path):
    File = open(path,'r')
    return File.readlines()

L1 = file2txt('Human.txt')
L2 = file2txt('Robot.txt')

#Senti_Labels1, Score1 = Senti_List(L1)
#Senti_Labels2, Score2 = Senti_List(L2)

#SaveListToFile(Senti_Labels1,'Senti_Labels1.pkl')
#SaveListToFile(Score1,'Score1.pkl')

#SaveListToFile(Senti_Labels2,'Senti_Labels2.pkl')
#SaveListToFile(Score2,'Score2.pkl')

Senti_Labels1 = LoadFileToList('Senti_Labels1.pkl')
Score1 = LoadFileToList('Score1.pkl')

Senti_Labels2 = LoadFileToList('Senti_Labels2.pkl')
Score2 = LoadFileToList('Score2.pkl')
