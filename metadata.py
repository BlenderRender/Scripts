#Imports
import mutagen
import glob
import os
import re

#Metadata Variables
artist = ''
album = ''
title = ''

#Array for regex parseing
split = []
#Song Counter
count = 0

#Path variable for mp3 folder (change accordingly)
path = 'mp3/'

from mutagen.mp4 import MP4
from mutagen.easyid3 import EasyID3

#Runs through the file structure - Artist / Album / SongTitle .m4a
for infile in glob.glob( os.path.join(path, '*/*/*.m4a') ):

		#Parses mp3 file structure using '.' '/' and '-' delimiters	
		split = re.split('\.|/|-', infile)
		#Sets variables and replaces underscores with white space
		artist = re.sub('_', " ", split[1])
		album = re.sub('_', " ", split[2])
		title = re.sub('_', " ", split[4])
		
		#Optional Print Statements & Counter
		print count
		print "artist: " + artist
		print "album: " + album
		print "title: " + title
		count = count + 1
		
		#Sets and Saves Metadata Variables
		audio = mutagen.File(infile, easy=True)
		audio["title"] = title
		audio["album"] = album
		audio["artist"] = artist
		audio.save()
		
		