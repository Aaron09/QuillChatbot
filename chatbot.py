import json
import random

class ChatBot: 

	def __init__(self, script):
		"""
		Loads the JSON script for chat responses and initializes the bot.
		"""
		self.script = json.loads(open(script).read())
		self.user_responses = {}
		self.conversation_statements = []
		self.just_prompted_user = False

	def start_conversation(self):
		"""
		Selects an opening statement and begin's the conversation.
		"""
		introduction = self.select_greeting()
		user_response = input(introduction + "\n")

		self.conversation_statements.append(introduction)
		self.user_responses[introduction] = user_response

		self.continue_conversation(introduction)

	def continue_conversation(self, most_recent_statement):
		"""
		Continuously receieves user input and selects and displays the appropriate response.
		@param most_recent_statement: the statement printed most recently by the bot
		"""
		while (not self.has_conversation_ended(most_recent_statement)):
			statement = self.get_response(most_recent_statement)
			user_response = self.get_user_input(statement)

			if user_response is None:
				break

			self.user_responses[statement] = user_response
			self.conversation_statements.append(statement)
			most_recent_statement = statement

		goodbye_message = self.select_ending()
		print(goodbye_message)

	def has_conversation_ended(self, most_recent_statement):
		"""
		Returns whether the conversation has ended by checking user input
		against the ending statements of the script.
		@param most_recent_statement: the statement printed most recently by the bot
		"""
		return self.user_responses[most_recent_statement] in self.script["ENDINGS"]

	def get_response(self, most_recent_statement):
		"""
		Returns the appropriate response based on the most recent statement by the bot
		and the user's response.
		@param most_recent_statement: the statement printed most recently by the bot
		"""
		user_response = self.user_responses[most_recent_statement]

		if self.just_prompted_user:
			response = self.get_user_query_information(user_response, most_recent_statement)
		else:
			response = self.get_query_options_prompt()

		self.just_prompted_user = not self.just_prompted_user

		return response

	def get_user_input(self, statement):
		"""
		Returns the input from the user or ends the program
		if the user entered a keyboard interrupt.
		@param statement: the next statement from the chatbot to prompt the user.
		"""
		try: 
			user_input = input(statement + "\n")
			return user_input
		except KeyboardInterrupt:
			return None

	def get_query_options_prompt(self):
		"""
		Returns a string containing the query options possible for the user.
		"""
		response_options = list(self.script["QUERIES"].keys())

		response = ""
		for i in range(0, len(response_options)):
			response += str(i + 1) + ". " + response_options[i] + "\n"

		return response

	def get_user_query_information(self, user_query, most_recent_statement):
		"""
		Returns the appropriate response based on the previously selected query by the user.
		@param user_query: the user's selected query based on the previous prompt.
		@param most_recent_statement: the statement printed most recently by the bot.
		"""
		if not user_query.isdigit():
			return "Please enter a digit indicating which option."

		queries = list(self.script["QUERIES"].keys())
		response = self.script["QUERIES"][queries[int(user_query) - 1]]
		return response

	def select_greeting(self):
		"""
		Returns a randomly selected greeting from the possible greetings specified by the script.
		"""
		num_greetings = len(self.script["GREETINGS"])
		return self.script["GREETINGS"][random.randint(0, num_greetings - 1)]

	def select_ending(self):
		"""
		Returns a randomly selected ending from the possible endings specified by the script.
		"""
		num_endings = len(self.script["ENDINGS"])
		return self.script["ENDINGS"][random.randint(0, num_endings - 1)]





