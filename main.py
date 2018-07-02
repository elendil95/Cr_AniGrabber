import sys
import os.path
import argparse
import subprocess

PATH = "~/CR Anime/"
series_name = input("Input name of the anime (Romanji only): ")
season_nr = input("Input a season number (The season you want, not the total number of seasons):")
episode_nr = None 
#full_path=PATH+series_name
normal_path=os.path.expanduser(os.path.join(PATH, series_name))

if (os.path.isdir(normal_path)):
	print("Folder "+series_name+" already exists.")
else:
	os.makedirs(normal_path)
	print("Creating directory "+series_name+" in "+PATH)

seasons=os.listdir(normal_path)
if seasons == []:
	print("There are currently no seasons of this anime: creating season ", season_nr,"...")
	os.makedirs(os.path.join(normal_path, "Season %s" %(season_nr)))
else:		
	print("Anime \'"+series_name+"\'"+" contains the following seasons already: "+str(seasons))
	if str("Season %s" %(season_nr)) in seasons:
		print("this season already exisits")
		sys.exit(1)

input_file = input("Please select a file (please include extnsion if present): ")
input_file=os.path.expanduser(os.path.join(PATH, input_file))			
if os.path.isfile(input_file) is True:
	print("File "+input_file+" found.")
	episode_nr =  len(open(input_file).read().splitlines()) #for the script to work there must be no lines after the last url
	print("Anime \'",series_name,"\' has ", episode_nr, " episodes")
else:
	file=str(os.path.join(PATH, input_file))
	print(file)
	print("File "+input_file+" does not exist")
	sys.exit(1)



	#if os.path.isfile(os.path.expanduser(os.path.join(PATH, input_file))) is True: