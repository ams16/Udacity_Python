import os

def rename_files():

	# 1 Get the names of files from the folder containing the pictures
	file_list = os.listdir("/home/ams-lin/Pictures/prank/prank/")
	print(file_list)

	# 2 Rename the files
	os.renamefiles()
rename_files()
