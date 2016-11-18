"""
	Kirk Hardy November 2016
	
	used to copy survey database files from palm sdcards into one location
	once all the files are in place a seperate script is run to compile the singular database
"""

import os
from shutil import copyfile

destination_prefix 	= 'files/' # this should be changed if the name of the destination directory is changed
source_suffix 		= 'AnswersArchive/' # change this if the SDcard directory structure changes

sdcards = []
search_card = 'COM' # all SDcards should be named 'COM0##'. If there's a different signifier, alter this line

volumes = os.listdir('/Volumes') # all attached drives

for volume in volumes:
	if search_card in str(volume):
		sdcards.append(volume) # append to list of actual sdcards

for sdcard in sdcards: # for every actual sdcard

	answerFiles = os.listdir( '/Volumes/' + str(sdcard) + '/' + source_suffix ) # answers are in multiple files 

	for answerFile in answerFiles:
		source 		= '/Volumes/' + str(sdcard) + '/' + source_suffix + str(answerFile) # build the filepaths
		destination = destination_prefix + str(answerFile)
	
		copyfile( source, destination ) # copy the files where we need them