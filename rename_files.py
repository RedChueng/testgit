import os

def rename_files():
	# 1) get file names from a folder. checked
	filename_list = os.listdir('F:\ML\prank\prank')
	# print filename_list
	old_path = os.getcwd()
	print old_path
	os.chdir('F:\ML\prank\prank')

	# 2) for each file, rename filename
	for filename in filename_list:
		os.rename(filename, filename.translate(None, '0123456789'))
	os.chdir(old_path)
	# print filename_list

rename_files()