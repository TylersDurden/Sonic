import time, sys, os
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation


def select_song(hasFolderTunes):
    print "[*]~-----------------------------------------------------~[*]"
    Music = {}
    i = 0
    if hasFolderTunes=='y' or hasFolderTunes == 'Y' or hasFolderTunes=='yes':
        songlib = open('songs.txt', 'r')
        for line in songlib.readlines():
            i += 1
            print "[" + str(i) + "] - " + line.replace('\n','')
            Music[i] = line.replace('\n','')
    else:
        os.system('find -name *.mp3 >> mp3.txt')
        songs = open('mp3.txt', 'r')
        for line in songs.readlines():
            i += 1
            print "[" + str(i) + "] - " + line.replace('\n', '')
            Music[i] = line.replace('\n', '')
    print "[*]~-----------------------------------------------------~[*]"
    UserChoice = Music[int(input('Enter a selection: \n'))]
    print "You selected: " + UserChoice
    

def main():
    print('Have you previously run sonic fingers,\n'
          '(and therefore already have music loaded)?')
    select_song(str(input('[y/n]')))


if __name__ == '__main__':
    main()
