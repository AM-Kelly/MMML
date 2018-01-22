#!/bin/sh
#This script will ensure that the mic is configured correctly for MM-alexa

export AUDIODEV=hw:1
export AUDIODRIVER=alsa

echo "Complete! (test with 'Rec test.flac/wav')"
#End of script

