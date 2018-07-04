#TODO: Check logic because the two conditions are probably redundant. seems to work for now though...
import os
import os.path
import fnmatch


def searchforInputfile(search_path, file):
	for dirpath, dirname, filename in os.walk(search_path):
		if file in filename:
 			final_filepath = os.path.join(dirpath, file)
 			print("Input file \'"+final_filepath+"\' found")
 			return final_filepath
		for name in fnmatch.filter(filename, "%s.???"%(file)):
			final_filepath=os.path.join(dirpath, name)
			print("file " +name+ " found")
			#print(final_filepath)
			return final_filepath
			break
		else:
			print("File "+file+" does not exist. re-run the program and select a valid file")

#print(searchforInputfile('/home/elendil/CR Anime/', 'konosuba'))