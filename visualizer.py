import time, sys, os, array
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation

class Visualizer:
    SONG = ''   # Path to the Song for visualizing

    def __init__(self, song):
        self.SONG = song
        AudioDataStructure = DSP(self.SONG)


class DSP :

    def __init__(self, audioFile):
        f = open(audioFile,'r')
        print(audioFile+" size is :"+str(f.__sizeof__()))
        buffer = []
        nbuffs = 0
        for chunk in f.read(1024):
            buffer.append(chunk)
            nbuffs += 1
        print(str(nbuffs) + " Buffers Filled")


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
    os.system('rm mp3.txt')

    print "[*]~-----------------------------------------------------~[*]"
    print "You selected: " + UserChoice
    os.system("mpg123 '"+UserChoice+"'")
    print "[*]~-----------------------------------------------------~[*]"
    os.system('clear')
    return UserChoice


def main():
    print('Have you previously run sonic fingers,\n'
          '(and therefore already have music loaded)?')
    songPicked = select_song(str(input('[y/n]: \n')))
    Visualizer(songPicked)


if __name__ == '__main__':
    main()
