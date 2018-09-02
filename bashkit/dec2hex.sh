#!/bin/bash
if (( $# == 1 )) ; then
    printf "%x\n" $1
else
    echo "Usage: dec2hex.sh <decimal_number>"
fi
#EOF
