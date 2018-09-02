#!/bin/bash
if (( $# == 1 )) ; then 
    printf "%d\n" $1
else
    echo "Usage: hex2dec.sh <hex>"
fi
#EOF
