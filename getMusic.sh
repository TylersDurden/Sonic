#!/bin/sh
dir=$PWD
# Download Aenima by tool 
mkdir Aenima
cd Aenima
su root $dir/getTool.sh
cd ..
sleep 10
# Grab "The Martyr" album 
mkdir Martyr
cd Martyr
su root $dir/martyr.sh
cd ..

# A few Tracks of Revolutionary Vol. 2
mkdir ReVol2
cd ReVol2
su root $dir/revolutionary.sh
cd ..

mkdir JAM
# Let the user add music
echo 'Enter a path to a folder with some mp3s you want to use: '
echo '* If Debug Mode Enter D *'
p=read
if $p='D' ; then
    ls /media/root/'FLASH DRIVE'/MusicLibrary/Music >> songs.txt
    echo '|ADMIN MODE|'
    cat songs.txt
else
    ls $p >> songs.txt
    cat songs.txt
fi

python SonicFingers.py
