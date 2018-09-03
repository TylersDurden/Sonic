import time, sys, os, array
import numpy as np, matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
import scipy
import scipy.io.wavfile

class Visualizer:
    SONG = ''   # Path to the Song for visualizing

    def __init__(self, song):
        self.SONG = song
        pygame.init()
        AudioDataStructure = DSP(self.SONG)



class DSP:
    playableName  = ''

    def __init__(self, audioFile):

        self.playableName = audioFile
        buff = self.get_raw_bytes(audioFile)

        # What if I did the integer conversion RIGHT after byte conv
        # in dump_bufferto_txt method below?
        nbytes = self.dump_bufferto_txt(buff)
        start = time.time()

        os.system('cat data.txt | while read line; do  ./hex2dec.sh $line >> sampels.txt; done; rm data.txt')
        print "Decoded all " + str(nbytes/10000) + "KB in "\
              + str(start - time.time())+"s"

        # This part doesn't crash but takes forever
        # self.hex_process(nbytes)

    def get_raw_bytes(self,audioFile):
        f = open(audioFile, 'r')
        print(audioFile + " size is :" + str(f.__sizeof__()))
        buffer = []
        nbuffs = 0
        try:
            for chunk in f.read():
                buffer.append("0x" + chunk.encode('hex'))
                nbuffs += 1
        except KeyboardInterrupt:
            pass
        print("****                     ****\n" +
              str(nbuffs) + " Bytes Captured")
        print str(nbuffs*16 / (44100)) + "s of data"
        return buffer

    def dump_bufferto_txt(self,buffer):
        f = open('data.txt','w')
        n = 0
        bcount = 1
        buff = []
        nums = []
        for byte in buffer:

            f.write(byte+'\n')
            n += 1
        print str(n) + " Bytes written to data.txt"
        return n

    def hex_process(self, length):
        hexdata = open('data.txt','r')
        os.system('touch nums.txt')
        lines = 0
        for line in hexdata.readlines():
            os.system('bashkit/hex2dec.sh '+line+' >> num.txt')
            lines += 1
        print(' lines of Hex translated to integers')
        if lines == length:
            os.system("rm data.txt")
            return 0
        else:
            return 1


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
