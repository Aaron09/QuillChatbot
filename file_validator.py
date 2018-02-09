import os

def is_valid_input_file(args):
	"""
	Validates that the input file exists and is a .json file.
	@param args: the command line arguments to the program.
	"""
	if len(args) < 2:
		return False

	filename_length = len(args[1])
	return os.path.isfile(args[1]) and args[1][filename_length - 5::] == ".json"