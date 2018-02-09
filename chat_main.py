import sys
import os
from chatbot import ChatBot
from file_validator import is_valid_input_file

##
# Runs a terminal-based chatbot program.
# That ChatBot's communication can be specified within a .json file.
# The filename should be specified as an argument to the program.
# Example usage: $python3 chat_main.py script.json
##
if __name__ == "__main__":
	if not is_valid_input_file(sys.argv):
		print("Please specify an existing json file to act as the script for this session.")
	else:
		script = sys.argv[1]
		chatbot = ChatBot(script)
		chatbot.start_conversation()

