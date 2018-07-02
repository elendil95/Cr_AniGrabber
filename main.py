import os.path
import argparse
import subprocess

PATH = "~/CR_aniGrabber/"
series_name = input("Input name of the anime (Romanji only): ")
input_file = input("Please select a file (please include extnsion if present): ")
try:
	full_path=PATH+series_name
	normal_path=os.path.expanduser(full_path)
	os.makedirs(normal_path)
except FileExistsError as e:
	raise e
	print("Directory already exists, continuing...")
else:
	print("Creating directoy structure..")

# try:
# 	os,path.isfile(PATH"/"input_file)
# except FileNotExistError as e:
# 	raise e


