#!/bin/sh

# Download Aenima by tool 
mkdir Aenima
cd Aenima
wget https://archive.org/compress/15ThirdEye_201611/formats=VBR%20MP3&file=/15ThirdEye_201611.zip
sleep 10
unzip 'formats=VBR MP3'
ls
rm 'formats=VBR MP3'
cd ..
sleep 10
# Grab "The Martyr" album 
mkdir Martyr
cd Martyr
wget https://archive.org/compress/Immortal_Technique_-_The_Martyr-2011/formats=VBR%20MP3&file=/Immortal_Technique_-_The_Martyr-2011.zip
sleep 10
unzip 'formats=VBR MP3'
ls
rm 'formats=VBR MP3'
cd ..

# A few Tracks of Revolutionary Vol. 2
mkdir ReVol2
cd ReVol2
wget https://archive.org/compress/immortaltechnique/formats=VBR%20MP3&file=/immortaltechnique.zip
sleep 10
unzip 'formats=VBR MP3'
ls
rm 'formats=VBR MP3'
cd ..
python SonicFingers.py

