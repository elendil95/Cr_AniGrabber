from __future__ import unicode_literals
import youtube_dl
import sys
import os.path
import argparse
import subprocess


BASE_PATH = os.path.join(os.environ.get('HOME'),"CR Anime")
series_name = input("Input name of the anime (Romanji only): ")

episode_nr = None 
#full_path=PATH+series_name
series_path=os.path.join(BASE_PATH, series_name)

if (os.path.isdir(series_path)):
	print("Series \'"+series_name+"\'"+" already exists, moving into it...")
else:
	os.makedirs(series_path)
	print("Creating series \'"+series_name+"\'"+" in "+BASE_PATH)

season_nr = input("Input a season number (The season you want, not the total number of seasons):")
seasons=os.listdir(series_path)
if seasons == []:
	print("There are currently no seasons of this anime: creating season ",season_nr,"...")
	os.makedirs(os.path.join(series_path, "Season %s" %(season_nr)))
else:
	season_str=', '.join(sorted(seasons))		
	print("Anime \'"+series_name+"\'"+" contains the following seasons already: "+season_str+'\n')
	if str("Season %s" %(season_nr)) in seasons:
		print("this season already exisits! Please re-run the program and select a valid season number")
		sys.exit(1)
	else:
		print("Season number is valid, creating season "+season_nr+"..."+'\n')
		os.makedirs(os.path.join(series_path, "Season %s" %(season_nr)))	 	

input_file = input("Please select an input file containing episode urls. (include extnsion if present): ")
input_file=os.path.expanduser(os.path.join(BASE_PATH, input_file))			
if os.path.isfile(input_file) is True:
	print("File "+input_file+" found.")
	episode_nr =  len(open(input_file).read().splitlines()) #for the script to work there must be no lines after the last url
	print("Anime \'",series_name,"\' has ", episode_nr, " episodes")
else:
	file=str(os.path.join(BASE_PATH, input_file))
	print(file)
	print("File "+input_file+" does not exist. re-run the program and select a valid file")
	sys.exit(1)
print("done"+'\n')
print("Creating last directory structure...")
os.chdir(os.path.expanduser(os.path.join(series_path, "Season %s" %(season_nr))))
for x in range(episode_nr):
	os.makedirs("Episode %d" %(x+1))

# ydl_opts = {
# 	'verbose': True,
# }

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     meta = ydl.extract_info(
#         'http://www.crunchyroll.com/konosuba-gods-blessing-on-this-wonderful-world/episode-1-this-self-proclaimed-goddess-and-reincarnation-in-another-world-692393', download=False)
# print(meta)