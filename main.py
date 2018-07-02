import os.path
import argparse
import subprocess

PATH = "~/CR Anime/"
series_name = input("Input name of the anime (Romanji only): ")
full_path=PATH+series_name
normal_path=os.path.expanduser(full_path)

if (os.path.isdir(normal_path)):
	print("Folder "+series_name+" already exists.")
else:
	os.makedirs(normal_path)
	print("Creating directory "+series_name+" in "+PATH)
	
input_file = input("Please select a file (please include extnsion if present): ")			

try:
	os.path.isfile(os.path.join(normal_path, input_file))
	print("File "+input_file+" found.")
except FileNotFoundError:
 	print("File "+input_file+" does not exist")



 