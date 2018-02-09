import sys
from chatbot import ChatBot

##
# Runs a terminal-based chatbot program.
# That ChatBot's communication can be specified within a .json file.
# The filename should be specified as an argument to the program.
# Example usage: $python3 chat_main.py script.json
##
if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please specify a json file to act as the script for this session.")
	else:
		script = sys.argv[1]
		chatbot = ChatBot(script)
		chatbot.start_conversation()