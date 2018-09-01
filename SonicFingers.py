import os, sys, wave, time
import numpy as np
from itertools import permutations
from itertools import combinations


class SonicFingers:
    albums = ['Aenima', 'Martyr','ReVol2']
    artists = ['Tool', 'Immortal Technique']
    MusicLibrary = {}

    def __init__(self):
        os.system('ls Aenima >> library.txt; cd ..')
        os.system('ls Martyr >> library.txt; cd ..')
        os.system('ls ReVol2 >> library.txt; cd .. ')
        musicLib = []
        f = open('library.txt','r')
        for song in f.readlines():
            musicLib.append(song.replace('\n',''))
        print(str(len(musicLib))+" Songs found")
        os.system('rm library.txt')

    def run(self):
        if str(input(' Want to listen in Shuffle Mode? [y/n]: ')) == 'y':
            self.shuffle_player()
        if str(input(' Want to pick a song? [y/n]:')) == 'y':
            self.song_search()

    @staticmethod
    def filereader(fname,path):
        filecontents = []
        f = open(path+'/'+fname,'r')
        for line in fname:
            filecontents.append(line.replace('\n',''))
        return filecontents

    def shuffle_player(self):
        """
                 _______________________
                |(<(< SHUFFLE MODE >)>) |
                |:return: Sweet Tunes :)|
                |< < SONIC_FINGERS > >  |
                |***********************|
                """
        print("*~- - - -=//SHUFFLE_MODE\\\\=- - - -~*")
        print("[X] Hit SPACE to Pause")
        print("[X] Hit Control+C to Skip a song")
        os.system('find -name *mp3 >> songs.txt')
        songs = []
        i = 0
        f = open('songs.txt', 'r')
        for song in f.readlines():
            songs.append(song.replace('\n',''))
            self.MusicLibrary[i] = song.replace('\n','')
            i += 1

        # Create a random IV for shuffle mode
        nsongs = len(self.MusicLibrary.keys())
        playlist = combinations(self.MusicLibrary.keys(),4)

        randomLists = []
        for tracks in playlist:
            randomLists.append(tracks)
        print(str(playlist.__sizeof__())+" Possible Playlists")
        rand = np.random.randint(0,nsongs,1,dtype=int)

        # Now play the random list
        print("Selecting random playlist "+str(rand))
        for track in randomLists.pop(rand):
            print("[*] Playing Track "+self.MusicLibrary[track]+" [*]")
            SONG = "'"+self.MusicLibrary[track]+"'"
            os.system("mpg123 "+SONG)

    def song_search(self,):
        """
        SONG_SEARCH - Lets the user select a song from the available
        music library
        :return:
        """
        print("Here's the music library. Enter the Number to play:\n")
        os.system('find -name *mp3 >> songs.txt')
        songs = {}
        i = 0
        f = open('songs.txt', 'r')
        for song in f.readlines():
            songs[i] = song.replace('\n', '')
            print(str(i)+" : "+song.replace('\n', ''))
            i += 1
        selection = int(input('Enter selection: '))
        SONG = "'"+songs[selection]+"'"
        print("[*] PLAYING "+songs[selection]+"[*]")
        os.system("mpg123 " + SONG)

def get_working_directory():
    os.system('pwd >> path.txt')
    dir = SonicFingers.filereader('path.txt')


def main():
    if len(sys.argv) < 2:
        SonicFingers().run()
    else:
        if sys.argv[1] == '-f':
            SonicFingers.filereader(sys.argv[2],)
        if sys.argv[1] == '-listen':
            SonicFingers().song_search()
    # CLEAN UP
    # os.system('rm songs.txt')


if __name__ == '__main__':
    main()
