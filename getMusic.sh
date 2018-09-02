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
python SonicFingers.py
