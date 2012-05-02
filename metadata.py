import mutagen
import glob
import os
import re

artist = ''
album = ''
title = ''
split = []
count = 0
path = 'mp3/'

from mutagen.mp4 import MP4
from mutagen.easyid3 import EasyID3

for infile in glob.glob( os.path.join(path, '*/*/*.m4a') ):

		print count
		split = re.split('\.|/|-', infile)
		artist = re.sub('_', " ", split[1])
		album = re.sub('_', " ", split[2])
		title = re.sub('_', " ", split[4])
		print "artist: " + artist
		print "album: " + album
		print "title: " + title
		count = count + 1

		audio = mutagen.File(infile, easy=True)
		audio["title"] = title
		audio["album"] = album
		audio["artist"] = artist
		audio.save()